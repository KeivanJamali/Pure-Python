from sqlalchemy import create_engine, MetaData, Table, Column, Integer, DECIMAL, CHAR, String, select, insert, func, text
from data import db_url_northwind as db_url
from tools import get_panda_data

engine = create_engine(db_url)
connection = engine.connect()
metadata = MetaData()
# item_table.drop(engine)
# print(f"Table 'items' is droped.")

try:
    item_table = Table("items", metadata)
    item_table.drop(engine, checkfirst=True)
    print("Table 'items' has been dropped if it existed.")
except:
    pass
product_table = Table("products", metadata, autoload_with=engine)
item_table = Table("items", metadata,
                   Column("item_id", Integer, primary_key=True),
                   Column("item_code", CHAR(5), nullable=True),
                   Column("item_name", String(40), nullable=False, server_default=text("''")),
                   Column("quantity", Integer, nullable=False, server_default=text("0")),
                   Column("price", DECIMAL(9, 2), nullable=False, server_default=text("0.00")),
                   extend_existing=True)
item_table.create(engine)
print("Table 'items' has been created.")

data = select(product_table.c.product_id,
    (func.concat(product_table.c.supplier_id, product_table.c.category_id, product_table.c.discontinued)),
    (product_table.c.product_name),
    (product_table.c.units_in_stock),
    (product_table.c.unit_price))

insert_quary1 = insert(item_table).from_select(
    ["item_id", "item_code", "item_name", "quantity", "price"],
    data
)
quary1 = select(item_table)
##############################################################################################################################################################
connection.execute(insert_quary1)
result1 = connection.execute(quary1)
print(get_panda_data(result1))