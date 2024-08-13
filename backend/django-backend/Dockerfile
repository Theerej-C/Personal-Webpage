# syntax=docker/dockerfile:1
FROM python:3

# Set environment variable
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /code

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy application code
COPY . .