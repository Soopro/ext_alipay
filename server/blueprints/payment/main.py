# coding=utf-8
from __future__ import absolute_import

from .routes import urlpatterns
from flask import Blueprint, request, current_app
from errors.base_errors import APIError
from utils.verify import verify_token
from utils.base_utils import route_inject, make_json_response

bp_name = 'payment'

open_api_endpoints = [

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
    if request.endpoint not in open_api_endpoints:
        verify_token(current_app.config.get("DEBUG"))


@blueprint.errorhandler(APIError)
def app_error(e):
    return make_json_response(e)
