FROM python:3.11.9-bookworm

WORKDIR /code

COPY requirements/ /code/requirements/

RUN pip install --upgrade pip
RUN pip install -r requirements/local.txt

EXPOSE 8000