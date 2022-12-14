FROM python:3.10

COPY DjangoPr/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . app
WORKDIR /app
ADD .env /env_file/.env

RUN python manage.py migrate
RUN python manage.py collecstatic
