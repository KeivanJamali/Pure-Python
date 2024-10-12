from sqlalchemy import inspect, create_engine, Column, Table, MetaData
from sqlalchemy.sql import select
from sqlalchemy.sql.functions import Extract
from data import db_url_northwind as db_url
import pandas as pd

engine = create_engine(db_url)
connection = engine.connect()
metadata = MetaData()

employees_table = Table("employees", metadata, autoload_with=engine)
quary = select((employees_table.c.first_name + " " + employees_table.c.last_name).label("Name"),
               Extract("year", employees_table.c.hire_date).label("Hire Year"))

result = connection.execute(quary)

data = pd.DataFrame(result.fetchall(), columns=result.keys())

print(data)