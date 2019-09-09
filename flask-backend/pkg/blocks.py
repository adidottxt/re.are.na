'''
blocks.py contains code that pertains to obtaining information
about the are.na blocks to be presented on re.are.na
'''
import random
from typing import List
from urllib3.exceptions import HTTPError

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


def get_random_blocks(number, username) -> List[int]:
    '''
    description:            get a number of random blocks from
                            a user's channels

    param:                  number: the number of blocks to return
                            user: given user's slug/username

    return:                 block_ids: a list of random block IDs
    '''
    # this could be a list comprehension but for the print statement
    blocks = []
    channels = get_random_channels(username, number)

    for i in range(number):
        print('Getting info on block {} of {}...'.format(i + 1, number))
        blocks.append(get_random_block(channels[i]))

    return blocks

def get_random_channels(username, number) -> List[str]:
    '''
    description:            get a random channel from a list of
                            a user's channels

    param:                  username: given user's username

    return:                 channel_slug: the random channel's unique URL
    '''
    final_channel_ids = [] # type: List[str]
    count = 0

    while True:
        if count > 5:
            print(HTTP_ERROR_MESSAGE)
            print(final_channel_ids)
            return final_channel_ids
        try:
            channels, _ = CLIENT.users.user(username).channels(per_page=100)

            # get all channel unique URLs -- are.na/username/channel-slug
            all_chan_slugs = {chan.slug for chan in channels if chan.published}

            random_channel_slugs = [
                random.sample(all_chan_slugs, 1)[0] \
                for i in range(number)
            ]

            for channel_slug in random_channel_slugs:
                temp_channel_id = CLIENT.channels.channel(channel_slug).id

                if check_unique_data(temp_channel_id, CHANNEL):
                    add_to_db_channel(temp_channel_id, channel_slug)
                    final_channel_ids.append(temp_channel_id)

            if len(final_channel_ids) == number:
                return final_channel_ids

            count += 1

        # HTTP error is usually down to the are.na API
        except HTTPError:
            print(HTTP_ERROR_MESSAGE)


def get_random_block(channel_id) -> int:
    '''
    description:            get a random block from a list of
                            blocks within a user's channel

    param:                  channel_slug: the channel's unique URL

    return:                 block_id: the random block's unique id
    '''
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
        block_id = int(random.sample(block_ids, 1)[0])

        if check_unique_data(block_id, BLOCK):
            try:
                # get block info
                # 403 UNAUTHORIZED HTTP ERROR HERE
                # 404 NOT FOUND FOR URL GIVEN ERROR HERE
                block = CLIENT.blocks.block(block_id)
            except HTTPError:
                print(HTTP_ERROR_MESSAGE)
                continue

            # check block type
            # (are.na's naming convention for this is class)
            block_type = getattr(block, 'class')

            # get the block's content, which is a URL or text depending
            # on the block type
            # TYPE ERROR HERE W ATTACHMENT
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

            if add_to_db_block(block_data):
                break

    return block_id
