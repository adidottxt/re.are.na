'''
test db.py
'''
from pkg.db import (
    check_unique_data,
    add_block_to_db,
    add_channel_to_db,
    add_test_data,
    clear_database
)

from pkg.constants import (
    BLOCK,
    CHANNEL,
    TEST_DB_CHANNEL_ID,
    TEST_DB_CHANNEL_SLUG,
    TEST_DB_BLOCK_ID
)


def test_check_unique_data():
    '''
    test check_unique_data
    '''
    clear_database()

    add_channel_to_db(5, TEST_DB_CHANNEL_SLUG)
    assert not check_unique_data(5, CHANNEL)
    assert check_unique_data(1, CHANNEL)

    clear_database()

    add_channel_to_db(6, TEST_DB_CHANNEL_SLUG)
    assert check_unique_data(2, CHANNEL)
    assert not check_unique_data(6, CHANNEL)


    test_block_data = {
        'created_at': '01-01-2000',
        'block_type': 'Text',
        'block_url': 'https://www.are.na/block/{}'.format(0),
        'block_content': 'test',
        'channel_title': 'test',
        'block_title': 'test',
        'block_id': 0,
        'channel_id': 15,
    }

    add_block_to_db(test_block_data)
    assert not check_unique_data(0, BLOCK)
    assert check_unique_data(1, BLOCK)

    clear_database()

    test_block_data = {
        'created_at': '01-01-2000',
        'block_type': 'Text',
        'block_url': 'https://www.are.na/block/{}'.format(4),
        'block_content': 'test',
        'channel_title': 'testing',
        'block_title': 'test',
        'block_id': 4,
        'channel_id': 5,
    }

    add_block_to_db(test_block_data)
    assert check_unique_data(7, BLOCK)
    assert not check_unique_data(4, BLOCK)

    clear_database()


def test_add_block_to_db():
    '''
    test add_block_to_db()
    '''
    clear_database()

    test_block_data = {
        'created_at': '01-01-2000',
        'block_type': 'Text',
        'block_url': 'https://www.are.na/block/{}'.format(10),
        'block_content': 'test',
        'channel_title': 'test-add',
        'block_title': 'test',
        'block_id': 10,
        'channel_id': 25,
    }

    add_block_to_db(test_block_data)
    assert not check_unique_data(10, BLOCK)

    clear_database()


def test_add_channel_to_db():
    '''
    test add_channel_to_db()
    '''
    clear_database()

    add_channel_to_db(24, TEST_DB_CHANNEL_SLUG)
    assert not check_unique_data(24, CHANNEL)

    clear_database()


def test_add_test_data():
    '''
    test add_test_data()
    '''
    clear_database()

    add_test_data()
    assert not check_unique_data(TEST_DB_CHANNEL_ID, CHANNEL)
    assert not check_unique_data(TEST_DB_BLOCK_ID, BLOCK)

    clear_database()


def test_clear_database():
    '''
    test clear_database()
    '''
