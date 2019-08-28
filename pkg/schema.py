'''
defining the schema for SQLAlchemy
'''
# pylint:disable=too-few-public-methods, missing-docstring

import graphene
from graphene import relay
from graphene_sqlalchemy import (
    SQLAlchemyObjectType,
    SQLAlchemyConnectionField
)

from .models import (
    Channel as ChannelModel,
    Block as BlockModel
)


class ChannelNode(SQLAlchemyObjectType):
    '''
    channel node
    '''
    class Meta:
        model = ChannelModel
        interfaces = (relay.Node, )


class ChannelConnections(relay.Connection):
    '''
    channel connections
    '''
    class Meta:
        node = ChannelNode


class BlockNode(SQLAlchemyObjectType):
    '''
    block node
    '''
    class Meta:
        model = BlockModel
        interfaces = (relay.Node, )


class BlockConnections(relay.Connection):
    '''
    block connections
    '''
    class Meta:
        node = BlockNode


class Query(graphene.ObjectType):
    '''
    defining how we can query
    '''
    node = relay.Node.Field()
    # no real reason to sort by primary key (block_id)
    all_blocks = SQLAlchemyConnectionField(BlockConnections)

    # no real reason to sort by primary key (channel_id)
    all_channels = SQLAlchemyConnectionField(ChannelConnections, sort=None)


SCHEMA = graphene.Schema(query=Query)
