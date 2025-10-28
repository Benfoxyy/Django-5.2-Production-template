FROM python:3.13-slim-bookworm

LABEL maintainer="benxfoxy@gmail.com"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./core/requirements.txt /app

RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

COPY ./core /app