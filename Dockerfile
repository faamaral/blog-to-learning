FROM python:3.9-slim

RUN useradd microblog

WORKDIR /home/microblog

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY blog blog
COPY migrations migrations
COPY boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP ./blog/app.py

RUN chown -R microblog:microblog ./
USER microblog

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]

# FROM python:3.10-slim-buster

# # Set the working directory to /app
# WORKDIR /var/www/app

# # Copy the entire project directory to the container
# COPY . .

# # Install Poetry and project dependencies
# RUN pip install poetry
# RUN poetry config virtualenvs.create false
# RUN poetry install --no-dev

# # Start the server
# CMD ["poetry", "run", "start"]