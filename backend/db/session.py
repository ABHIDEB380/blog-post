from core.config import settings
from typing import Generator
from sqlalchemy import create_engine

# Now with create_engine we can interact with the
# connection but to execure SQL in
# ORM we need session maker which can
# execute ORM as well as keep a connection object
from sqlalchemy.orm import sessionmaker

engine = create_engine(settings.POSTGRES_DB_URL)

SESSIONLOCAL = sessionmaker(bind=engine)

# This is equivalent to a db connection
def get_db() -> Generator:
    try:
        db = SESSIONLOCAL()
        yield db
    except Exception as e:
        print(f"Error inside generator: {e}")
        raise
    finally:
        db.close()
