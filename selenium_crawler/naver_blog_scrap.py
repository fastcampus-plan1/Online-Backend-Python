import re
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def crawl_naver_blog(url):
    # Set up webdriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run Chrome in headless mode
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service,)
    
    driver.get(url)
    iframe_element = driver.find_element(By.ID, "mainFrame")  # iframe의 id를 사용하여 찾는 예시
    driver.switch_to.frame(iframe_element)  # iframe 내부로 전환
    driver.find_element(By.ID, "post-area")  # iframe 안의 엘리먼트의 class로 찾는 예시
    res = driver.page_source
    driver.quit()
    soup = BeautifulSoup(res, "html.parser")
    content = soup.find("div", {"class": "se-main-container"})
    if content is None:
        content = soup.find("div", {"id": "post-area"})
    span_tag = content.find("span", text=re.compile("블로그기자단"))
    if span_tag:
        span_tag.decompose()
    content = content.text
    content = re.sub(r"\n+", " ", content)
    return content


def crawl_naver_blog_by_requests(url):
    res = requests.get(url)
    root_url = "https://blog.naver.com"

    if 'id="mainFrame"' in res.text:
        soup = BeautifulSoup(res.text, "html.parser")
        iframe = soup.find("iframe", {"id": "mainFrame"})
        iframe_src = iframe["src"]
        res = requests.get(root_url + iframe_src)

    soup = BeautifulSoup(res.text, "html.parser")
    content = soup.find("div", {"class": "se-main-container"})
    if content is None:
        content = soup.find("div", {"id": "post-area"})
    span_tag = content.find("span", text=re.compile("블로그기자단"))
    if span_tag:
        span_tag.decompose()
    content = content.text
    content = re.sub(r"\n+", " ", content)
    
    return content