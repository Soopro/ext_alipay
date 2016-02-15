#coding=utf-8
from __future__ import absolute_import

from flask import Blueprint, request, current_app
from .models import AlipayProfile, AlipayOrder
from .routes import urlpatterns
from errors.base_errors import APIError
from utils.base_utils import make_json_response, route_inject
from utils.request import verify_token


bp_name = 'alipay'

open_api_endpoints = [
    "{}.get_shoptitle".format(bp_name),
    "{}.new_order".format(bp_name),
    "{}.get_member_id_order".format(bp_name),
    "{}.get_order".format(bp_name),
    "{}.confirm_payment".format(bp_name),
    "{}.log_payment".format(bp_name)
]


blueprint = Blueprint(bp_name, __name__, static_folder='static')

route_inject(blueprint, urlpatterns)

model_list = [AlipayProfile, AlipayOrder]


@blueprint.before_app_first_request
def before_first_request():
    current_app.mongodb_database.register(model_list)
    return


@blueprint.before_request
def before_request():
    if request.endpoint in open_api_endpoints:
        return
    verify_token()
    return


@blueprint.errorhandler(APIError)
def app_error(e):
    return make_json_response(e)