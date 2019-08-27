'''
All code pertaining to are.na blocks
'''
import random
from typing import List

from arena import Arena

from config import ACCESS_TOKEN

CLIENT = Arena(ACCESS_TOKEN)
USED_BLOCKS = {}
USED_CHANNELS = {}

def get_random_blocks(number, user) -> List[str]:
    '''
    description:            get a number of random blocks from
                            a user's channels

    :param                  number: the number of blocks to return
                            user: given user's slug/username

    :return                 block_ids: a list of random block IDs
    '''
    return [get_random_block(get_random_channel(user)) for i in range(number)]


def get_random_channel(username) -> str:
    '''
    description:            get a random channel from a list of
                            a user's channels

    :param                  username: given user's username

    :return                 channel_slug: the random channel's unique URL
    '''
    channels, _ = CLIENT.users.user(username).channels(per_page=100)
    channel_ids = {chan.slug for chan in channels if chan.published}
    return random.sample(channel_ids, 1)[0]


def get_random_block(channel_slug) -> int:
    '''
    description:            get a random block from a list of
                            blocks within a user's channel

    :param                  channel_slug: the channel's unique URL

    :return                 block_id: the random block's unique id
    '''
    channel = CLIENT.channels.channel(channel_slug)
    channel_pages = channel.length // 100

    if channel.length % 100 != 0:
        channel_pages += 1

    block_ids = {block.id \
        for i in range(1, channel_pages+1) \
        for block in channel.contents(page=i, per_page=100)[0]
    }

    return random.sample(block_ids, 1)


def get_block_class(block_id) -> str:
    '''
    description:            given a block_id, return the block's
                            class/type (image/text/link/media/attachment)

    :param                  block_id: the random block's unique id

    :return                 block_class: the given block's class/type
    '''
    return(getattr(CLIENT.blocks.block(block_id), 'class'))


def get_block_data(block_id):
    '''
    description:            given a block_id and class/type, return the block's
                            data (output could vary depending on block class)

    :param                  block_id: the given block's unique id

    :return                 block_data: the given block's data
    '''
    # get block
    # check for block type/class
    # based on block type/class, return data in appropriate format
    pass


def check_block_unique(block_id) -> bool:
    '''
    description:            given a block_id, check if the block has been
                            displayed to the user before

    :param                  block_id: the given block's unique id

    :return                 True/False
    '''
    # eventually swap this for database check
    return True if block_id not in USED_BLOCKS else False


def check_channel_unique(channel_id) -> bool:
    '''
    description:            given a channel_id, check if a block from
                            the given channel has been displayed to the
                            user before

    :param                  channel_id: the given channel's unique id

    :return                 True/False
    '''
    # eventually swap this for database check
    return True if channel_id not in USED_CHANNELS else False
