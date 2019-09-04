'''
Defining database models for sqlite3 tables
'''

from typing import Any

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

Base = declarative_base()  # type: Any
Base.query = DB_SESSION.query_property()  # needed for querying
Base.metadata.drop_all(bind=ENGINE)
Base.metadata.create_all(bind=ENGINE)


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
    block_id = Column(Integer)
    channel_id = Column(Integer, ForeignKey('channel.channel_id'))
    channel_title = Column(String)
    block_title = Column(String)
    block_type = Column(String)
    block_content = Column(String)
    block_url = Column(String)
    block_create_date = Column(String)
    request_id = Column(Integer, primary_key=True, autoincrement=True)
    channel = relationship(
        Channel,
        backref=backref('blocks',
                        uselist=True,
                        cascade='delete,all'))
