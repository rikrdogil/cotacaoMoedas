FROM nginx:latest

#RUN rm /etc/nginx/sites-enabled/default
#RUN rm /etc/nginx/conf.d/default.conf
#RUN rm /etc/nginx/conf.d/default.conf

COPY prod.conf /temp/prod.conf

RUN envsubst /app < /temp/prod.conf > /etc/nginx/conf.d/default.conf


COPY sites-enabled/ /etc/nginx/sites-enabled
