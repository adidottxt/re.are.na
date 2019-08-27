'''
All code pertaining to are.na blocks
'''
from arena import Arena

from .config import ACCESS_TOKEN

def get_random_channel() -> str:
    '''
    description:            get a random channel from a list of
                            a user's channels

    :param                  N/A

    :return                 channel_id: the random channel's unique id
    '''
    pass

def get_random_block(channel_id) -> str:
    '''
    description:            get a random block from a list of
                            blocks within a user's channel

    :param                  channel_id: the channel's unique id

    :return                 block_id: the random block's unique id
    '''
    pass

def get_block_class(block_id) -> str:
    '''
    description:            given a block_id, return the block's
                            class/type (image/text/link/media/attachment)

    :param                  block_id: the random block's unique id

    :return                 block_class: the given block's class/type
    '''
    pass

def get_block_data(block_id, block_class):
    '''
    description:            given a block_id and class/type, return the block's
                            data (output could vary depending on block class)

    :param                  block_id: the given block's unique id
                            block_class: the given block's class/type

    :return                 block_data: the given block's data
    '''
    pass

def check_block_unique(block_id) -> bool:
    '''
    description:            given a block_id, check if the block has been
                            displayed to the user before

    :param                  block_id: the given block's unique id

    :return                 True/False
    '''
    pass

