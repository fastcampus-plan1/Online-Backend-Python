from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from sqlalchemy import create_engine
from webdriver_manager.chrome import ChromeDriverManager
import googlemaps
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# from api_scrap.geocoding import geocode_address
def get_webdriver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver

def wait_until_visible(driver, by, value, timeout=10):
    wait = WebDriverWait(driver, timeout)
    wait.until(ec.visibility_of_element_located((by, value)))

def wait_until_clickable(driver, by, value, timeout=10):
    wait = WebDriverWait(driver, timeout)
    wait.until(ec.element_to_be_clickable((by, value)))

def input_and_send(driver, by, value, keys):
    field = driver.find_element(by, value)
    field.send_keys(keys)
    field.send_keys(Keys.ENTER)

def click_button(driver, by, value):
    button = driver.find_element(by, value)
    button.click()

def geocode_address(address):
    gmaps = googlemaps.Client(key='AIzaSyB6IABEWjSBFf3Cj5p05y-Z7cJaH94UFDw')
    geocode_result = gmaps.geocode(address)
    if geocode_result:
        location = geocode_result[0]['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']
        return latitude, longitude
    else:
        return None


def get_items(html: str, parsed_items: list, cuisine: str, category: str):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.select("li.PlaceItem.clickArea")
    
    for item in items:
        if item.find('p', {'data-id': 'address'}) is None:
            continue
        loc = geocode_address(item.find('p', {'data-id': 'address'}).text)
        if loc:
            lat, long = loc
        else:
            lat, long = None, None
        more_info = item.find("a", {"data-id": "moreview"})
        place_id = more_info["href"].split("/")[-1]
        parsed_items.append({
            "name": item.find('span', {'data-id': 'screenOutName'}).text,
            "place_id": place_id,
            "address": item.find('p', {'data-id': 'address'}).text,
            "phone": item.find('span', {'data-id': 'phone'}).text,
            "cuisine_type": cuisine,
            "category": category,
            "rating": item.find('em', {'data-id': 'scoreNum'}).text,
            "business_hour": item.find('a', {'data-id': 'periodTxt'}).text,
            "latitude": lat,
            "longitude": long
        })

def get_sql_connection():
    engine = create_engine('mysql+pymysql://root@localhost:3306/fdc_dm?charset=utf8')
    return engine.connect()


def get_data_from_kakaomap(search_keyword: str, cuisine: str, category: str):
    driver = get_webdriver()
    db_conn = get_sql_connection()
    try:
        # 웹사이트 열기
        driver.get("https://map.kakao.com/")
        wait_until_visible(driver, By.ID, "search.keyword.query")

        # 검색창에 검색어 입력하기
        input_and_send(driver, By.ID, "search.keyword.query", search_keyword)
        input_and_send(driver, By.ID, "search.keyword.query", Keys.ENTER)
        wait_until_clickable(driver, By.ID, "info.search.place.more")

        driver.execute_script("""
            var element = document.getElementById('dimmedLayer')
            if (element) {
                element.className = 'DimmedLayer HIDDEN';
            }
        """)

        click_button(driver, By.ID, "info.search.place.more")
        wait_until_visible(driver, By.ID, "info.search.page")

        page_count = 0
        items = []

        while page_count <= 5:
            page_count += 1
            page_num = page_count % 5 if page_count % 5 != 0 else 5

            click_button(driver, By.ID, f"info.search.page.no{page_num}")
            wait_until_visible(driver, By.ID, "info.search.place.list")

            place_list = driver.find_element(By.ID, "info.search.place.list")
            shop_list = place_list.get_attribute("innerHTML")

            get_items(shop_list, items, cuisine, category)
            sleep(1)

        
        driver.quit()

        import pandas as pd
        sql_df = pd.read_sql(f'SELECT name, address FROM restaurants WHERE cuisine_type="{cuisine}" AND category="{category}"', db_conn)
        df = pd.DataFrame(items)
        df.rename(columns={'place_id': 'kakao_place_id'}, inplace=True)
        combined_df = pd.concat([sql_df, df])
        combined_df.drop_duplicates(subset=['name', 'address'], keep=False, inplace=True)
        combined_df["rating"] = pd.to_numeric(combined_df["rating"], errors='coerce')
        combined_df.to_sql("restaurants", db_conn, if_exists='append', index=False)
        db_conn.commit()

        return items
    except Exception as e:
        print(e)
        raise e
    finally:
        db_conn.close()
        driver.quit()
    
    

        