#base
FROM python:3.10.4-slim-bullseye

#variables de entorno
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#directorio de trabajo
WORKDIR /code

#dependencias
COPY ./requirements.txt .
RUN pip install -r requirements.txt

#copiar proyecto
COPY . .