FROM python:3.9  
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

# docker-compose run web python manage.py startapp mainapp
# docker-compose run web pip freeze > requirements.txt