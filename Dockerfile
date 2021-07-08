FROM python:3.8.10
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ENV DJANGO_SETTINGS_MODULE=memo_reminder.settings
RUN mkdir /code
WORKDIR /code
RUN apt-get update -yq && apt-get install -yq gdal-bin nano curl
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
CMD python manage.py migrate
CMD python manage.py runserver 0.0.0.0:8000
