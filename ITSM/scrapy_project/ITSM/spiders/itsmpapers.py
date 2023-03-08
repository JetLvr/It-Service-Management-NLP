import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ItsmpapersSpider(CrawlSpider):
    name = "itsmpapers"
    allowed_domains = ["itsm.tools"]
    start_urls = ["https://itsm.tools/category/automation-and-ai/"]

    rules = (Rule(LinkExtractor(), callback='parse_item', follow=True),)

    def parse_item(self, response):

        spantext = response.xpath("//span[@class='elementor-icon-list-text']/text()").getall()

        title = response.xpath("//h1/text()").get()

        author = spantext[0]

        date = spantext[1]

        category = response.xpath("//span[@class='elementor-icon-list-text']//a/text()").getall()

        body = response.xpath("//p/text()").getall()

        yield {
            'postDate' : date,
            'category' : category,
            'author' : author,
            'title' : title,
            'textBody' : body
        }


