import scrapy
import json

class YourSpiderName(scrapy.Spider):
    name = 'your_spider_name'
    start_urls = ['https://fooddelivery.mykeeta.com/api/v1/homePage/homePageInfo']
    headers = {
        'deviceType': 'sdk_gphone64_arm64',
        'Accept-Language': 'en',
        'appVersion': '1.1.10',
        'retrofit_exec_time': '1700590724587',
        'timeZone': 'GMT+08:00',
        'M-SHARK-TRACEID': '5171f71126b2d4544b38a98a4ff0e4cd66d7a16999806706990672227d03c17005907245875e1c22',
        'cityId': '810001',
        'locale': 'en',
        'uuid': '00000000000007024EEFCC47C49358643C0AE382C498BA169998067154711603',
        'platform': '4',
        'clientType': 'c_android',
        'districtId': '8100019',
        'osVersion': '33_13',
        'partner': '85204',
        'seq_id': '13',
        'region': 'HK',
        'request_id': '28BAC42F-6E16-4DFD-B978-EE48F2BEA1AF',
        'Content-Type': 'application/json; charset=UTF-8',
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 13; sdk_gphone64_arm64 Build/TE1A.220922.034)',
    }
    json_data = {
        'location': {
            'latitude': '22.31924733900611',
            'longitude': '114.1692228242755',
        },
    }

    def parse(self, response):
        yield scrapy.Request(
            self.start_urls[0],
            method='POST',
            headers=self.headers,
            body=json.dumps(self.json_data),
            callback=self.parse_result,
            meta={'dont_merge_cookies': True},
        )

    def parse_result(self, response):
        data = json.loads(response.text)
        yield {'data': data}
