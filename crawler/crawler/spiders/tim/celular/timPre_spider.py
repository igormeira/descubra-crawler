import scrapy
import requests
import datetime

class QuotesSpider(scrapy.Spider):
    name = "timPre"
    start_urls = [
        'http://www.tim.com.br/pb/para-voce/planos/pre-pago/tim-pre',
    ]

    def parse(self, response):
        for content in response.css('div.offercards__item'):

            dadosInt = content.css('span.tp-card__internetbwvalue::text').extract_first()
            dadosMet = content.css('span.tp-card__internetbwtype::text').extract_first()
            dadosLig = content.css('span.offercards__benefits::text').extract_first()
            dadosPre = content.css('span.offercards__itemvalue-price::text').extract_first()
            dadosVal = content.css('span.offercards__itemvalue-periodicity::text').extract_first()

            operadora = 'TIM'
            plano = 'Pre'
            internet = str(dadosInt) + str(dadosMet)
            preco = 'R$ ' + str(dadosPre)
            detalhes = str(dadosLig)
            validade = dadosVal[3:]

            if (dadosInt is not None):
                r = requests.get('https://descubra-api.herokuapp.com/add/celular/' + operadora +
                                 '/' + plano + '/' + preco + '/' + validade + '/' + internet + '/' + detalhes)

                yield {
                    'Date': str(datetime.datetime.now()),
                    'Spider': 'timPre',
                    'Status': r.status_code,
                    'Response': r.text
                }