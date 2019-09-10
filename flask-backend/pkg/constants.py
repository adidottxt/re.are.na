'''
constants
'''

CHANNEL_CHECK = '{ allChannels { edges { node { channelId slug } } } }'
BLOCK_CHECK = '{ allBlocks { edges { node { channelId blockId type } } } }'
HTTP_ERROR_MESSAGE = 'HTTPError: are.na API may have issues, trying again...'
BLOCK = 'block'
CHANNEL = 'channel'
TEST_CHANNEL_ID = 469043
TEST_BLOCK_ID = 4996042
