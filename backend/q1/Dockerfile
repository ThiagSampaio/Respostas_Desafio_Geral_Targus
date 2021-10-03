FROM python:3.9-slim

WORKDIR /app

COPY docker-build.bash .
RUN bash docker-build.bash -t analise:04 .

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY app/ .

EXPOSE 8000


CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--reload"]

