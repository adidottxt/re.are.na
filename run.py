'''
testing
'''
from pkg.blocks import get_random_blocks
from pkg.db import add_test_data

if __name__ == '__main__':
    add_test_data()
    print(get_random_blocks(3, 'adi'))
