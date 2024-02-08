import json
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from sqlalchemy import MetaData, text
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from .restuarant_crawler import get_webdriver, get_sql_connection, wait_until_visible


def scrap_kakao_place_info(driver, place_id):
    url = f"https://place.map.kakao.com/{place_id}"
    driver.get(url)
    wait_until_visible(driver, By.CLASS_NAME, "link_tag")
    
    # Review
    review_more_btn = driver.find_element(By.XPATH, "//div[@class='cont_review']//div[@class='wrap_list']//a[@class='link_more']")
    if review_more_btn:
        for _ in range(2):
            review_more_btn.click()
            time.sleep(1)

    html_content = driver.page_source

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
        next_sibling = a_tag.find_next_sibling("span", class_="info_user")
        if not next_sibling:
            pub_date = None
        else:
            pub_date_el = next_sibling.find("span", class_="txt_date")
            pub_date = pub_date_el.text if pub_date_el else None
        title = a_tag.find('strong', class_='tit_story')
        review_list.append((title.text, a_tag["href"], pub_date))
    
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


def save_data_to_sql(sql_conn, info, place_id, db_id):
    menu = info.get("menu_item", [])
    tags = ",".join(info.get("tags", []))
    review = info.get("review_list", [])
    
    restaurant_table = "restaurants"  # 테이블 이름
    restaurant_review_table = "restaurant_blog_reviews"  # 테이블 이름
    where_condition = f"id = {db_id}"  # 조건 (예: ID가 1인 레코드를 업데이트)

    # Raw SQL 쿼리 작성
    sql = text(f"""
        UPDATE {restaurant_table}
        SET menu = :menu_item,
            tags = :tags
        WHERE {where_condition}
    """)
    sql = sql.bindparams(menu_item=json.dumps(menu), tags=tags)
    sql_conn.execute(sql)

    for title, href, pub_date in review:
        select_sql_for_check_url = text(f"""
            SELECT id
            FROM {restaurant_review_table}
            WHERE blog_url = :url
        """)
        select_sql_for_check_url = select_sql_for_check_url.bindparams(url=href)
        result = sql_conn.execute(select_sql_for_check_url).fetchone()
        if result:
            continue

        sql = text(f"""
            INSERT INTO {restaurant_review_table} (restaurant_id, title, blog_url, published_date)
            VALUES (:restaurant_id, :title, :url, :published_date)
        """)
        sql = sql.bindparams(restaurant_id=db_id, title=title, url=href, published_date=pub_date)
        sql_conn.execute(sql)


def collect_kakao_place_info(place_ids: list[tuple[str]]):
    driver = get_webdriver()
    sql_conn = get_sql_connection()
    try:
        for place_id, db_id in place_ids:
            info = scrap_kakao_place_info(driver, place_id)
            print(place_id)
            save_data_to_sql(sql_conn, info, place_id, db_id)
        sql_conn.commit()
    finally:
        sql_conn.close()
        driver.quit()
