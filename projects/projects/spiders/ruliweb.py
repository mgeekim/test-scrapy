import re
import scrapy
import better_exceptions
better_exceptions.hook()

class RuliwebSpider(scrapy.Spider):
    name = 'ruliweb'
    allowed_domains = ['bbs.ruliweb.com/best/best/now?orderby=best_id']
    start_urls = ['http://bbs.ruliweb.com/best/best/now?orderby=best_id/']

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
                item = {
                    'user'   : user,
                    'title'  : title,
                    'recomd' : recomd,
                }
                print(item)