FROM alpine:latest

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5210:8080

CMD ["python", "HBnB_App.py"]