'''
integration tests, blocks
'''
from typing import List

from pkg.blocks import (
    get_random_blocks,
    get_channels_from_user
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


def test_get_random_blocks():
    '''
    test get_random_blocks
    '''
    more_blocks = get_random_blocks(2, USERNAME)
    assert len(more_blocks) == 2
    assert isinstance((more_blocks[0]), int)
    assert isinstance((more_blocks[1]), int)
