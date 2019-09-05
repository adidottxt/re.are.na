'''
This is the main.py module, and is essentially where the "backend"
portion of this project, namely, the server, is created and run.
'''

from flask import Flask, request, render_template
from flask_graphql import GraphQLView
from flask_cors import CORS

from pkg.schema import SCHEMA
from pkg.blocks import get_random_blocks
from pkg.db import add_test_data, clear_database


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


@APP.before_request
def get_block_data() -> None:
    '''
    description:            this is where block data is downloaded via the
                            are.na API, using functions defined in pkg/

    return:                 None
    '''
    # only get blocks when specific request from UI is called
    if request.method == 'POST' and request.content_length == 333:
        get_random_blocks(3, 'adi')


@APP.route('/')
def my_index() -> str:
    '''
    description:            this function renders the index.html file created
                            via React, to the endpoint defined above

    return:                 the rendered index.html file
    '''
    return render_template("index.html")


@APP.teardown_appcontext
def shutdown_session(exception=None) -> None:  # pylint:disable=unused-argument
    '''
    description:            this function shuts the database in
                            DB_SESSION down as part of shutting down the
                            Flask application

    return:                 None
    '''
    clear_database()


if __name__ == '__main__':
    # add test data to sqlite3 database
    add_test_data()

    # enable cross origin resource sharing to allow front end access
    CORS(APP, resources={r'/graphql': {'origins': '*'}})

    # run Flask app
    APP.run(debug=True, use_reloader=False)
