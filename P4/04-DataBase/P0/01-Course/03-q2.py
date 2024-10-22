from sqlalchemy import create_engine, Integer
from datetime import date
from sqlalchemy.sql import select
from data import db_url_northwind as db_url
from tools import get_panda_data
from sqlalchemy.sql.functions import func

engine = create_engine(db_url)
connection = engine.connect()

quary = select(func.cast(func.date_part("year",func.age(func.current_date(), date(2001, 12, 26))), Integer).label("My Age"))

result = connection.execute(quary)
print(get_panda_data(result))