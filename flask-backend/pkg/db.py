'''
database specific functions
'''
# pylint: disable=no-member
from sqlalchemy.exc import DatabaseError

from .models import DB_SESSION, ENGINE, Base, Channel, Block
from .schema import SCHEMA
from .constants import CHANNEL_CHECK, BLOCK_CHECK, REQUEST_COUNT


def add_test_data() -> None:
    '''
    add test data
    '''
    Base.metadata.drop_all(bind=ENGINE)
    Base.metadata.create_all(bind=ENGINE)
    test_chan = Channel(channel_id=0, slug='test_channel')
    DB_SESSION.add(test_chan)
    test_block = Block(
        block_id=0,
        channel_id=0,
        request_number=0,
        block_type='test',
        block_url='test',
        block_content='test',
        channel_title='test',
        block_title='test',
        block_create_date='test',
    )
    DB_SESSION.add(test_block)
    DB_SESSION.commit()


def check_unique_channel_id(channel_id) -> bool:
    '''
    description:            check if a channel_id has been stored in
                            the database

    :param                  channel_id: the given channel's unique id

    :return                 True if channel is unique, False otherwise
    '''
    result = str(SCHEMA.execute(CHANNEL_CHECK).data)
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
    result = str(SCHEMA.execute(BLOCK_CHECK).data)
    if "('blockId', '{}')".format(block_id) not in result:
        return True
    return False


def return_request_count() -> int:
    global REQUEST_COUNT
    REQUEST_COUNT += 1
    return REQUEST_COUNT

def clear_database() -> None:
    '''
    description:            clear any data stored in the database
    '''
    DB_SESSION.remove()


def add_to_db_channel(channel_id, slug) -> bool:
    '''
    description:            add channel information to our database

    :param                  channel_id: the given channel's unique id
                            slug: the given channel's slug

    :return                 True if added successfully, False otherwise
    '''
    try:
        if check_unique_channel_id(channel_id):
            Base.metadata.create_all(bind=ENGINE)
            channel = Channel(channel_id=channel_id, slug=slug)
            DB_SESSION.add(channel)  # pylint:disable=no-member
            DB_SESSION.commit()  # pylint:disable=no-member
        return True
    except DatabaseError:
        return False


def add_to_db_block(block_data) -> bool:
    '''
    description:            add block information to our database

    :param                  block_id: the given block's unique id
                            channel_id: the channel id for the given block
                            type: the block's type/class

    :return                 True if added successfully, False otherwise
    '''
    try:
        block_id = block_data['block_id']
        if check_unique_block_id(block_id):
            Base.metadata.create_all(bind=ENGINE)
            block = Block(
                block_create_date=block_data['created_at'],
                block_title=block_data['block_title'],
                channel_title=block_data['channel_title'],
                block_id=block_id,
                channel_id=block_data['channel_id'],
                block_type=block_data['block_type'],
                block_url=block_data['block_url'],
                block_content=block_data['block_content'],
                request_number=return_request_count(),
            )
            DB_SESSION.add(block)  # pylint: disable=no-member
            DB_SESSION.commit()  # pylint: disable=no-member
            return True
        print("Error: Block ID has already been added to database")
        return False
    except DatabaseError:
        return False
