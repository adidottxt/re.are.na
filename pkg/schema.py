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
    class Meta:
        model = ChannelModel
        interfaces = (relay.Node, )

class ChannelConnections(relay.Connection):
    class Meta:
        node = ChannelNode

class BlockNode(SQLAlchemyObjectType):
    class Meta:
        model = BlockModel
        interfaces = (relay.Node, )

class BlockConnections(relay.Connection):
    class Meta:
        node = BlockNode

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # no real reason to sort by primary key (block_id)
    all_blocks = SQLAlchemyConnectionField(BlockConnections)

    # no real reason to sort by primary key (channel_id)
    all_channels = SQLAlchemyConnectionField(ChannelConnections, sort=None)

schema = graphene.Schema(query=Query)
