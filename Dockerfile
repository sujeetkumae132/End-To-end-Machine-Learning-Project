FROM python:3.8-slim-buster

RUN apt update -y && \
    apt install awscli -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
    
WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["pythom3","app.py"]
