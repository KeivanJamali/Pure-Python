from sqlalchemy import create_engine, MetaData, Table, func, select, Numeric
from data import db_url_northwind as db_url
from tools import get_panda_data

engine = create_engine(db_url)
connection = engine.connect()
metadata = MetaData()

product_table = Table("products", metadata, autoload_with=engine)
order_table = Table("orders", metadata, autoload_with=engine)
order_detail_table = Table("order_details", metadata, autoload_with=engine)
customer_table = Table("customers", metadata, autoload_with=engine)
supplier_table = Table("suppliers", metadata, autoload_with=engine)
employee_table = Table("employees", metadata, autoload_with=engine)
##############################################################################################################################################################
joined_table = order_table.join(order_detail_table, order_table.c.order_id==order_detail_table.c.order_id)
quary1 = select(order_table.c.order_id, 
                func.round(func.cast(order_detail_table.c.unit_price*order_detail_table.c.quantity, Numeric), 2).label("Total Value")
                ).select_from(joined_table
                ).where(order_table.c.ship_country=="France"
                ).order_by((order_detail_table.c.unit_price*order_detail_table.c.quantity).desc())


joined_table = supplier_table.join(product_table, supplier_table.c.supplier_id==product_table.c.supplier_id)
quary2 = select(supplier_table.c.company_name,
                product_table.c.product_name
                ).select_from(joined_table
                ).where(supplier_table.c.country=="Japan")

joined_table = employee_table.join(order_table, employee_table.c.employee_id==order_table.c.employee_id)
subquary = select(order_table.c.order_id,
                  employee_table.c.employee_id,
                  employee_table.c.last_name,
                  employee_table.c.first_name,
                  ).select_from(joined_table).subquery()
joined_table = order_detail_table.join(subquary, subquary.c.order_id==order_detail_table.c.order_id)
quary3 = select(subquary.c.last_name,
                subquary.c.first_name,
                func.sum(func.round(func.cast(order_detail_table.c.unit_price*order_detail_table.c.quantity, Numeric), 2))
                ).select_from(joined_table
                ).group_by(subquary.c.last_name, subquary.c.first_name
                ).having(func.sum(order_detail_table.c.unit_price*order_detail_table.c.quantity) < 100_000)

joined_table = employee_table.join(order_table, employee_table.c.employee_id==order_table.c.employee_id).join(order_detail_table, order_detail_table.c.order_id==order_table.c.order_id)
quary4 = select(employee_table.c.last_name,
                employee_table.c.first_name,
                func.sum(func.round(func.cast(order_detail_table.c.unit_price*order_detail_table.c.quantity, Numeric), 2))
                ).select_from(joined_table
                ).group_by(employee_table.c.last_name, employee_table.c.first_name
                ).order_by(func.sum(order_detail_table.c.unit_price*order_detail_table.c.quantity).desc()
                ).limit(5)
##############################################################################################################################################################
result1 = connection.execute(quary1)
result2 = connection.execute(quary2)
result3 = connection.execute(quary3)
result4 = connection.execute(quary4)
print(get_panda_data(result1))
print(get_panda_data(result2))
print(get_panda_data(result3))
print(get_panda_data(result4))