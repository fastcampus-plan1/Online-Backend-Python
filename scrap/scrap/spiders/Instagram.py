import scrapy
from http.cookies import SimpleCookie
import json


class InstagramSpider(scrapy.Spider):
    name = 'insta'
    allowed_domains = ['www.instagram.com']
    # start_urls = ['http://www.instagram.com/']
    headers = {
        "x-asbd-id": 45678,
        "x-csrftoken": "<csrftoken>",
        "x-ig-app-id": 12345,
        "x-requested-with": "XMLHttpRequest"
    }

    def start_requests(self):
        yield scrapy.Request(
            url=f'https://www.instagram.com/api/v1/tags/web_info/?tag_name=%EB%85%B8%ED%8B%B0%EB%93%9C%EC%B2%AD%EB%8B%B4',
            cookies = cookie_parse(),
            headers=self.headers,
            callback=self.parse
        )

    def parse(self, response):
        resp = json.loads(response.body)
        tag_posts = resp['data']['top']['sections']
        for tag_post in tag_posts:
            if tag_post['feed_type'] == 'clips':
                for post in tag_post['layout_content']['fill_items']:
                    media = post['media']
                    caption = media['caption']
                    print(caption['text'], "\n")
            elif tag_post['feed_type'] == 'media':
                for post in tag_post['layout_content']['medias']:
                    media = post['media']
                    caption = media['caption']
                    print(caption['text'], "\n")
            else:
                print('feed type is not clips or feed_type')



def cookie_parse():
    cookie_string = 'this_is_cookie'
    #enter your cookies in the cookie string variable
    cookie = SimpleCookie()
    cookie.load(cookie_string)

    cookies = {}

    for key, value in cookie.items():
        cookies[key] = value.value
    
    return cookies