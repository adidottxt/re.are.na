'''
blocks.py contains code that pertains to obtaining information
about the are.na blocks to be presented on re.are.na
'''
import random
from typing import List
from requests import exceptions

from arena import Arena

from .config import ACCESS_TOKEN
from .constants import HTTP_ERROR_MESSAGE, BLOCK, CHANNEL
from .db import (
    add_to_db_channel,
    add_to_db_block,
    check_unique_data,
)

# start are.na client to be used across blocks.py
CLIENT = Arena(ACCESS_TOKEN)


def get_random_blocks(number, user) -> List[int]:
    '''
    description:            get a number of random blocks from
                            a user's channels

    param:                 number: the number of blocks to return
                            user: given user's slug/username

    return:                block_ids: a list of random block IDs
    '''
    # this could be a list comprehension but for the print statement
    blocks = []
    for i in range(number):
        print('Getting info on block {} of {}...'.format(i + 1, number))
        blocks.append(get_random_block(get_random_channel(user)))
    return blocks


def get_random_channel(username) -> str:
    '''
    description:            get a random channel from a list of
                            a user's channels

    param:                username: given user's username

    return:                 channel_slug: the random channel's unique URL
    '''
    while True:
        try:
            # get all of a given username's channels
            channels, _ = CLIENT.users.user(username).channels(per_page=100)

            # get all channel unique URLs -- are.na/username/channel-slug
            channel_slugs = {chan.slug for chan in channels if chan.published}

            # get random channel slug, and the corresponding channel id
            channel_slug = random.sample(channel_slugs, 1)[0]
            channel_id = CLIENT.channels.channel(channel_slug).id

            # check if channel has been added to database before
            if check_unique_data(channel_id, CHANNEL):
                # add to database to ensure the next channel is unique
                add_to_db_channel(channel_id, channel_slug)

                # return channel id to be used to find a random block
                return channel_id

        # HTTP error is usually down to the are.na API
        except exceptions.HTTPError:
            print(HTTP_ERROR_MESSAGE)


def get_random_block(channel_id) -> int:
    '''
    description:            get a random block from a list of
                            blocks within a user's channel

    param:                  channel_slug: the channel's unique URL

    return:                 block_id: the random block's unique id
    '''
    # get channel info from the given channel id
    channel = CLIENT.channels.channel(channel_id)

    # check how many pages are present based on length
    # (each page holds 100 blocks)
    channel_pages = channel.length // 100

    # if < 100 blocks, then we have only 1 page
    if channel.length % 100 != 0:
        channel_pages += 1

    # get all unique block ids within this channel (all pages)
    block_ids = {
        block.id
        for i in range(1, channel_pages + 1)
        for block in channel.contents(page=i, per_page=100)[0]
    }

    while True:
        # get random block id
        block_id = int(random.sample(block_ids, 1)[0])

        if check_unique_data(block_id, BLOCK):
            try:
                # get block info
                block = CLIENT.blocks.block(block_id)

                # check block type
                # (are.na's naming convention for this is class)
                block_type = getattr(block, 'class')

                # get the block's content, which is a URL or text depending
                # on the block type
                block_content = block.image['display']['url'] \
                    if block_type in ('Image', 'Link', 'Media') \
                    else block.image['display']['url'] if block_type == 'Attachment' \
                    else block.content

                # get block creation date, format YYYY-MM-DD to MM-DD-YYYY
                block_date = block.created_at[:10]
                block_date = '{}-{}'.format(block_date[5:], block_date[:4])

                # create block data as a dict to be added to database
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

                # add to database, if it works, break from while loop
                if add_to_db_block(block_data):
                    break

            # HTTP error is usually down to the are.na API
            except exceptions.HTTPError:
                print(HTTP_ERROR_MESSAGE)

    # return block_id if all is successful
    return block_id
