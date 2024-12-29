FROM python:3.13-alpine

EXPOSE 8000


WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN apk add --no-cache gcc musl-dev libffi-dev postgresql-dev

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


RUN python -m compileall .

WORKDIR /usr/src/app/app


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]