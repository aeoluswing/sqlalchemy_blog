# coding: utf-8
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root@localhost:3306/blog')
print(engine)