import scrapy


class QuotesSpider(scrapy.Spider):
    name = "claro"
    start_urls = [
        'https://www.claro.com.br/celular/pos/detalhes-do-plano-7gb1',
        'https://www.claro.com.br/celular/pos/detalhes-do-plano-10-gb1',
        'https://www.claro.com.br/celular/pos/detalhes-do-plano-15-gb1',
        'https://www.claro.com.br/celular/pos/detalhes-do-plano-30gb1',
        'https://www.claro.com.br/celular/pos/detalhes-do-plano-60gb1',
    ]

    def parse(self, response):
        for content in response.css('div.col-sm-12'):
            yield {
                'begin1': content.css('div strong span span::text').extract_first(),
                'begin2': content.css('div::text').extract_first(),
                'begin3': content.css('p strong::text').extract_first(),
                'begin4': content.css('p span strong::text').extract_first(),
                'beginDebito': content.css('div div div strong span::text').extract_first(),
                'beginBoleto': content.css('div p strong::text').extract(),
            }
        for content in response.css('div.col-md-6'):
            yield {
                'medle': content.css('p::text').extract(),
            }
