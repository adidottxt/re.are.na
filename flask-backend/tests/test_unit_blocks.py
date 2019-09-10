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


def test_get_channel_object():
    '''
    testing get_channel_object'''


def test_get_channel_id():
    '''
    testing get_channel_id
    '''
    assert get_channel_id('test-wdcl2dwjvri') == 469043


def test_get_block_ids():
    '''
    testing get_block_ids
    '''
