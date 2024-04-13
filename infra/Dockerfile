FROM python:3.9.13-slim

WORKDIR /app

RUN pip install --upgrade pip
ADD ./requirements.txt /app/
RUN pip install -r requirements.txt --no-cache-dir

ADD ./lesta /app/lesta
ADD ./infra /app/infra

RUN python -m nltk.downloader punkt

WORKDIR /app/lesta

# CMD ["gunicorn", "lesta.wsgi:application", "--bind", "0:8000"]
CMD ["python", "manage.py", "runserver", "0:8000"]
