'''
testing db.py
'''

from graphene.test import Client
from ..pkg import schema

TEST_CLIENT = Client(SCHEMA)

print('test')
