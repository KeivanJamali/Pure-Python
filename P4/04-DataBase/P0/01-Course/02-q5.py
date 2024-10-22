from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.sql import select
from tools import get_panda_data
from data import db_url_northwind as db_url

engine = create_engine(db_url)
connection = engine.connect()
metadata = MetaData()

order_table = Table("orders", metadata, autoload_with=engine)

quary = select(order_table.c.order_id,
               order_table.c.customer_id,
               order_table.c.shipped_date
               ).where((order_table.c.ship_country == "Canada") &
                       (order_table.c.shipped_date.between("1996-12-01", "1997-01-31")))

result = connection.execute(quary)
print(get_panda_data(result))