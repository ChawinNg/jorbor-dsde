FROM python:3.10-alpine
WORKDIR /app

RUN pip install kafka-python
RUN pip install pymongo
RUN pip install python-dotenv

COPY . .

CMD ["python", "-u", "consumer.py"]