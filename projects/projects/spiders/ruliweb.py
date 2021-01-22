import re
import scrapy
import time
import better_exceptions
better_exceptions.hook()

from projects.items import ProjectsItem

class RuliwebSpider(scrapy.Spider):
    name = 'ruliweb'
    allowed_domains = ['bbs.ruliweb.com']
    start_urls = ['http://bbs.ruliweb.com/best/best/now?orderby=best_id/']

    def __init__(self, *args, **kwargs):
        super(RuliwebSpider, self).__init__(*args, **kwargs)
        self.next_id    = 1
        self.next_url   = "https://bbs.ruliweb.com/best/best/now?orderby=best_id&range=24h&page={}"
        self.last_id    = 5
        self.sleep_time = 2

    def parse(self, response):
        rule_post  = r'https://bbs\.ruliweb\.com/best/board/300143/read/.*'
        css_each   = '.board_list_table .table_body'
        css_link   = '.subject a[href^="https"]'
        css_user   = '.writer::text'
        css_title  = '.subject a::text'
        css_recomd = '.recomd::text'

        p = re.compile(rule_post)
        for each in response.css(css_each):
            url = each.css(css_link).extract_first()
            if url != None and p.search(url):
                user   = each.css(css_user).extract_first().strip()
                title  = each.css(css_title).extract_first().strip()
                recomd = each.css(css_recomd).extract_first().strip()

                item = ProjectsItem()
                item['user'] = user
                item['title'] = title
                item['recomd'] = recomd
                yield item

        self.next_id += 1
        if not self.next_id > self.last_id:
            time.sleep(self.sleep_time)
            yield scrapy.Request(url=self.next_url.format(self.next_id), callback=self.parse)