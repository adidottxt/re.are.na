'''
This is the main.py module, and is essentially where the "backend"
portion of this project, namely, the server, is created and run.
'''
import sys

from flask import Flask, request, render_template
from flask_graphql import GraphQLView
from flask_cors import CORS
from jinja2 import Template

from pkg.schema import SCHEMA
from pkg.config import ARENA_USERNAME
from pkg.constants import REQUEST_LENGTH, DATA_CHECK
from pkg.html import JINJA_HTML
from pkg.blocks import get_random_blocks
from pkg.db import add_test_data, clear_database
from pkg.mail import create_content, send_email


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
    if request.method == 'POST' and request.content_length == REQUEST_LENGTH:
        get_random_blocks(3, ARENA_USERNAME)


def get_blocks_for_email() -> None:
    '''
    description:            this is where block data is downloaded via the
                            are.na API, using functions defined in pkg/

    return:                 None
    '''
    get_random_blocks(3, ARENA_USERNAME)

    # execute query to database using GraphQL query
    data = SCHEMA.execute(DATA_CHECK).data['allBlocks']['edges'][1:]
    content = []

    # get data, parse for info on each block
    for block in data:

        block_id = block['node']['blockId']
        block_content = block['node']['blockContent']
        block_channel = block['node']['channelTitle']
        block_add_date = block['node']['blockCreateDate']

        if block['node']['blockType'] == 'Text':
            content.append(create_content(block_id, block_content, 'Text'))
        else:
            content.append(create_content(block_id, block_content, 'Media'))

        content.append(create_content(block_channel, block_add_date, 'Info'))

    # create email content with data
    email_template = Template(JINJA_HTML)
    email_content = email_template.render(
        block1=content[0],
        block1_info=content[1],
        block2=content[2],
        block2_info=content[3],
        block3=content[4],
        block3_info=content[5],
    )

    # send email with final html
    send_email(email_content)


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
    if len(sys.argv) > 1 and sys.argv[1] == '--email':
        # add test data to sqlite3 database
        add_test_data()

        # get data for email
        get_blocks_for_email()


    else:
        # add test data to sqlite3 database
        add_test_data()

        # enable cross origin resource sharing to allow front end access
        CORS(APP, resources={r'/graphql': {'origins': '*'}})

        # run Flask app
        APP.run(host='0.0.0.0', debug=True, use_reloader=False)
