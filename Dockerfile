FROM python:3.9-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV PORT=5000

EXPOSE $PORT

VOLUME ["app/data"]

CMD ["sh", "-c", "gunicorn --bind localhost:$PORT HBnB_App:app"]