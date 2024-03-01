
FROM python:3.9

WORKDIR /hawsr

COPY requirements.txt /hawsr/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /hawsr/

RUN python manage.py makemigrations
RUN python manage.py migrate
EXPOSE 8000


CMD ["python", "manage.py", "runserver", "8000"]
