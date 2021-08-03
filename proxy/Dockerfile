FROM nginxinc/nginx-unprivileged:1-alpine

COPY ./default.conf /etc/proxy/conf.d/default.conf
COPY ./uwsgi_params /etc/proxy/uwsgi_params

USER root

RUN mkdir -p /vol/static
RUN chmod 755 /vol/static

USER nginx