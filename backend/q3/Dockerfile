FROM python:3.8.3-slim-buster

WORKDIR /code

ADD . /code
RUN pip3 install -r requirements.txt

#RUN apk update && apk add postgresql

CMD python3 src/app.py