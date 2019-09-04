'''
All code pertaining to are.na blocks
'''
import random
from typing import List
from werkzeug.exceptions import Unauthorized
from requests import exceptions

from arena import Arena

from .config import ACCESS_TOKEN
from .constants import HTTP_ERROR_MESSAGE
from .db import add_to_db_channel, add_to_db_block

CLIENT = Arena(ACCESS_TOKEN)


def get_random_blocks(number, user) -> List[int]:
    '''
    description:            get a number of random blocks from
                            a user's channels

    :param                  number: the number of blocks to return
                            user: given user's slug/username

    :return                 block_ids: a list of random block IDs
    '''
    # return [get_random_block(get_random_channel(user)) \
    #         for i in range(number)]
    blocks = []
    for i in range(number):
        print('Getting info on block {} of {}...'.format(i + 1, number))
        blocks.append(get_random_block(get_random_channel(user)))
    return blocks


def get_random_channel(username) -> str:
    '''
    description:            get a random channel from a list of
                            a user's channels

    :param                  username: given user's username

    :return                 channel_slug: the random channel's unique URL
    '''
    try:
        channels, _ = CLIENT.users.user(username).channels(per_page=100)
        channel_slugs = {chan.slug for chan in channels if chan.published}

        channel_slug = random.sample(channel_slugs, 1)[0]
        channel_id = CLIENT.channels.channel(channel_slug).id

        add_to_db_channel(channel_id, channel_slug)

        return channel_id

    except exceptions.HTTPError:
        print(HTTP_ERROR_MESSAGE)
        return ''


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
                'block_url': 'https://www.are.na/block/{}'.format(block_id),
                'block_content': block_content,
                'channel_title': channel.title,
                'block_title': block.title if block.title else 'N/A',
                'block_id': block_id,
                'channel_id': channel_id
            }
            if add_to_db_block(block_data):
                break
        except exceptions.HTTPError:
            print(HTTP_ERROR_MESSAGE)
    return block_id
