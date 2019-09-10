'''
integration tests, blocks
'''
from pkg.blocks import (
    get_random_blocks,
    get_channels_from_user,
    get_block_and_status,
    get_block_from_channel
)

from pkg.constants import (
    USERNAME,
    TEST_CHANNEL_ID,
    TEST_BLOCK_ID,
)


def test_get_random_blocks():
    '''
    test get_random_blocks
    '''
    blocks = get_random_blocks(1, USERNAME)
    assert len(blocks) == 1
    assert isinstance((blocks[0]), int)

    more_blocks = get_random_blocks(2, USERNAME)
    assert len(more_blocks) == 2
    assert isinstance((more_blocks[0]), int)
    assert isinstance((more_blocks[1]), int)
    assert blocks[0] not in more_blocks


def test_get_channels_from_user():
    '''
    test get_channels_from_user
    '''
    channels = get_channels_from_user(1, USERNAME)
    assert len(channels) == 1
    assert isinstance((channels[0]), int)

    more_channels = get_channels_from_user(2, USERNAME)
    assert len(more_channels) == 2
    assert isinstance((more_channels[0]), int)
    assert isinstance((more_channels[1]), int)
    assert channels[0] not in more_channels


def test_get_block_and_status():
    '''
    test get_block_and_status
    '''
    block = get_block_and_status(1, 1, TEST_CHANNEL_ID)
    assert isinstance(block, int)
    assert block == TEST_BLOCK_ID


def test_get_block_from_channel():
    '''
    test get_block_from_channel
    '''
    block = get_block_from_channel(TEST_CHANNEL_ID)
    assert isinstance(block, int)
    assert block == TEST_BLOCK_ID
