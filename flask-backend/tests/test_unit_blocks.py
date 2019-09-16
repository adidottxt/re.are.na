'''
Trying to test blocks
'''
from pkg.blocks import (
    get_channel_id,
    get_block_object,
    get_channel_object,
    get_block_ids,
    get_block,
    get_block_from_channel,
    get_block_data,
    get_all_user_channels
)

from pkg.constants import (
    TEST_BLOCK_ID,
    TEST_CHANNEL_ID,
    TEST_CHANNEL_SLUG
)

from pkg.db import add_test_data, clear_database
from pkg.config import USERNAME


def test_get_all_user_channels(snapshot):
    '''
    testing get_all_user_channels
    '''
    test_all_chans = get_all_user_channels(USERNAME)
    snapshot.assert_match(test_all_chans)


def test_get_block_data(snapshot):
    '''
    testing get_block_data
    '''
    test_block = get_block_data(TEST_BLOCK_ID, 'test', TEST_CHANNEL_ID)
    snapshot.assert_match(test_block)


def test_get_block_object(snapshot):
    '''
    testing get_block_object
    '''
    test_block = get_block_object(TEST_BLOCK_ID)
    snapshot.assert_match(test_block)


def test_get_channel_object(snapshot):
    '''
    testing get_channel_object'''
    test_channel = get_channel_object(TEST_CHANNEL_ID)
    snapshot.assert_match(test_channel)


def test_get_channel_id(snapshot):
    '''
    testing get_channel_id
    '''
    test_chan_id = get_channel_id(TEST_CHANNEL_SLUG)
    snapshot.assert_match(test_chan_id)


def test_get_block_ids(snapshot):
    '''
    testing get_block_ids
    '''
    block_ids = get_block_ids(get_channel_object(TEST_CHANNEL_ID))
    snapshot.assert_match(block_ids)


def test_get_block_and_status(snapshot):
    '''
    test get_block_and_status
    '''
    block = get_block(0, 1, TEST_CHANNEL_ID)
    snapshot.assert_match(block)


def test_get_block_from_channel(snapshot):
    '''
    test get_block_from_channel
    '''
    add_test_data()

    block = get_block_from_channel(TEST_CHANNEL_ID)
    snapshot.assert_match(block)

    clear_database()
