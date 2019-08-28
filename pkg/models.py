'''
Defining database models for sqlite3 tables
'''

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

ENGINE = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
DB_SESSION = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=ENGINE))

Base = declarative_base()
Base.query = DB_SESSION.query_property()  # needed for querying


class Channel(Base):  # pylint:disable=too-few-public-methods
    '''
    creating the channels table
    '''
    __tablename__ = 'channel'
    channel_id = Column(Integer, primary_key=True)
    slug = Column(String)


class Block(Base):  # pylint:disable=too-few-public-methods
    '''
    creating the blocks table
    '''
    __tablename__ = 'block'
    block_id = Column(Integer, primary_key=True)
    type = Column(String)
    channel_id = Column(Integer, ForeignKey('channel.channel_id'))
    channel = relationship(
        Channel,
        backref=backref('blocks',
                        uselist=True,
                        cascade='delete,all'))
