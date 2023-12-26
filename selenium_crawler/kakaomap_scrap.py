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
        wait.until(ec.visibility_of_element_located((By.ID, "info.search.place.list")))

        # 검색 결과 확인
        place_list = driver.find_element(By.ID, "info.search.place.list")
        shop_list = place_list.get_attribute("innerHTML")

        # scroll down to the bottom
        driver.quit()
        return shop_list
    except Exception as e:
        print(e)
        raise e
    
    
