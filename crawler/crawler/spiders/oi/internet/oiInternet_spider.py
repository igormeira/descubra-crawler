import datetime
import requests
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "oiInternet"
    start_urls = [
        'https://www.oi.com.br/internet/',
    ]

    def parse(self, response):
        for content in response.css('div.CardInternet'):

            dadosVel = content.css('span.card-title::text').extract_first()
            dadosPre = content.css('span.integer::text').extract_first()

            provedor = 'Oi'
            plano = str(dadosVel)
            preco = 'R$ ' + str(dadosPre) + ',90'
            validade = '1 Mês'
            detalhes = 'Download até ' + str(dadosVel)

            if dadosPre is not None:
                r = requests.get('https://descubra-api.herokuapp.com/add/internet/' + provedor +
                                 '/' + plano + '/' + preco + '/' + validade + '/' + detalhes)

                yield {
                    'Date': str(datetime.datetime.now()),
                    'Spider': 'oiInternet',
                    'Status': r.status_code,
                    'Response': r.text
                }
