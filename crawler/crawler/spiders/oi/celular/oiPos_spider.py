import datetime
import requests
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "oiPos"
    start_urls = [
        'https://www.oi.com.br/celular/pos-pago/',
    ]

    def parse(self, response):
        for content in response.css('div.card-content'):

            dadosPla = content.css('span.offer-title::text').extract_first()
            dadosVel = content.css('span.card-title::text').extract_first()
            dadosDet = content.css('span.card-description-highlight::text').extract_first()
            dadosPre = content.css('span.integer::text').extract_first()

            operadora = 'Oi'
            plano = 'Pos'
            internet = str(dadosPla)
            preco = 'R$ ' + str(dadosPre) + ',90'
            validade = '1 Mês'
            detalhes = str(dadosVel) + ' + ' + str(dadosDet)

            if dadosPre is not None:
                r = requests.get('https://descubra-api.herokuapp.com/add/celular/' + operadora +
                                 '/' + plano + '/' + preco + '/' + validade + '/' + internet + '/' + detalhes)

                yield {
                    'Date': str(datetime.datetime.now()),
                    'Spider': 'oiPós',
                    'Status': r.status_code,
                    'Response': r.text
                }
