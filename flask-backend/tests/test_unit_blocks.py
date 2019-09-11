'''
Trying to test blocks
'''
from typing import List

from pkg.blocks import (
    get_channels_from_user,
    get_channel_id,
    get_block_object,
    get_channel_object,
    get_block_ids,
)

from pkg.config import USERNAME

from pkg.constants import (
    TEST_BLOCK_ID,
    TEST_CHANNEL_ID,
    TEST_CHANNEL_SLUG
)

def test_get_channels_from_user():
    '''
    testing channel list
    '''
    channels = get_channels_from_user(1, USERNAME)

    assert len(channels) == 1
    assert isinstance(channels, List)
    assert isinstance(channels[0], int)

    more_channels = get_channels_from_user(2, USERNAME)

    assert len(more_channels) == 2
    assert isinstance(more_channels, List)
    assert isinstance(more_channels[0], int)
    assert isinstance(more_channels[1], int)
    assert channels[0] not in more_channels


def test_get_block_object():
    '''
    testing get_block_object
    '''
    test_block = get_block_object(TEST_BLOCK_ID)

    assert str(test_block.created_at) == '2019-09-10T21:36:21.270Z'
    assert getattr(test_block, 'class') == 'Text'
    assert test_block.id == TEST_BLOCK_ID
    assert test_block.base_class == 'Block'
    assert test_block.content == 'test'


def test_get_channel_object():
    '''
    testing get_channel_object'''
    test_channel = get_channel_object(TEST_CHANNEL_ID)

    assert str(test_channel.created_at) == '2019-09-10T21:25:12.325Z'
    assert test_channel.title == 'test'
    assert test_channel.id == TEST_CHANNEL_ID
    assert test_channel.status == 'closed'
    assert test_channel.length == 1
    assert test_channel.slug == TEST_CHANNEL_SLUG


def test_get_channel_id():
    '''
    testing get_channel_id
    '''
    assert get_channel_id(TEST_CHANNEL_SLUG) == TEST_CHANNEL_ID


def test_get_block_ids():
    '''
    testing get_block_ids
    '''
    assert get_block_ids(get_channel_object(TEST_CHANNEL_ID)) == {TEST_BLOCK_ID}
