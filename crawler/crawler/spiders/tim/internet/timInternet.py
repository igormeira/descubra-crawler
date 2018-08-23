import scrapy
import requests
import datetime

class QuotesSpider(scrapy.Spider):
    name = "timInternet"
    start_urls = [
        'http://www.tim.com.br/pb/para-voce/internet/internet-para-casa/tim-live-internet',
    ]

    def parse(self, response):
        for content in response.css('div.offercards__item'):

            dadosVel = content.css('span.tbe-card__internetbwvalue::text').extract_first()
            dadosMet = content.css('small::text').extract_first()
            dadosFra = content.css('li.tbe-card__textfeature::text').extract_first()
            dadosPre = content.css('span.offercards__itemvalue-price::text').extract_first()
            dadosDU = content.css('li.offercards__plans-description__item::text').extract()

            provedor = 'TIM'
            plano = str(dadosVel) + ' ' + str(dadosMet)
            preco = 'R$ ' + str(dadosPre)
            validade = '1 Mês'
            detalhes = str(dadosFra) + ' (' + str(dadosDU[0]) + ', ' + str(dadosDU[1]) + ')'

            if dadosPre is not None:
                r = requests.get('https://descubra-api.herokuapp.com/add/internet/' + provedor +
                                 '/' + plano + '/' + preco + '/' + validade + '/' + detalhes)

                yield {
                    'Date': str(datetime.datetime.now()),
                    'Spider': 'timInternet',
                    'Status': r.status_code,
                    'Response': r.text
                }
