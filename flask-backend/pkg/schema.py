'''
schema.py is where defining the schema for SQLAlchemy is defined via
graphene, which allows us to use GraphQL to query information from the
sqlite3 database set up in the other modules within pkg/
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
    description:            This is where ChannelNode is defined
    '''
    class Meta:
        model = ChannelModel
        interfaces = (relay.Node, )


class ChannelConnections(relay.Connection):
    '''
    description:            This is where ChannelConnections is defined
    '''
    class Meta:
        node = ChannelNode


class BlockNode(SQLAlchemyObjectType):
    '''
    description:            This is where BlockNode is defined
    '''
    class Meta:
        model = BlockModel
        interfaces = (relay.Node, )


class BlockConnections(relay.Connection):
    '''
    description:            This is where BlockConnections is defined
    '''
    class Meta:
        node = BlockNode


class Query(graphene.ObjectType):
    '''
    description:            This is where the ability to query the
                            sqlite3 database via GraphQL is defined
    '''
    node = relay.Node.Field()
    all_blocks = SQLAlchemyConnectionField(BlockConnections)
    all_channels = SQLAlchemyConnectionField(ChannelConnections)


SCHEMA = graphene.Schema(query=Query)
