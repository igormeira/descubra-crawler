import datetime
import requests
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "oiTv"
    start_urls = [
        'https://www.oi.com.br/tv-hd/',
    ]

    def parse(self, response):
        for content in response.css('div.card-content'):

            dadosPla = content.css('span.card-product::text').extract_first()
            dadosPre = content.css('span.integer::text').extract_first()
            dadosDe1 = content.css('span.card-title::text').extract()
            dadosDe2 = content.css('span.card-subtitle::text').extract()

            provedor = 'Oi'
            plano = str(dadosPla)
            preco = 'R$ ' + str(dadosPre) + ',90'
            detalhes = str(dadosDe1[0]) + str(dadosDe1[1]) + ', ' + str(dadosDe2[0]) + str(dadosDe2[1]) + str(dadosDe2[2])

            if dadosPre is not None:
                r = requests.get('https://descubra-api.herokuapp.com/add/tv/' + provedor +
                                 '/' + plano + '/' + preco + '/' + detalhes)

                yield {
                    'Date': str(datetime.datetime.now()),
                    'Spider': 'oiTv',
                    'Status': r.status_code,
                    'Response': r.text
                }
