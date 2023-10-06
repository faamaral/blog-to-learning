FROM python:3.9

WORKDIR /usr/app/src

COPY /app .

RUN pip install -r requirements-dev.txt

ENTRYPOINT python3 run.py
