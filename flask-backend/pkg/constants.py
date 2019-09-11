'''
constants
'''

CHANNEL_CHECK = '{ allChannels { edges { node { channelId slug } } } }'
BLOCK_CHECK = '{ allBlocks { edges { node { channelId blockId } } } }'

HTTP_ERROR_MESSAGE = 'HTTPError: are.na API may have issues, trying again...'

BLOCK = 'block'
CHANNEL = 'channel'

TEST_CHANNEL_ID = 469043
TEST_BLOCK_ID = 4996042
TEST_CHANNEL_SLUG = 'test-wdcl2dwjvri'

TEST_DB_CHANNEL_ID = 0
TEST_DB_CHANNEL_SLUG = 'test'
TEST_DB_BLOCK_ID = 0
