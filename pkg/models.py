from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    create_engine
)
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship,
    backref
)
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()  # needed for querying


class Channel(Base):
    __tablename__ = 'channel'
    channel_id = Column(Integer, primary_key=True)
    channel_slug = Column(String)


class Block(Base):
    __tablename__ = 'block'
    block_id = Column(Integer, primary_key=True)
    block_type = Column(String)
    channel_id = Column(Integer, ForeignKey('channel.channel_id'))
    channel = relationship(
        Channel,
        backref=backref('blocks',
                        uselist=True,
                        cascade='delete,all'))
