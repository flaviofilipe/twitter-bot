from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Table, create_engine, MetaData, Column, Integer, String, DateTime)

engine = create_engine('sqlite:///../twitter.db', echo=False)
# metadata = MetaData(bind=engine)

Base = declarative_base()

class Aswered(Base):
    __tablename__ = 'answered'
    id = Column(Integer, primary_key=True)
    id_tweet = Column(String(255))
    created_at = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f'Aswered {self.id_tweet}'

# Aswered = Table(
#     'answered', 
#     metadata,
#     Column('id', Integer, primary_key=True ),
#     Column('id_tweet', String(255), index=True ),
#     Column('created_at', DateTime, default=datetime.now)
#     )

# # metadata.create_all()
Base.metadata.create_all(engine)
