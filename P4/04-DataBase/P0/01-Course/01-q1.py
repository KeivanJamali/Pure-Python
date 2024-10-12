from sqlalchemy import create_engine, MetaData, Column, Table
from sqlalchemy.sql import select
from data import db_url_northwind as db_url
import pandas as pd


engine = create_engine(db_url)
connection = engine.connect()

metadata = MetaData()
product_table = Table("products", metadata, autoload_with=engine)

quary = select(product_table.c.product_id,
               product_table.c.product_name,
               product_table.c.quantity_per_unit,
               product_table.c.unit_price,
               product_table.c.units_in_stock)
data = pd.DataFrame(connection.execute(quary))

print(data)