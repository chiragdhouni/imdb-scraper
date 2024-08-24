import json
import scrapy

from imdbScraper.items import Info


class ImdbspiderSpider(scrapy.Spider):
    name = "imdbspider"
    allowed_domains = ["imdb.com"]
    start_urls = ["https://imdb.com/chart/top/"]

    def parse(self, response):
        
        raw_data = response.css("script[id='__NEXT_DATA__']::text").get()

        json_data = json.loads(raw_data)

        needed_data = json_data['props']['pageProps']['pageData']['chartTitles']['edges']

        information = Info()

        for movie in needed_data:

            temp = movie['node']['titleGenres']['genres']
            information['genres'] =[]
            for i in range(len(temp)):
                information['genres'].append(temp[i]['genre']['text'])


            information['title'] = movie['node']['titleText']['text'],
            
            information['rating']  = movie['node']['ratingsSummary']['aggregateRating'],
            information['description']  = movie['node']['plot']['plotText']['plainText']
            
            yield information