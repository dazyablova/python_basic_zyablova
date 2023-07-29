#  docker run -it -p 8000:8000 fastapi_app

FROM python:3.9-buster

ENV PYTHONBUFFERED=1

WORKDIR /fast_api_app

COPY fast_api_app/requirements.txt ./

RUN pip install -r requirements.txt

COPY fast_api_app .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host=0.0.0.0" ,"--port=8000"]