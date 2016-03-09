# coding=utf-8
from __future__ import absolute_import

from utils.auth import AuthFailed, get_current_user, get_current_member
from apiresps.general_errors import AuthenticationFailed, ErrInactiveUser
from flask import current_app, g


def get_user_from_app():
    redis_conn = current_app.redis
    mongodb_conn = current_app.mongodb_conn
    expired_token_key_prefix = current_app.config.get(
        "INVALID_USER_TOKEN_PREFIX")
    current_user = get_current_user(redis_conn,
                                    mongodb_conn,
                                    expired_token_key_prefix)
    return current_user


def get_member():
    redis_conn = current_app.redis
    mongodb_conn = current_app.mongodb_conn
    expired_token_key_prefix = current_app.config.get(
        "INVALID_MEMBER_TOKEN_PREFIX")
    member = get_current_member(redis_conn,
                                mongodb_conn,
                                expired_token_key_prefix)
    return member


def verify_jwt():
    try:
        current_user = get_user_from_app()
    except AuthFailed:
        raise AuthenticationFailed

    if current_user is None:
        raise AuthenticationFailed

    if current_user["activated"] is not True:
        raise ErrInactiveUser

    g.current_user = current_user


def verify_jwt_allow_inactive():
    try:
        current_user = get_user_from_app()
    except AuthenticationFailed:
        raise AuthenticationFailed

    if current_user is None:
        raise AuthenticationFailed

    g.current_user = current_user


def verify_jwt_member():
    try:
        member = get_member()
    except AuthFailed:
        raise AuthenticationFailed

    g.current_member = member
