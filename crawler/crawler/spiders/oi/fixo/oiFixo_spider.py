import scrapy
import requests
import datetime

class QuotesSpider(scrapy.Spider):
    name = "oiFixo"
    start_urls = [
        'https://www.oi.com.br/fixo/',
    ]

    def parse(self, response):
        for content in response.css('tbody'):

            dadosPre = content.css('span.integer::text').extract_first()

            operadora = 'Oi'
            plano = 'Fixo'
            preco = 'R$ ' + str(dadosPre) + ',90'
            detalhes = 'Ligações Locais: Ilimitado* + Ligações DDD: Ilimitado* + Ligações Celular: Ilimitado*'

            if dadosPre is not None:
                r = requests.get('https://descubra-api.herokuapp.com/add/fixo/' + operadora +
                                 '/' + plano + '/' + preco + '/' + detalhes)

                yield {
                    'Date': str(datetime.datetime.now()),
                    'Spider': 'oiFixo',
                    'Status': r.status_code,
                    'Response': r.text
                }
