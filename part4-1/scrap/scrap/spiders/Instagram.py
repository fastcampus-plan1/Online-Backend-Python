import scrapy
from http.cookies import SimpleCookie
import json


class InstagramSpider(scrapy.Spider):
    name = 'insta'
    allowed_domains = ['www.instagram.com']
    # start_urls = ['http://www.instagram.com/']
    headers = {
        "x-asbd-id": 129477,
        "x-csrftoken": "6DprFERzTmSJtteHlIeOw0wyKRsDdRGB",
        "x-ig-app-id": 936619743392459,
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
                    print(caption['text'])
                    print("="*50)
            elif tag_post['feed_type'] == 'media':
                for post in tag_post['layout_content']['medias']:
                    media = post['media']
                    caption = media['caption']
                    print(caption['text'], "\n")
                    print("="*50)
            else:
                print('feed type is not clips or feed_type')



def cookie_parse():
    cookie_string = 'ig_did=1DE266FE-5C49-45E3-892B-86741CB7868A; datr=8HeKZb-6hjnBWqB4cKyoXxiE; mid=ZYp39gAEAAFMKVyKt4SEUK203mFN; ig_nrcb=1; shbid="19471\0542256592870\0541735109521:01f72d5c6970e1a0fca4bc8897ccb341d889f5231cb66cce76fdd6de4e57bae9e0d7e50b"; shbts="1703573521\0542256592870\0541735109521:01f79be2ff6e20ca834ca56512a56725ba2f94d2ad26b81f16fa84ea24475a66697b974c"; csrftoken=6DprFERzTmSJtteHlIeOw0wyKRsDdRGB; ds_user_id=2256592870; sessionid=2256592870%3AZYW6OfKaAyBraw%3A1%3AAYdrtMDDvp5ExPNcRGz_2nKhT23-8bZCaxnKfTw4UQ; dpr=1; rur="CCO\0542256592870\0541735311382:01f7027262b845a84f6de323d6605fed493fc7e9868172a139bf4cd450e5f6d171c96c7d"'
    #enter your cookies in the cookie string variable
    cookie = SimpleCookie()
    cookie.load(cookie_string)

    cookies = {}

    for key, value in cookie.items():
        cookies[key] = value.value
    
    return cookies