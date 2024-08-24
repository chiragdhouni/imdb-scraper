import scrapy


class Info(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = scrapy.Field()
    genres = scrapy.Field()

    rating = scrapy.Field() 

    description = scrapy.Field()    