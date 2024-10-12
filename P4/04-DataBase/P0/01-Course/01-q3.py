from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.sql import select
from data import db_url_northwind as db_url

import pandas as pd

engine = create_engine(db_url)
connection = engine.connect()
metadata = MetaData()

products_table = Table("products", metadata, autoload_with=engine)

quary = select(products_table.c.product_name,
               products_table.c.unit_price,
               products_table.c.units_in_stock,
               (products_table.c.unit_price * products_table.c.units_in_stock).label("Total Value"))

result = connection.execute(quary)
data = pd.DataFrame(result.fetchall(), columns=result.keys())
print(data)