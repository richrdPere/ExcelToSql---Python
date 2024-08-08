from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import sessionmaker
from config import DB_CONFIG

DATABASE_URI = (
    f"mssql+pyodbc://{DB_CONFIG['username']}:{DB_CONFIG['password']}@"
    f"{DB_CONFIG['server']}/{DB_CONFIG['database']}?driver={DB_CONFIG['driver']}"
)

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

metadata = MetaData()

# Ejemplo de tabla
example_table = Table('example', metadata,
                      Column('id', Integer, primary_key=True),
                      Column('data', String))

metadata.create_all(engine)

def insert_data(table, data):
    ins = table.insert().values(data)
    conn = engine.connect()
    conn.execute(ins)
    conn.close()
