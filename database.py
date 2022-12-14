import sqlalchemy
import sqlalchemy.ext.declarative as declerative
import sqlalchemy.orm as orm

DB_URL = "sqlite:///./dbfile.db"
engine = sqlalchemy.create_engine(DB_URL, connect_args={"check_same_thread": False})

SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declerative.declarative_base()