# Cotação de moedas com base no dolar

O projeto Django que consome e persiste os dados da api vatcomply.com 

## Regras de Implementação
- Sistema que guarde as cotações do dólar versus real, euro e iene(JPY) e que as exibe em um gráfico, respeitando as seguintes especificações:

- Inicialmente o gráfico deve conter as cotações dos últimos cinco dias úteis.

- Deve ser possível alterar o período contanto que seja de no máximo 5 dias úteis.

- Deve ser possível variar as moedas (real, euro e iene). 


## Instalação

```
$ docker-compose up -d --build
```
```
$ docker-compose exec web python collectstatic --noinput
```

```
$ docker-compose exec web python manage.py migrate
```


## Informações complementares 


altere a crontab para o intervalo desejado para ver as tasks no painel do Flower http://localhost:5566/




## Acessando Aplicação

[http://localhost:8000](http://localhost:8000).

## Acessando API

[http://localhost:8000/api/v1/rates/](http://localhost:8000/api/v1/rates/).

## Acessando Flower

[http://localhost:5566/](http://localhost:5566/).



