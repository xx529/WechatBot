import os
import pandas as pd
import psycopg2


print('PG_HOST', os.environ.get('PG_HOST'))
print('PG_PORT', os.environ.get('PG_PORT'))
print('PG_DB', os.environ.get('PG_DB'))
print('PG_USER', os.environ.get('PG_USER'))
print('PG_PASSWORD', os.environ.get('PG_PASSWORD'))

conn = psycopg2.connect(
    dbname=os.environ.get('PG_DB'),
    user=os.environ.get('PG_USER'),
    password=os.environ.get('PG_PASSWORD'),
    host=os.environ.get('PG_HOST'),
    port=os.environ.get('PG_PORT')
)

df = pd.read_sql('select * from test', conn)
print(df)
