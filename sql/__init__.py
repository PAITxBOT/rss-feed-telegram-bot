import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

DATABASE_URL = os.environ.get("postgres://kqtshnww:QRG79h0i4oPLSvEOGk_CRmstNxf3PWwJ@tuffi.db.elephantsql.com/kqtshnww")

def start() -> scoped_session:
    engine = create_engine(DATABASE_URL)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


try:
    BASE = declarative_base()
    SESSION = start()
except AttributeError as e:
    # this is a dirty way for the work-around required for #23
    print("DATABASE_URL is not configured. Features depending on the database might have issues.")
    print(str(e))
