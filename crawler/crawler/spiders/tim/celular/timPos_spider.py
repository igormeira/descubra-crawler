import scrapy
import requests
import datetime

class QuotesSpider(scrapy.Spider):
    name = "timPos"
    start_urls = [
        'http://www.tim.com.br/pb/para-voce/planos/pos-pago/tim-pos',
    ]

    def parse(self, response):
        for content in response.css('div.offercards__item'):

            dadosInt = content.css('span.ddm-card__internetbwvalue::text').extract_first()
            dadosLig = content.css('li.ddm-card__textfeature::text').extract_first()
            dadosPre = content.css('span.offercards__itemvalue-price::text').extract_first()

            operadora = 'TIM'
            plano = 'Pos'
            internet = str(dadosInt) + 'GB'
            preco = 'R$ ' + str(dadosPre)
            detalhes = str(dadosLig)
            validade = '1 Mês'

            if (dadosInt is not None):
                r = requests.get('https://descubra-api.herokuapp.com/add/celular/' + operadora +
                                 '/' + plano + '/' + preco + '/' + validade + '/' + internet + '/' + detalhes)

                yield {
                    'Date': str(datetime.datetime.now()),
                    'Spider': 'timPos',
                    'Status': r.status_code,
                    'Response': r.text
                }
