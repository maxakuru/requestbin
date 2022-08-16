FROM python:3.9-alpine

RUN apk add --update \
      musl-dev \
      bsd-compat-headers \
      libevent-dev \
      && rm -rf /var/cache/apk/* \
      && pip install supervisor honcho

ADD ./code /app
ADD supervisord.conf /etc/supervisord.conf

WORKDIR /app

RUN  pip install --quiet --disable-pip-version-check -r requirements.txt \
  && mkdir /var/log/supervisor \
  && chmod -R 777 /var/log/supervisor \
  && touch /var/log/supervisor/supervisor.log \
  && touch /var/log/supervisor/requestbin.log

EXPOSE 5000

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
