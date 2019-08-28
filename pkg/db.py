'''
database specific functions
'''
from .models import db_session
from .schema import schema
from .constants import CHANNEL_CHECK, BLOCK_CHECK


def check_unique_channel_id(channel_id):
    '''
    description:            check if a channel_id has been stored in
                            the database

    :param                  channel_id: the given channel's unique id

    :return                 True/False
    '''
    result = str(schema.execute(CHANNEL_CHECK).data)
    if "('channelId', '{}')".format(channel_id) not in result:
        return True
    return False

def check_unique_block_id(block_id):
    '''
    description:            check if a block_id has been stored in
                            the database

    :param                  block_id: the given block's unique id

    :return                 True/False
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
