'''
constants
'''

# these are the GraphQL queries for info on all channels and all blocks
CHANNEL_CHECK = '{ allChannels { edges { node { channelId slug } } } }'
BLOCK_CHECK = '{ allBlocks { edges { node { channelId blockId } } } }'

# this is the HTTP error message displayed when the are.na API acts up
HTTP_ERROR_MESSAGE = 'HTTPError: are.na API may have issues, trying again...'

BLOCK = 'block'
CHANNEL = 'channel'

# these are the channel + block IDs + slug data for my test channel, which
# can be used by anyone to run tests -- the test channel is not private
TEST_CHANNEL_ID = 469043
TEST_BLOCK_ID = 4996042
TEST_CHANNEL_SLUG = 'test-wdcl2dwjvri'

# these are values to test the local database
TEST_DB_CHANNEL_ID = 0
TEST_DB_CHANNEL_SLUG = 'test'
TEST_DB_BLOCK_ID = 0
