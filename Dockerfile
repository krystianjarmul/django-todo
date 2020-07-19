FROM python:3.8

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip -r requirements.txt

COPY ./mysite /app

EXPOSE 8000

CMD python3 manage.py runserver 0.0.0.0:8000

#docker build -t todo:dev .
#docker run --rm -p "8001:8000" -t todo:dev