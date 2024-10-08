FROM python:3.12-alpine3.17

WORKDIR  /app

# RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev

COPY requirements.txt requirements.txt
RUN pip --no-cache-dir install -r requirements.txt

COPY . /app

CMD ["python", "src/app.py"]



