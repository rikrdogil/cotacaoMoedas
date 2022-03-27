import datetime
import json
from locale import currency
import time
from django.shortcuts import render, redirect
import requests
from django.db.models import Subquery
from decimal import Decimal

from app.models import Rate,BaseRate, Currency


def save_rates(dados):
   
    rates = dados["rates"]
    date=dados["date"]
    base=dados["base"]  

    if not BaseRate.objects.filter(date=date,base=base ).exists():
        rate_base = BaseRate( date = date, base = base )
        rate_base.save()
        rate_base_pk = BaseRate.objects.get(pk=rate_base.id)
        for key, value in rates.items():
            if not Rate.objects.filter(base_rate=rate_base_pk, rate=key ).exists():
                rate_data = Rate(rate = key, valor = value,  base_rate=rate_base_pk)
                rate_data.save()
            

def save_currencies(dados):

   for key, value in dados.items():
    if not Currency.objects.filter(sigla=key,name=value["name"]).exists():
        currency_data = Currency(sigla = key, name = value["name"],  symbol=value["symbol"])
        currency_data.save()
   