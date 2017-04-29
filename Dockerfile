FROM python:3-alpine
MAINTAINER Alexander Istinspring "istinspring@gmail.com"

ENV PYCURL_SSL_LIBRARY="openssl"
RUN apk update
RUN apk add libxml2-dev libxslt-dev libffi-dev openssl-dev libcurl curl-dev \
    gcc libgcc musl-dev
RUN pip install grab && mkdir code

WORKDIR "/code"
