from flask import Flask, request
import logging
import os
import json
import psycopg2

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)


@app.route('/message', methods=['POST'])
def message():
    data = json.loads(request.json)
    logging.info(f"{data['wechat_id']} - {data['wechat_name']} - {data['room_id']} - {data['timestamp']} - {data['message'][:15]}...")

    with psycopg2.connect(dbname=os.environ.get('PG_DB'),
                          user=os.environ.get('PG_USER'),
                          password=os.environ.get('PG_PASSWORD'),
                          host=os.environ.get('PG_HOST'),
                          port=os.environ.get('PG_PORT')
                         ) as conn:

        sql = f"""insert into message 
                 (wechat_id, wechat_name, room_id, timestamp, message)
                 values ('{data['wechat_id']}', '{data['wechat_name']}', '{data['room_id']}', {data['timestamp']}, '{data['message']}')
               """
        conn.cursor().execute(sql)

    return {'state': 'ok'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
