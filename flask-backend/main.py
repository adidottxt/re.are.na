import flask
from flask_graphql import GraphQLView

from pkg.schema import SCHEMA
from pkg.blocks import get_random_blocks
from pkg.db import add_test_data

app = flask.Flask('__main__')
app.debug = True

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=SCHEMA,
        graphiql=True
    )
)

add_test_data()
print(get_random_blocks(3, 'adi'))

@app.route('/')
def my_index():
    return flask.render_template("index.html")

app.run(debug=True, use_reloader=False)
