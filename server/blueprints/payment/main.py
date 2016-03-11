# coding=utf-8
from __future__ import absolute_import

from .routes import urlpatterns
from flask import Blueprint, request, current_app
from errors.base_errors import APIError
from utils.verify import verify_token, verify_customer
from utils.base_utils import route_inject, make_json_response

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
        verify_customer(current_app.config.get("DEBUG"))
    else:
        verify_token(current_app.config.get("DEBUG"))


@blueprint.errorhandler(APIError)
def app_error(e):
    return make_json_response(e)
