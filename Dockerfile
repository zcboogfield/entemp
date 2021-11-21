# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /entemp
COPY requirements.txt /entemp/
RUN pip install -r requirements.txt
COPY . /entemp/
