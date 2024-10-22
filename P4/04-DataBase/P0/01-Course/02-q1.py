from sqlalchemy import create_engine, MetaData, Table, inspect
from sqlalchemy.sql import select
from sqlalchemy.sql.functions import func
from data import db_url_northwind as db_url

import pandas as pd

engine = create_engine(db_url)
connection = engine.connect()
# inspector = inspect(engine)
# print(inspector.get_table_names())
metadata = MetaData()
customer_table = Table("customers", metadata, autoload_with=engine)
customer_columns = customer_table.c

quary = select(customer_columns.customer_id,
               customer_columns.company_name,
               customer_columns.country).where(customer_columns.country != "USA")

result = connection.execute(quary)

data = pd.DataFrame(result.fetchall(), columns=result.keys())
print(data)

