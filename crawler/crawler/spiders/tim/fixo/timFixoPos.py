import scrapy
import requests
import datetime

class QuotesSpider(scrapy.Spider):
    name = "timFixoPos"
    start_urls = [
        'http://www.tim.com.br/pb/para-voce/planos/fixo/tim-fixo-pos',
    ]

    def parse(self, response):
        for content in response.css('li.oferta'):

            dadosTit = content.css('h3::text').extract_first()
            dadosPre = content.css('div.valor::text').extract_first()

            operadora = 'TIM'
            plano = 'Pós ' + str(dadosTit)
            preco = 'R$ ' + str(dadosPre) + ' por mês'
            detalhes = 'None'


            if dadosPre is not None:
                r = requests.get('https://descubra-api.herokuapp.com/add/fixo/' + operadora +
                                 '/' + plano + '/' + preco + '/' + detalhes)

                yield {
                    'Date': str(datetime.datetime.now()),
                    'Spider': 'timFixoPos',
                    'Status': r.status_code,
                    'Response': r.text
                }
