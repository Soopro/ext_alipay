# coding=utf-8
from __future__ import absolute_import

from apiresps.errors import InternalServerError


class OrderNotFound(InternalServerError):
    status_message = "ORDER_NOT_FOUND"
    response_code = 400001
