# coding=utf-8
from __future__ import absolute_import


class Config(object):
    DEBUG = True

    HOST = "127.0.0.1"
    PORT = 5003

    EXT_PAYMENT_DB_HOST = '127.0.0.1'
    EXT_PAYMENT_DB_PORT = 27017

    SECRET_KEY = 'secret_key'

    ALLOW_ORIGINS = ['*']
    ALLOW_CREDENTIALS = False

    EXT_KEY = 'comment-1453895893'
    EXT_SECRET = '38a6daf0-a718-4456-938f-c6ab2ad03456'
    GRANT_TYPE = 'code'

    REMOTE_OAUTH_URL = 'http://d.soopro.com/#/oauth'
    TOKEN_URL = 'http://api.soopro.com/oauth/token'

    REDIRECT_URI = 'http://localhost:9527/#/redirect'
    EXPIRED_IN = 36000

    CHECKOUT_NOTIFY_URL = u'http://localhost:5001/alipay/confirm_payment'
    CHECKOUT_RETURN_URL = u'http://localhost:9002/checkout#/notify'

    # # JWT
    # JWT_SECRET_KEY = SECRET_KEY  # SECRET_KEY
    # JWT_ALGORITHM = 'HS256'
    # JWT_VERIFY_EXPIRATION = True,
    # JWT_LEEWAY = 0
    # JWT_EXPIRATION_DELTA = timedelta(seconds=3600 * 24 * 30)
    # JWT_DEFAULT_REALM = 'Login Required'


class DevelopmentConfig(Config):
    EXT_PAYMENT_DB_DBNAME = 'ext_payment_dev'


class TestCaseConfig(Config):
    DEBUG = False
    EXT_PAYMENT_DB_DBNAME = 'ext_payment_testcase'


class TestingConfig(Config):
    DEBUG = False
    EXT_PAYMENT_DB_DBNAME = 'ext_payment_test'


class ProductionConfig(Config):
    DEBUG = False
    EXT_PAYMENT_DB_DBNAME = 'ext_payment_production'

    REDIRECT_URI = 'http://ext.soopro.com/payment/client/#/redirect'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'testcase': TestCaseConfig,
    'default': DevelopmentConfig
}
