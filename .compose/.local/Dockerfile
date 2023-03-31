FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1

RUN addgroup -S dds \
  && adduser -S -G dds dds

COPY ./requirements /requirements

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r /requirements/local.txt \
  && rm -rf /requirements

USER dds

WORKDIR /app

USER dds
