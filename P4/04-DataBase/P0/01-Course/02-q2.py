from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.sql import select
from sqlalchemy.sql.functions import func
from data import db_url_northwind as db_url

import pandas as pd

engine = create_engine(db_url)
connection = engine.connect()
metadata = MetaData()

product_table = Table("products", metadata, autoload_with=engine)

quary = select(product_table.c.product_name,
               product_table.c.unit_price,
               product_table.c.units_in_stock,
               (product_table.c.unit_price * product_table.c.units_in_stock).label("Total Value")).where(product_table.c.unit_price * product_table.c.units_in_stock >= 1000)

result = connection.execute(quary)

data = pd.DataFrame(result.fetchall(), columns=result.keys())
print(data)
