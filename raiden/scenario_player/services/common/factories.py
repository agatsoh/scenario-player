import pathlib

from flask import Flask


def construct_flask_app(*blueprints, db_name='default', test_config=None, secret='dev'):
    """Construct a flask app with the given blueprints registered."""
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=secret,
        DATABASE=db_name,
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    # ensure the instance folder exists
    pathlib.Path.mkdir(app.instance_path, parents=True, exist_ok=True)

    return app
