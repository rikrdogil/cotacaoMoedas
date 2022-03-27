import datetime
import json
import time
from turtle import st
from django.shortcuts import render, redirect
from django.db.models import Subquery
from decimal import Decimal
from django.db.models import Q
from django.http import JsonResponse
from django.http import HttpResponse
from app.models import Currency, Rate, BaseRate
from app.tasks import GetCurrencyClass, GetRateClass

''' 
  Método que gera os filtros das moedas solicitadas no desafio
'''  

def home_app(request):
   
    moeda = "BRL"
    data_inicial = ""
    data_final = ""
    m=""
    if request.method == 'GET' and 'rate' and 'data_inicial' and 'data_final' in request.GET:
        moeda = request.GET["rate"]
        data_inicial = request.GET["data_inicial"]
        data_final = request.GET["data_final"]
    if request.method == 'GET' and 'm'  in request.GET:
        m = request.GET["m"]

    filtro_moedas = (Q(sigla="BRL") | Q(sigla="JPY") | Q(sigla="EUR")) 
    if m=='all':
        filtro_moedas =(Q(id__gte=1)) 
    combomoedas = list(Currency.objects.filter(filtro_moedas).order_by('name'))
    if not combomoedas:
        # executa a task que importa o endpoint correncies  caso não exista dados na tabela
        GetCurrencyClass.get_currencies()
        combomoedas = list(Currency.objects.filter(filtro_moedas).order_by('name') )


    # # lista de datas das cotacoes usadas no eixo X do gráfico
    datas_cotacoes = list(BaseRate.objects.order_by('date').values_list('date', flat=True)[:5])
    if not datas_cotacoes:
        # executa a task que importa as cotações dos ultimos 5 dias uteis da API exter
        GetRateClass.get_rates_api_inicial()
        datas_cotacoes = list(BaseRate.objects.order_by('date').values_list('date', flat=True))
        
    # lista todas o historico de cotacao da moeda escolhida
    if data_inicial and data_final:
        rates= Rate.objects.select_related('base_rate').filter(rate=moeda,base_rate__date__gte=data_inicial, base_rate__date__lte=data_final)
    else:
        rates= Rate.objects.select_related('base_rate').filter(rate=moeda)

    # montagem do corpo do dicionario e o preenchimento 
    moedas_series_request = {"name":"",  "data": [],  "type": 'area' }
    moedas_series_request["name"]=moeda
    for rate in rates:
        valor_formatado = "{:.2f}".format(rate.valor)
        moedas_series_request["data"].append(float(valor_formatado))
            
    return render(request, 'index.html',{'datas_cotacoes':json.dumps(datas_cotacoes,default=str),'series_moedas':moedas_series_request,'combo_moedas': combomoedas})
