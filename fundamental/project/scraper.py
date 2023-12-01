from bs4 import BeautifulSoup
import requests
import re

class Scraper:
    def __init__(self):
        self.__url = "https://www.musinsa.com/app/contents/onsale"
        self.__params = {
            "d_cat_cd": "018", 
            "page_kind": "onsale", 
            "list_kind": "small", 
            "sort": "pop_category", 
            "page": "1", 
            "display_cnt": "90", 
            "sale_fr_rate": "70", 
            "sale_yn": "Y", 
            "sale_dt_yn": "Y", 
            "sale_campaign_yn": "N", 
            "chk_timesale": "on", 
        }
        self.__headers = {
            "user-agent": "'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'"
        }
        self.__price_pattern = re.compile(r'[\d,]+원')

    def do(self):
        response = requests.get(self.__url, params=self.__params, headers=self.__headers)
        soup = BeautifulSoup(response.text, "html.parser")
        item_boxes = soup.find("div", class_="list-box").find_all("li", class_="li_box")

        result = []
        for item_box in item_boxes:
            # 브랜드명 가져오기
            item_title = item_box.find("p", class_="item_title").findChild("a")
            brand = item_title.text

            # 아이템 이름, URL 가져오기
            item_link = item_box.find("p", class_="list_info").findChild("a")
            name = item_link.text.strip()
            url = "https://www.musinsa.com" + item_link["href"]

            # 가격정보 가져오기
            item_price = item_box.find("p", class_="price")
            prices = self.__price_pattern.findall(item_price.text)

            # 이미지 가져오기
            img_box = "https:" + (item_box.find("div", class_="list_img").find("img")["data-original"])

            item = {
                "brand": brand,
                "name": name,
                "url": url,
                "original_price": prices[0],
                "sale_price": prices[1],
                "image": img_box
            }

            result.append(item)
        
        return result
                
if __name__ == "__main__":
    scraper = Scraper()
    items = scraper.do()
    print(items)
