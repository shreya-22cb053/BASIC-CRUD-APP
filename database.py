from models import Base
from sqlalchemy import create_engine

DATABASE_URL = 'mysql+mysqlconnector://root:root@localhost/flask_db'
engine = create_engine(DATABASE_URL)

# Create all tables
Base.metadata.create_all(engine)
