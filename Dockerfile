FROM python:3.10.0-slim
WORKDIR /ML
COPY . .
RUN pip install -r requirements.txt