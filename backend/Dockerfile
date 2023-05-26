FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install psycopg2

COPY . .

CMD [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0" ]