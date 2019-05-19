# ---- Base python ----
FROM python:3.6-alpine AS base
ENV PYTHONUNBUFFERED 1
MAINTAINER Chirag Maliwal "cmaliwal@amsysis.com"

# ---- Dependencies ----
FROM base AS dependencies
RUN apk add git
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
