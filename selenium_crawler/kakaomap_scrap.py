from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def get_data_from_kakaomap():
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        # 웹사이트 열기
        driver.get("https://map.kakao.com/")
        wait = WebDriverWait(driver, 10)
        wait.until(ec.visibility_of_element_located((By.ID, "search.keyword.query")))

        # 검색창에 검색어 입력하기
        search_input = driver.find_element(By.ID, "search.keyword.query")
        # wait until the element is visible
        search_input.send_keys("강남구 카페")
        search_input.send_keys(Keys.ENTER)
        wait = WebDriverWait(driver, 10)
        wait.until(ec.element_to_be_clickable((By.ID, "info.search.place.more")))

        driver.execute_script("""
            var element = document.getElementById('dimmedLayer')
            if (element) {
                element.className = 'DimmedLayer HIDDEN';
            }
        """)

        show_more_btn = driver.find_element(By.ID, "info.search.place.more")
        show_more_btn.click()

        wait = WebDriverWait(driver, 10)
        wait.until(ec.visibility_of_element_located((By.ID, "info.search.page")))

        page_count = 0
        items = []

        while page_count <= 5:
            page_count += 1
            page_num = page_count % 5 if page_count % 5 != 0 else 5

            page_btn_id = f"info.search.page.no{page_num}"
            next_btn = driver.find_element(By.ID, page_btn_id)
            next_btn.click()
            wait = WebDriverWait(driver, 10)
            wait.until(ec.visibility_of_element_located((By.ID, "info.search.place.list")))

            place_list = driver.find_element(By.ID, "info.search.place.list")
            shop_list = place_list.get_attribute("innerHTML")

            get_items(shop_list, items)
            sleep(2)

        
        driver.quit()
        return items
    except Exception as e:
        print(e)
        raise e
    
    
def get_items(html: str, parsed_items: list):
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, "html.parser")
    items = soup.select("li.PlaceItem.clickArea")
    for item in items:
        item_dict = {}
        item_dict["name"] = item.find('span', {'data-id': 'screenOutName'}).text
        item_dict["score"] = item.find('em', {'data-id': 'scoreNum'}).text
        item_dict["address"] = item.find('p', {'data-id': 'address'}).text
        item_dict["hour"] = item.find('a', {'data-id': 'periodTxt'}).text
        parsed_items.append(item_dict)

    return parsed_items