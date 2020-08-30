# pylint: disable=invalid-name
import os

from ariadne import graphql_sync
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify, send_file
from flask import render_template

from app.api.graphql_engine import GraphqlEngine

app = Flask(__name__)

graphql_engine = GraphqlEngine()
schema = graphql_engine.schema()

@app.route("/")
def hello():
    return 'OK', 200


@app.route("/ads/<img>")
def ads_img(img):
    script_directory_path = os.path.dirname(os.path.realpath(__file__))
    img_path = os.path.join(script_directory_path, 'api', 'ads', img)
    return send_file(img_path), 200


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    # On GET request serve GraphQL Playground
    # You don't need to provide Playground if you don't want to
    # but keep on mind this will not prohibit clients from
    # exploring your API using desktop GraphQL Playground app.
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    # GraphQL queries are always sent as POST
    data = request.get_json()

    # Note: Passing the request to the context is optional.
    # In Flask, the current request is always accessible as flask.request
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code


if __name__ == "__main__":
    app.run()
