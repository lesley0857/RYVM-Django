FROM python:3.8.5-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt 

RUN pip3 install --upgrade pip --no-cache-dir

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

ENTRYPOINT [ "sh", "./entrypoint.sh" ]