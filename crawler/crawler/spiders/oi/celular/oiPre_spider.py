import datetime
import requests
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "oiPre"
    start_urls = [
        'https://www.oi.com.br/celular/pre-pago/',
    ]

    def parse(self, response):
        for content in response.css('div.card-wrapper'):

            dadosVel = content.css('span.card-title::text').extract_first()
            dadosDe1 = content.css('span.card-description-highlight::text').extract_first()
            dadosDe2 = content.css('span.card-text-small::text').extract_first()
            dadosPre = content.css('span.integer::text').extract_first()
            dadosVal = content.css('strong::text').extract_first()

            operadora = 'Oi'
            plano = 'Pre'
            internet = str(dadosVel)
            preco = 'R$ ' + str(dadosPre) + ',00'
            validade = str(dadosVal)
            detalhes = str(dadosDe1) + ' + ' + str(dadosDe2)

            if dadosPre is not None:
                r = requests.get('https://descubra-api.herokuapp.com/add/celular/' + operadora +
                                 '/' + plano + '/' + preco + '/' + validade + '/' + internet + '/' + detalhes)

                yield {
                    'Date': str(datetime.datetime.now()),
                    'Spider': 'oiPré',
                    'Status': r.status_code,
                    'Response': r.text
                }
