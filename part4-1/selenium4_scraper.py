from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# WebDriver 경로 설정
driver_path = '/Users/ryan/Online-Backend-Python/chromedriver'
service = Service(executable_path=driver_path)

# ChromeDriver를 통해 Chrome 브라우저 실행
browser = webdriver.Chrome(service=service)

# 웹 페이지 열기
browser.get('https://www.google.com')
