import scrapy
from scrap.items import FastcampusItem


class FastcampusspiderSpider(scrapy.Spider):
    name = "FastcampusSpider"
    allowed_domains = ["fastcampus.co.kr"]
    custom_settings = {
        "DOWNLOAD_DELAY": 1,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 10,
        "HTTPCACHE_STORAGE": "scrapy.extensions.httpcache.FilesystemCacheStorage",
        "DOWNLOADER_MIDDLEWARES": {
            "scrap.middlewares.ScrapDownloaderMiddleware": 2,
        }
    }
    start_urls = [
        "https://fastcampus.co.kr/.api/www/categories/10/page",
        "https://fastcampus.co.kr/.api/www/categories/10/page",
        "https://fastcampus.co.kr/.api/www/categories/10/page",
        "https://fastcampus.co.kr/.api/www/categories/10/page",
        "https://fastcampus.co.kr/.api/www/categories/10/page",
        "https://fastcampus.co.kr/.api/www/categories/10/page",
        "https://fastcampus.co.kr/.api/www/categories/10/page",
    ]

    def parse(self, response):
        # 데이터 변환 함수 호출
        data = response.json().get("data", {})
        data = data.get("categoryInfo", {})
        yield from self.transform_data(data)

    def transform_data(self, data):
        for item in data.get("courses", []):
            yield FastcampusItem(
                public_title=item.get("publicTitle"),
                public_description=item.get("publicDescription"),
                keywords=item.get("keywords"),
                img=item.get("img")
            )
