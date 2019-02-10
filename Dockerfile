FROM python:3.7

COPY . /app
WORKDIR /app
RUN mkdir -p /app/data
RUN mkdir -p /app/log

RUN pip install -r requirements.txt

CMD [ "python", "/app/main.py" ]