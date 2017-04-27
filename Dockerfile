FROM python:3-alpine

RUN apk update
RUN apk add libxml2-dev libxslt-dev libffi-dev openssl-dev libcurl
RUN pip install grab




