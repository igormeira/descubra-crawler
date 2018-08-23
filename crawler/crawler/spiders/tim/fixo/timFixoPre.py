import scrapy
import requests
import datetime

class QuotesSpider(scrapy.Spider):
    name = "timFixoPre"
    start_urls = [
        'http://www.tim.com.br/pb/para-voce/planos/fixo/tim-fixo-pre',
    ]

    def parse(self, response):
        for content in response.css('div.tim-price'):

            dadosText = content.css('p.period::text').extract_first()
            dadosPre = content.css('p.price::text').extract_first()

            operadora = 'TIM'
            plano = 'Pré'
            preco = str(dadosText) + ' ' + str(dadosPre) + ' por minuto'
            detalhes = 'None'

            if dadosPre is not None:
                r = requests.get('https://descubra-api.herokuapp.com/add/fixo/' + operadora +
                                 '/' + plano + '/' + preco + '/' + detalhes)

                yield {
                    'Date': str(datetime.datetime.now()),
                    'Spider': 'timFixoPre',
                    'Status': r.status_code,
                    'Response': r.text
                }
