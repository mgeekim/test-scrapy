import scrapy
import better_exceptions
better_exceptions.hook()

class RuliwebSpider(scrapy.Spider):
    name = 'ruliweb'
    allowed_domains = ['bbs.ruliweb.com/best/best/now?orderby=best_id']
    start_urls = ['http://bbs.ruliweb.com/best/best/now?orderby=best_id/']

    def parse(self, response):
        pass
