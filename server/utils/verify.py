# coding=utf-8
from __future__ import absolute_import

from flask import current_app, request, g
from errors.general_errors import AuthenticationFailed


def verify_outer(debug=False):
    CommentExtension = current_app.mongodb_conn.CommentExtension
    if debug:
        comment_extension = CommentExtension.find_one()
        if not comment_extension:
            comment_extension = CommentExtension()
            comment_extension.save()
        g.current_comment_extension = CommentExtension
    else:
        ExtKey = request.headers.get('ExtKey')
        if not ExtKey:
            raise AuthenticationFailed('key is required')
        # extension_id = base64.b64decode(ExtKey)
        # comment_extension = CommentExtension.find_one_by_eid(extension_id)
        open_id = ExtKey
        comment_extension = CommentExtension.find_one_by_open_id(open_id)
        if not comment_extension:
            raise AuthenticationFailed('invalid key')

        if not request.url.startswith(comment_extension.allowed_origin):
            raise AuthenticationFailed('not allowed origin')

        if comment_extension.require_login:
            pass
            # memeber_token = request.headers.get('MemberAuthor')
            # open_id = comment_ext["open_id"]
            # if not check_member_token(memeber_token):
            #     raise AuthenticationFailed('login, please')

        g.current_comment_extension = comment_extension


def verify_token(debug=False):
    User = current_app.mongodb_conn.User
    if debug:
        user = User.find_one()
        if not user:
            user = User()
            user['open_id'] = u"open_id_for_test"
            user.save()
        g.current_user = user
    else:
        ext_token = request.headers.get('Authorization')
        if ext_token is None:
            raise AuthenticationFailed('Authorization(token) Required, \
                Authorization header was missing')

        open_id = current_app.sup_auth.parse_ext_token(ext_token)

        if not open_id:
            raise AuthenticationFailed('invalid token')

        current_user = User.find_one_by_open_id(open_id)
        if current_user is None:
            raise AuthenticationFailed("User Not Exist")
        # print "openid", open_id
        g.current_user = current_user
        # print "current_user:", g.current_user


def verify_customer(debug=False):
    pass
