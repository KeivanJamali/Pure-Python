from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.sql import select
from data import db_url_northwind as db_url
from tools import get_panda_data

engine = create_engine(db_url)
connection = engine.connect()
metadata = MetaData()

product_table = Table("products", metadata, autoload_with=engine)

quary = select(product_table.c.product_id,
               product_table.c.product_name,
               product_table.c.quantity_per_unit
               ).where(product_table.c.quantity_per_unit.like("%bottles%"))

result = connection.execute(quary)
print(get_panda_data(result))