import flask
from flask_graphql import GraphQLView
from flask_cors import CORS

from pkg.models import DB_SESSION
from pkg.schema import SCHEMA
from pkg.blocks import get_random_blocks
from pkg.db import add_test_data

APP = flask.Flask('__main__')

def create_app():
    APP.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=SCHEMA,
            graphiql=True
        )
    )
    add_test_data()
    print(get_random_blocks(3, 'adi'))

@APP.route('/')
def my_index():
    return flask.render_template("index.html")

@APP.teardown_appcontext
def shutdown_session(exception=None):  # pylint:disable=unused-argument
    '''
    shut down database
    '''
    DB_SESSION.remove()

if __name__ == '__main__':
    create_app()
    CORS(APP, resources={r'/graphql': {'origins': '*'}})
    APP.run(debug=True, use_reloader=False)
