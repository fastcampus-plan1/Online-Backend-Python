import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec

def scrap_kakao_place_info(place_id):
    url = f"https://place.map.kakao.com/{place_id}"
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(url)

    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "link_tag")))
    
    # Review
    review_more_btn = driver.find_element(By.XPATH, "//div[@class='cont_review']//div[@class='wrap_list']//a[@class='link_more']")
    if review_more_btn:
        for _ in range(2):
            review_more_btn.click()
            time.sleep(1)

    html_content = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html_content, 'html.parser')
    tag_group = soup.find('span', class_='tag_g')
    link_tags = tag_group.find_all('a', class_='link_tag')
    texts = []
    if link_tags:
        texts = [tag.text.lstrip('#') for tag in link_tags if tag.text.startswith('#')]

    list_facility = soup.find('ul', class_='list_facility')
    if list_facility:
        facility_tags = list_facility.find_all('span', class_='color_g')
        texts += [tag.text for tag in facility_tags]

    # Review
    review_list = []
    review_a_tags = soup.find_all('a', class_='link_review')
    for a_tag in review_a_tags:
        title = a_tag.find('strong', class_='tit_story')
        review_list.append((title.text, a_tag["href"]))
    

    # Menu
    menu_list = []
    menu_div = soup.find_all("div", class_="info_menu")
    for m in menu_div:
        menu_span = m.find("span", class_="loss_word")
        price_em = m.find("em", class_="price_menu")
        screen_out_el = price_em.find("span", class_="screen_out")
        if screen_out_el:
            screen_out_el.decompose()
        menu_item = {"name": menu_span.text, "price": price_em.text}
        menu_list.append(menu_item)
    

    return {
        "tags": ["".join(t.split()) for t in texts],
        "review_list": review_list,
        "menu_item": menu_list,
    }


