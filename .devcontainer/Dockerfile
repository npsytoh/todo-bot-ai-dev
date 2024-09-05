FROM python:3.11.9-bookworm

RUN mkdir /code
RUN mkdir /code/requirements
WORKDIR /code

COPY requirements/local.txt /code/reqirements/local.txt

RUN pip install --upgrade pip
RUN pip install -r requirements/local.txt

COPY . /code/

EXPOSE 8000