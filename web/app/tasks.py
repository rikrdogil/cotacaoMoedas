import os
from datetime import datetime, timedelta
from celery.utils.log import get_task_logger
from cotacao.celery import celery
from celery.schedules import crontab
from django.shortcuts import render, redirect
from app.models import Rate
import requests
from app.importador import save_rates, save_currencies
from celery import shared_task
from celery import Task
from bizdays import Calendar


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cotacao.settings")
logger = get_task_logger(__name__)


class GetRateClass(Task):

    @shared_task(name='task_get_rates_api_inicial') 
    def get_rates_api_inicial():
       

        cal = Calendar(name='actual')
        datas_uteis = list()
        limit = 6
        
        
        for index in range(limit):
            tamanho_lista = len(datas_uteis)
            if tamanho_lista <= limit:
               
                dia_util = datetime.today().date() - timedelta(days = tamanho_lista)
                print(dia_util)
                print(tamanho_lista)
                if cal.isbizday(dia_util):                
                    url = 'https://api.vatcomply.com/rates?base=USD&date='+str(dia_util)
                    logger.info("Consumo de API iniciada..")    
                    response = requests.get(url)
                    data = response.json()
                    save_rates(data)
                    datas_uteis.append(dia_util)
                    logger.info("Dados enviados para armazenamento")
        
        return "importacao inicial completa" 


    # consumo automatico diariamente
    @shared_task(name='task_get_rates_api') 
    def get_rates_api():
       
        logger.info("Consumo de API iniciada..")
        url = 'https://api.vatcomply.com/rates?base=USD'
        response = requests.get(url)
        data = response.json()
        save_rates(data)
        logger.info("Dados enviados para armazenamento")
        
        return data  
  
class GetCurrencyClass(Task):
     
    @shared_task(name='task_get_currencies') 
    def get_currencies():
        logger.info("Consumo de API currencies iniciada.")
        url = 'https://api.vatcomply.com/currencies'
        response = requests.get(url)
        data = response.json()
        save_currencies(data)
    
        logger.info("currencies enviados para armazenamento")
        
        return data  


