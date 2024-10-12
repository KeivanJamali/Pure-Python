from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.sql import select
from sqlalchemy.sql.functions import func
from data import db_url_northwind as db_url

import pandas as pd

engine = create_engine(db_url)
connection = engine.connect()
metadata = MetaData()

employees_table = Table("employees", metadata, autoload_with=engine)

quary = select((employees_table.c.first_name + " " + employees_table.c.last_name).label("Name"),
               (func.extract("year", employees_table.c.hire_date)).label("Hire Year"),
               (func.to_char(employees_table.c.birth_date, "month")).label("Birth month"))

result = connection.execute(quary)
data = pd.DataFrame(result.fetchall(), columns=result.keys())
print(data)