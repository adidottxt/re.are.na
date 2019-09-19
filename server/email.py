'''
This module is what is used to send an email with three blocks to
a given email address. It only uses the Flask server.
'''

from flask import Flask
from flask_graphql import GraphQLView

from pkg.schema import SCHEMA
from pkg.config import USERNAME
from pkg.constants import DATA_CHECK
from pkg.blocks import get_random_blocks
from pkg.db import add_test_data

# starting Flask application, adding graphiql url
APP = Flask('__main__')
APP.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=SCHEMA,
        graphiql=True
    )
)

def get_block_data() -> None:
    '''
    description:            this is where block data is downloaded via the
                            are.na API, using functions defined in pkg/

    return:                 None
    '''
    # only get blocks when specific request from UI is called
    get_random_blocks(3, USERNAME)

    # execute query to database using GraphQL query
    data = str(SCHEMA.execute(DATA_CHECK).data)
    print(data)

    # get data, parse for info on each block

    # send that data to a function that replaces the appropriate parts in html

    # send email with final html


if __name__ == '__main__':
    # add test data to sqlite3 database
    add_test_data()
    APP.run(host='0.0.0.0', debug=True, use_reloader=False)
    get_block_data()
