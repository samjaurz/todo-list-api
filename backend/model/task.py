from sqlalchemy.orm import DeclarativeBase, Mapped , mapped_column
from sqlalchemy import  String
from sqlalchemy import create_engine

engine = create_engine('sqlite:///tasks.db', echo=True)

class Base(DeclarativeBase):
    pass

class Task(Base):
    __tablename__ = "task"
    id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(String)

    def __repr__(self) -> str:
        return f"<Task id={self.id} name={self.name}>"

Base.metadata.create_all(engine)