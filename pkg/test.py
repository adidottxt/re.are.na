import json

from arena import Arena

from .config import ACCESS_TOKEN

client = Arena(ACCESS_TOKEN)

if __name__ == '__main__':
    chan = client.channels.channel('photo-street')
    blocks, page = chan.contents()

    print(blocks[0].source)
    print(getattr(blocks[1], 'class'))

