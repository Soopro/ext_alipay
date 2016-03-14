# coding=utf-8
from __future__ import absolute_import

from .routes import urlpatterns
from flask import Blueprint, request, current_app
from apiresps import APIError
from ..helpers import verify_token
from utils.helpers import route_inject
from utils.api_utils import make_json_response

bp_name = 'payment'

customer_api_endpoints = [
    "{}.new_order".format(bp_name),
    "{}.get_order".format(bp_name),
    "{}.delete_order".format(bp_name),
    "{}.pay".format(bp_name)
]

blueprint = Blueprint(bp_name, __name__)

route_inject(blueprint, urlpatterns)


@blueprint.before_app_first_request
def before_first_request():
    from .models import Order
    from .terms import profiles
    current_app.mongodb_database.register([Order] + profiles)


@blueprint.before_request
def before_request():
    if request.endpoint in customer_api_endpoints:
        pass
    else:
        verify_token()


@blueprint.errorhandler(APIError)
def app_error(e):
    return make_json_response(e)
