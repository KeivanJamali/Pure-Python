from sqlalchemy import create_engine, MetaData, Table, func, select
from data import db_url_northwind as db_url
from tools import get_panda_data

engine = create_engine(db_url)
connection = engine.connect()
metadata = MetaData()

product_table = Table("products", metadata, autoload_with=engine)
order_table = Table("orders", metadata, autoload_with=engine)
customer_table = Table("customers", metadata, autoload_with=engine)
##############################################################################################################################################################
quary1 = select(product_table.c.product_id,
                product_table.c.product_name,
                product_table.c.unit_price
                ).where(product_table.c.unit_price==select(func.min(product_table.c.unit_price)).scalar_subquery())


quary1 = select(
    product_table.c.product_id,
    product_table.c.product_name,
    product_table.c.unit_price,
    (select(func.min(product_table.c.unit_price))).label('min_price')
).where(product_table.c.unit_price == (select(func.min(product_table.c.unit_price)).scalar_subquery()))


min_price_subquery = select(
    product_table.c.product_id,
    product_table.c.product_name,
    product_table.c.unit_price
).where(product_table.c.unit_price == (select(func.min(product_table.c.unit_price)).scalar_subquery())).subquery()

quary1 = select(min_price_subquery)
##############################################################################################################################################################
quary2 = select(func.count(order_table.c.order_id)
                ).where(~order_table.c.customer_id.in_(select(customer_table.c.customer_id).scalar_subquery()))
##############################################################################################################################################################
result1 = connection.execute(quary1)
result2 = connection.execute(quary2)
print(get_panda_data(result1))
print(get_panda_data(result2))