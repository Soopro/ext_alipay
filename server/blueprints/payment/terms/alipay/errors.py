# coding=utf-8
from __future__ import absolute_import

from apiresps.errors import InternalServerError


class ProfileNotFound(InternalServerError):
    status_message = "ALIPAY_PROFILE_NOT_FOUND"
    response_code = 401001


class ProfileHasExisted(InternalServerError):
    status_message = "ALIPAY_PROFILE_HAS_EXISTED"
    response_code = 401002
