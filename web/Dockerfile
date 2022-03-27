FROM python:3.9-buster

RUN python -m pip install --upgrade pip

COPY ./wait.sh wait.sh

RUN chmod +x wait.sh

COPY ./requirements.txt requirements.txt

RUN python -m pip install -r requirements.txt

ENV LOG_LEVEL info

COPY . .

CMD /wait.sh postgres 5432 \
  && python manage.py collectstatic --noinput \
  && python manage.py migrate \