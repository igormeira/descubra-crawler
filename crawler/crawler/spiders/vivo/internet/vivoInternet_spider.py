import scrapy


class QuotesSpider(scrapy.Spider):
    name = "vivoInternet"
    start_urls = [
        'https://assine.vivo.com.br/banda-larga',
    ]

    def parse(self, response):
        for content in response.css('article.header-card-purple'):
            yield {
                'vel': content.css('h2.title-description-medium::text').extract_first(),
                'det': content.css('li.list-item::text').extract,
                'pre': content.css('strong.value-large::text').extract_first(),
            }
