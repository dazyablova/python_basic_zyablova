# docker run -p 8000:8000 myapp

FROM python:3.9-buster

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./app /app

RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
