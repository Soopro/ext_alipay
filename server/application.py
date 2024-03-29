# coding=utf-8
from __future__ import absolute_import

import traceback

from flask import Flask, current_app, request
from mongokit import Connection as MongodbConn

from config import config
from utils.encoders import Encoder
from utils.sup_ext_oauth import SupAuth
from utils.base_utils import make_json_response, make_cors_headers
from errors.general_errors import (NotFound,
                                   MethodNotAllowed,
                                   ErrUncaughtException)


__version_info__ = ('0', '1', '0')
__version__ = '.'.join(__version_info__)

__artisan__ = ['Majik']


def create_app(config_name='development'):
    app = Flask(__name__)

    app.version = __version__
    app.artisan = __artisan__

    # config
    app.config.from_object(config[config_name])
    app.json_encoder = Encoder

    # database connections
    app.mongodb_database = MongodbConn(
        host=app.config.get("EXT_PAYMENT_DB_HOST"),
        port=app.config.get("EXT_PAYMENT_DB_PORT"))
    app.mongodb_conn = app.mongodb_database[
        app.config.get("EXT_PAYMENT_DB_DBNAME")]

    app.sup_auth = SupAuth(ext_key=app.config.get("EXT_KEY"),
                           ext_secret=app.config.get("EXT_SECRET"),
                           grant_type=app.config.get("GRANT_TYPE"),
                           secret_key=app.config.get("SECRET_KEY"),
                           redirect_uri=app.config.get("REDIRECT_URI"),
                           expired_in=app.config.get("EXPIRED_IN"))

    from blueprints.user.models import User
    app.mongodb_database.register([User])

    # register blueprints
    from blueprints.payment import blueprint as payment_blueprint
    app.register_blueprint(payment_blueprint, url_prefix="/payment")

    from blueprints.user import blueprint as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix="/payment/user")

    # register error handlers
    @app.errorhandler(404)
    def app_error_404(error):
        current_app.logger.warn(
            "Error: 404\n{}".format(traceback.format_exc()))
        return make_json_response(NotFound())

    @app.errorhandler(405)
    def app_error_405(error):
        current_app.logger.warn(
            "Error: 405\n{}".format(traceback.format_exc()))
        return make_json_response(MethodNotAllowed())

    @app.errorhandler(Exception)
    def app_error_uncaught(error):
        current_app.logger.warn(
            "Error: Uncaught\n{}".format(traceback.format_exc()))
        return make_json_response(ErrUncaughtException(repr(error)))

    @app.before_request
    def app_before_request():
        # cors response
        if request.method == "OPTIONS":
            resp = current_app.make_default_options_response()
            cors_headers = make_cors_headers()
            resp.headers.extend(cors_headers)
            return resp

    print "-------------------------------------------------------"
    print "Payment Extension: {}".format(app.version)
    print "Developers: {}".format(', '.join(app.artisan))
    print "-------------------------------------------------------"

    return app
