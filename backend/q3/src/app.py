from flask import Flask
from flask import request
import requests
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from flask_pydantic import validate
import psycopg2
from flask import jsonify


app = Flask("API")
conn = psycopg2.connect(host="postgres", database="test_database",
                        user="test_user", password="test_password")


cur = conn.cursor()
cur.execute("""
CREATE TABLE if not exists events (
    id SERIAL,
	event_time timestamp,
    url text,
    status text
)
""")
cur.close()
conn.commit()


class RequestUrlBodyModel(BaseModel):
    url: str


class RequestListUrlBodyModel(BaseModel):
    after_time: datetime


@app.route('/', methods=['GET'])
def home():
    return {"hello": "world"}


@app.route('/url', methods=['POST'])
@validate()
def request_url(body: RequestListUrlBodyModel):
    after_time = body.after_time

    cur = conn.cursor()
    cur.execute("""
    SELECT 
        id,
        event_time,
        url,
        status
    FROM events
    WHERE event_time > %s
    ORDER BY event_time
    """, (after_time,))
    rows = cur.fetchall()
    cur.close()
    conn.commit()

    response = []
    for row in rows:
        response.append({
            'event_time': row[1],
            'url': row[2],
            'status': row[3],
        })

    return jsonify(response)


@app.route('/', methods=['POST'])
@validate()
def list_urls(body: RequestUrlBodyModel):
    url = body.url

    status = 'online'
    try:
        r = requests.get(url)
    except requests.exceptions.RequestException as e:
        status = 'offline'

    event = {
        'event_time': datetime.now(),
        'url': url,
        'status': status,
    }
    print(event)

    cur = conn.cursor()
    cur.execute(
        "INSERT INTO events (event_time, url, status) VALUES (%(event_time)s, %(url)s, %(status)s)", event)
    cur.close()
    conn.commit()

    return event


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
