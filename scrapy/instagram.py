import scrapy
import time

class InstagramSpider(scrapy.Spider):
    name = 'instagram'
    start_urls = ['https://www.instagram.com/']

    def parse(self, response):
        # Fill in email field
        email_field = response.css('input._aa4b._add6._ac4d._ap35')[0]
        email_field.send_keys('hymium@gmail.com')

        # Fill in password field
        password_field = response.css('input._aa4b._add6._ac4d._ap35')[1]
        password_field.send_keys('Dlflffk88!')

        # Wait for 1 second
        time.sleep(1)

        # Click login button
        login_button = response.css('button._acan._acap._acas._aj1-._ap30')[0]
        login_button.click()

        # Move to explore page
        explore_url = 'https://www.instagram.com/explore/tags/knotted_donut/'
        yield scrapy.Request(explore_url, callback=self.parse_explore)

    def parse_explore(self, response):
        # Print current HTML
        print(response.body)


# Run spider
# $ scrapy runspider instagram.py

