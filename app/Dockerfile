FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /api
ADD ./requirements.txt /api/requirements.txt
COPY . /api

RUN pip install -r requirements.txt

CMD ["python3", "-u" , "app.py"]
