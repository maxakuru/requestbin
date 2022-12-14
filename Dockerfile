FROM python:3.9-alpine

RUN apk add --update \
      bash \
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
  && mkdir /var/log/gunicorn \
  && chmod -R 777 /var/log/supervisor \
  && chmod -R 777 /var/log/gunicorn \
  && touch /var/log/supervisor/supervisor.log \
  && touch /var/log/gunicorn/access.log \
  && touch /var/log/gunicorn/error.log

COPY run.sh ./run.sh
RUN chmod +x ./run.sh

ENTRYPOINT ["./run.sh"]