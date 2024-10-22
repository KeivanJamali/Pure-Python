from sqlalchemy import create_engine, MetaData, Table, Integer
from sqlalchemy.sql import select
from data import db_url_northwind as db_url
from tools import get_panda_data
from sqlalchemy.sql.functions import func

engine = create_engine(db_url)
connection = engine.connect()
metadata = MetaData()

employees_table = Table("employees", metadata, autoload_with=engine)

quary = select(employees_table.c.employee_id,
               func.concat(employees_table.c.first_name, " ", employees_table.c.last_name).label("employee"),
               employees_table.c.hire_date
               # ).where(func.cast(func.date_part("year", employees_table.c.hire_date), Integer)==1993)
               ).where(func.extract("year", employees_table.c.hire_date)==1993)

result = connection.execute(quary)
print(get_panda_data(result))