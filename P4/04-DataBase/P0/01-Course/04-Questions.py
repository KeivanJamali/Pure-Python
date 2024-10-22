from sqlalchemy import create_engine, MetaData, Table, Numeric, desc, func, select
from data import db_url_northwind as db_url
from tools import get_panda_data

engine = create_engine(db_url)
connection = engine.connect()
metadata = MetaData()

order_detail_table = Table("order_details", metadata, autoload_with=engine)
product_table = Table("products", metadata, autoload_with=engine)
order_table = Table("orders", metadata, autoload_with=engine)
##############################################################################################################################################################
quary1 = select(order_detail_table.c.order_id,
                func.round(func.cast(func.sum(order_detail_table.c.unit_price * order_detail_table.c.quantity).label("Total"), Numeric), 2).label("Total values"),
                ).group_by(order_detail_table.c.order_id
                ).order_by(desc(func.sum(order_detail_table.c.unit_price * order_detail_table.c.quantity))
                ).limit(5)
##############################################################################################################################################################
quary2 = select(func.count(product_table.c.product_id).label("Total number of products")
                ).where(product_table.c.discontinued == 0)
##############################################################################################################################################################
quary3 = select(func.count(product_table.c.product_id).label("Not available")
                ).where(product_table.c.discontinued == 1)
##############################################################################################################################################################
step_1 = select(func.count(product_table.c.product_id)
                   ).group_by(product_table.c.supplier_id)
data4 = get_panda_data(connection.execute(step_1))
min_value = min(data4.iloc[:, 0])
quary4 = select(product_table.c.supplier_id, func.count(product_table.c.product_id).label("Number of products")
                ).group_by(product_table.c.supplier_id
                ).having(func.count(product_table.c.product_id) == min_value)
##############################################################################################################################################################
quary5 = select(order_table.c.employee_id,
                func.count(order_table.c.order_id)
                ).group_by(order_table.c.employee_id
                ).having(func.count(order_table.c.order_id) > 100)
##############################################################################################################################################################
##############################################################################################################################################################
result1 = connection.execute(quary1)
result2 = connection.execute(quary2)
result3 = connection.execute(quary3)
result4 = connection.execute(quary4)
result5 = connection.execute(quary5)
print(get_panda_data(result1))
print(get_panda_data(result2))
print(get_panda_data(result3))
print(get_panda_data(result4))
print(get_panda_data(result5))