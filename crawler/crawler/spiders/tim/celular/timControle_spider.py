import scrapy
import requests
import datetime

class QuotesSpider(scrapy.Spider):
    name = "timControle"
    start_urls = [
        'http://www.tim.com.br/pb/para-voce/planos/controle',
    ]

    def parse(self, response):
        for content in response.css('div.tim-controle__plan'):

            dadosInt = content.css('span.tim-controle__plan-infos__internet::text').extract_first()
            dadosLig = content.css('p.tim-controle__plan-infos__info::text').extract()
            dadosPre = content.css('span strong::text').extract_first()

            operadora = 'TIM'
            plano = 'Controle'
            internet = str(dadosInt) + 'GB'
            preco = 'R$ ' + str(dadosPre)
            detalhes = str(dadosLig[0]) + ' + ' + str(dadosLig[1])
            validade = '1 Mês'

            if (dadosInt is not None):
                r = requests.get('https://descubra-api.herokuapp.com/add/celular/' + operadora +
                                 '/' + plano + '/' + preco + '/' + validade + '/' + internet + '/' + detalhes)

                yield {
                    'Date': str(datetime.datetime.now()),
                    'Spider': 'timControle',
                    'Status': r.status_code,
                    'Response': r.text
                }