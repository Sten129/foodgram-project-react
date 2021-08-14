FROM python:3.8.5

WORKDIR /code
COPY . .
RUN pip install -r requirements.txt
CMD gunicorn --bind 0.0.0.0:8000  --chdir foodgram foodgram.wsgi