# Pull base image
FROM python:3.7-slim

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock /app/
RUN pipenv install --system --deploy

# Copy project
COPY . /app/