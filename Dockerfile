FROM python:3.6.5-alpine

WORKDIR app
COPY . app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

VOLUME /app

CMD ["flask", "run", "-h", "0.0.0.0"]


