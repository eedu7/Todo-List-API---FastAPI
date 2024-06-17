# Define the Database Configuration

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"

# Create a database engine with specific connection arguments
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)  # Create a session factory bound to the engine
Base = declarative_base()  # Create a base class for ORM models to inherit from


def get_db():  # Define a function to provide a database session
    """
    A database session in the context of SQLAlchemy is a temporary,
    isolated connection to the database that allows for executing operations
     and transactions in a safe and consistent manner.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
