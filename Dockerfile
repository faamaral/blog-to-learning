FROM python:3.9

WORKDIR /usr/app/src

COPY requirements-dev.txt .

RUN pip install -r requirements-dev.txt
