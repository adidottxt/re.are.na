'''
All code pertaining to are.na blocks
'''
import random
from typing import List
from werkzeug.exceptions import Unauthorized

from arena import Arena

from .config import ACCESS_TOKEN
from .db import add_to_db_channel, add_to_db_block

CLIENT = Arena(ACCESS_TOKEN)


def get_random_blocks(number, user) -> List[str]:
    '''
    description:            get a number of random blocks from
                            a user's channels

    :param                  number: the number of blocks to return
                            user: given user's slug/username

    :return                 block_ids: a list of random block IDs
    '''
    # return [get_random_block(get_random_channel(user)) for i in range(number)]
    blocks = []
    for i in range(number):
        print('Getting info on block {} of {}...'.format(i+1, number))
        blocks.append(get_random_block(get_random_channel(user)))
    return blocks

def get_random_channel(username) -> str:
    '''
    description:            get a random channel from a list of
                            a user's channels

    :param                  username: given user's username

    :return                 channel_slug: the random channel's unique URL
    '''
    channels, _ = CLIENT.users.user(username).channels(per_page=100)
    channel_slugs = {chan.slug for chan in channels if chan.published}

    channel_slug = random.sample(channel_slugs, 1)[0]
    channel_id = CLIENT.channels.channel(channel_slug).id

    # use add_to_db_channel to add to database
    add_to_db_channel(channel_id, channel_slug)

    return channel_id


def get_block_class(block_id) -> str:
    '''
    description:            given a block_id, return the block's
                            class/type (image/text/link/media/attachment)

    :param                  block_id: the random block's unique id

    :return                 block_class: the given block's class/type
    '''
    return getattr(CLIENT.blocks.block(block_id), 'class')


def get_block_url(block_id) -> str:
    '''
    description:            given a block_id, return the block's
                            class/type (image/text/link/media/attachment)

    :param                  block_id: the random block's unique id

    :return                 block_class: the given block's class/type
    '''
    # block_data = CLIENT.blocks.block(block_id)

    # if getattr(block_data, 'class') == 'Text':
    #     return block_data.content
    # if block_data.source:
    #     return block_data.source['url']
    # if block_data.image:
    #     return block_data.image['display']['url']
    # return block_data.content
    return 'https://www.are.na/block/{}'.format(block_id)


def get_block_title(block_id) -> str:
    '''
    description:            given a block_id, return the block's title

    :param                  block_id: the random block's unique id

    :return                 block_title: the given block's title
    '''
    return CLIENT.blocks.block(block_id).title


def get_random_block(channel_id) -> int:
    '''
    description:            get a random block from a list of
                            blocks within a user's channel

    :param                  channel_slug: the channel's unique URL

    :return                 block_id: the random block's unique id
    '''
    channel = CLIENT.channels.channel(channel_id)
    channel_pages = channel.length // 100

    if channel.length % 100 != 0:
        channel_pages += 1

    block_ids = {
        block.id
        for i in range(1, channel_pages + 1)
        for block in channel.contents(page=i, per_page=100)[0]
    }

    while True:
        block_id = int(random.sample(block_ids, 1)[0])
        try:
            block = CLIENT.blocks.block(block_id)
            block_type = getattr(block, 'class')
            block_content = block.image['display']['url'] \
                if block_type in ('Image', 'Link', 'Media') \
                else block.image['display']['url'] if block_type == 'Attachment' \
                else block.content

            block_date = block.created_at[:10]
            block_date = '{}-{}'.format(block_date[5:], block_date[:4])

            block_data = {
                'created_at': block_date,
                'block_type': getattr(block, 'class'),
                'block_url': get_block_url(block_id),
                'block_content': block_content,
                'channel_title': channel.title,
                'block_title': block.title,
                'block_id': block_id,
                'channel_id': channel_id
            }
            if add_to_db_block(block_data):
                break
        except Unauthorized:
            pass
    return block_id
