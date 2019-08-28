'''
database specific functions
'''
from sqlalchemy.exc import DatabaseError

from .models import db_session, engine, Base, Channel, Block
from .schema import schema
from .constants import CHANNEL_CHECK, BLOCK_CHECK


def check_unique_channel_id(channel_id) -> bool:
    '''
    description:            check if a channel_id has been stored in
                            the database

    :param                  channel_id: the given channel's unique id

    :return                 True if channel is unique, False otherwise
    '''
    result = str(schema.execute(CHANNEL_CHECK).data)
    if "('channelId', '{}')".format(channel_id) not in result:
        return True
    return False

def check_unique_block_id(block_id) -> bool:
    '''
    description:            check if a block_id has been stored in
                            the database

    :param                  block_id: the given block's unique id

    :return                 True if block is unique, False otherwise
    '''
    result = str(schema.execute(BLOCK_CHECK).data)
    if "('blockId', '{}')".format(block_id) not in result:
        return True
    return False


def clear_database() -> None:
    '''
    description:            clear any data stored in the database
    '''
    db_session.remove()

def add_to_db_channel(channel_id, slug) -> bool:
    '''
    description:            add channel information to our database

    :param                  channel_id: the given channel's unique id
                            slug: the given channel's slug

    :return                 True if added successfully, False otherwise
    '''
    try:
        Base.metadata.create_all(bind=engine)
        channel = Channel(channel_id=channel_id, slug=slug)
        db_session.add(channel) # pylint:disable=no-member
        db_session.commit() # pylint:disable=no-member
        return True
    except DatabaseError:
        return False

def add_to_db_block(block_id, channel_id, block_type) -> bool:
    '''
    description:            add block information to our database

    :param                  block_id: the given block's unique id
                            channel_id: the channel id for the given block
                            type: the block's type/class

    :return                 True if added successfully, False otherwise
    '''
    try:
        Base.metadata.create_all(bind=engine)
        block = Block(block_id=block_id, channel_id=channel_id, type=block_type)
        db_session.add(block) # pylint:disable=no-member
        db_session.commit() # pylint:disable=no-member
        return True
    except DatabaseError:
        return False
