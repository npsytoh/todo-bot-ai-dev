FROM python:3.11.9-bookworm

RUN mkdir /code
WORKDIR /code

COPY requirements/ /code/requirements/

RUN pip install --upgrade pip
RUN pip install -r requirements/local.txt

COPY . /code/

EXPOSE 8000