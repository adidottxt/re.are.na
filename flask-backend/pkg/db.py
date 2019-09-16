'''
db.py contains code that pertains to sqlite3/database-specific functions
'''
# pylint: disable=no-member
from typing import Dict

from sqlalchemy.exc import DatabaseError

from .models import (
    DB_SESSION,
    ENGINE,
    Base,
    Channel,
    Block
)

from .constants import (
    CHANNEL_CHECK,
    BLOCK_CHECK,
    BLOCK,
    CHANNEL
)

from .schema import SCHEMA


def add_test_data() -> bool:
    '''
    description:            this function adds test data to the
                            sqlite3 database used by this application

    return:                 None
    '''
    try:
        # reset database
        Base.metadata.drop_all(bind=ENGINE)
        Base.metadata.create_all(bind=ENGINE)

        # create test channel to be added to the database
        test_chan = Channel(channel_id=0)

        # add test channel to the current session
        DB_SESSION.add(test_chan)

        # create a test block to be added to the database
        test_block = Block(
            block_id=0,
            channel_id=0,
            block_type='test',
            block_url='test',
            block_content='test',
            channel_title='test',
            block_title='test',
            block_create_date='test',
        )

        # add test block to the current session
        DB_SESSION.add(test_block)

        # commit test block + channel to database
        DB_SESSION.commit()
        return True

    except DatabaseError:
        return False


def check_unique_data(data_id: int, data_type: str) -> bool:
    '''
    description:            check if a data_id has been stored in
                            the database

    param:                  data_id: the given block/channel's unique id

    return:                 True if block/channel is unique, False otherwise
    '''
    if data_type is CHANNEL:
        # get channel data present in database with CHANNEL_CHECK graphql query
        result = str(SCHEMA.execute(CHANNEL_CHECK).data)

        # check if given channel id is present in result
        if "('channelId', '{}')".format(data_id) not in result:
            return True
        return False

    if data_type is BLOCK:
        # get block data present in database with BLOCK_CHECK graphql query
        result = str(SCHEMA.execute(BLOCK_CHECK).data)

        # check if given block is present in result
        if "('blockId', {})".format(data_id) not in result:
            return True
        return False

    # return False if data_type is neither a block or a channel
    return False


def clear_database() -> bool:
    '''
    description:            clear any data stored in the database

    return:                 None
    '''
    try:
        DB_SESSION.remove()
        return True

    except DatabaseError:
        return False


def add_channel_to_db(channel_id: int) -> bool:
    '''
    description:            add channel information to our database

    param:                  channel_id: the given channel's unique id

    return:                 True if added successfully, False otherwise
    '''
    try:

        # create new channel using channel id
        channel = Channel(channel_id=channel_id)

        # connect, add, and commit to database
        Base.metadata.create_all(bind=ENGINE)
        DB_SESSION.add(channel)  # pylint:disable=no-member
        DB_SESSION.commit()  # pylint:disable=no-member

        return True

    except DatabaseError:
        return False


def add_block_to_db(block_data: Dict) -> bool:
    '''
    description:            add block information to our database

    param:                  block_id: the given block's unique id
                            channel_id: the channel id for the given block
                            type: the block's type/class

    return:                 True if added successfully, False otherwise
    '''
    try:
        # create block using block_data
        block = Block(
            block_create_date=block_data['created_at'],
            block_title=block_data['block_title'],
            channel_title=block_data['channel_title'],
            block_id=block_data['block_id'],
            channel_id=block_data['channel_id'],
            block_type=block_data['block_type'],
            block_url=block_data['block_url'],
            block_content=block_data['block_content'],
        )

        # connect, add and commit to database
        Base.metadata.create_all(bind=ENGINE)
        DB_SESSION.add(block)  # pylint: disable=no-member
        DB_SESSION.commit()  # pylint: disable=no-member

        return True

    except DatabaseError:
        return False
