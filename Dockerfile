FROM python:3.9.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /usr/src/company/

COPY ./Pipfile /usr/src/Pipfile
COPY ./Pipfile.lock /usr/src/Pipfile.lock

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install pipenv
RUN pipenv install --system --deploy

COPY . /usr/src/company/
WORKDIR /usr/src/company/

ENTRYPOINT ["/bin/sh", "entrypoint.sh"]
