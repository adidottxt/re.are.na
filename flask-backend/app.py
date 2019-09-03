'''
grapiql setup app
'''
from flask import Flask
from flask_graphql import GraphQLView

from pkg.models import DB_SESSION
from pkg.schema import SCHEMA
from pkg.db import add_test_data

APP = Flask(__name__)
APP.debug = True

APP.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=SCHEMA,
        graphiql=True
    )
)


@APP.teardown_appcontext
def shutdown_session(exception=None):  # pylint:disable=unused-argument
    '''
    shut down database
    '''
    DB_SESSION.remove()


if __name__ == '__main__':
    # add_test_data()
    APP.run()
