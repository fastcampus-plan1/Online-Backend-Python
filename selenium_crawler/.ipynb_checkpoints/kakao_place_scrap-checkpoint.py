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
    return ["".join(t.split()) for t in texts]


