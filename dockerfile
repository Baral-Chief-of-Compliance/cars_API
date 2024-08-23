FROM python:3.10-alpine

RUN mkdir -p /usr/app

WORKDIR /usr/app

COPY ./src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "3000", "--reload"]

EXPOSE 3000
