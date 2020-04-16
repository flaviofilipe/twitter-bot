from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (create_engine, Column, Integer, String, DateTime)

engine = create_engine('sqlite:///../twitter.db', echo=False)
Base = declarative_base()


class Answered(Base):
    __tablename__ = 'answered'
    id = Column(Integer, primary_key=True)
    id_tweet = Column(String(255))
    created_at = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f'Aswered {self.id_tweet}'


Base.metadata.create_all(engine)
