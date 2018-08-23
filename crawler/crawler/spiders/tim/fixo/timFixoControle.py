import scrapy
import requests
import datetime

class QuotesSpider(scrapy.Spider):
    name = "timFixoControle"
    start_urls = [
        'http://www.tim.com.br/pb/para-voce/planos/fixo/tim-fixo-controle',
    ]

    def parse(self, response):
        for content in response.css('div.tim-price'):

            dadosPre = content.css('p.price::text').extract_first()

            operadora = 'TIM'
            plano = 'Controle'
            preco = str(dadosPre) + ' por minuto'
            detalhes = 'None'

            if dadosPre is not None:
                r = requests.get('https://descubra-api.herokuapp.com/add/fixo/' + operadora +
                                 '/' + plano + '/' + preco + '/' + detalhes)

                yield {
                    'Date': str(datetime.datetime.now()),
                    'Spider': 'timFixoControle',
                    'Status': r.status_code,
                    'Response': r.text
                }
