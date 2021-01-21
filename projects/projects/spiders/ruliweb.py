import scrapy


class RuliwebSpider(scrapy.Spider):
    name = 'ruliweb'
    allowed_domains = ['https://bbs.ruliweb.com/best/best/now?orderby=best_id']
    start_urls = ['http://https://bbs.ruliweb.com/best/best/now?orderby=best_id/']

    def parse(self, response):
        pass
