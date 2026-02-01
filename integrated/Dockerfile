#install linux box with python version 3.10
FROM python:3.10-slim

#folder inside the container called app, where the app will be installed
WORKDIR /app

#copy local requirements.txt to /app inside container
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt 

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
