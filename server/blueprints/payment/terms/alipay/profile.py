# coding=utf-8
from __future__ import absolute_import

from utils.models import BaseDocument


class AlipayProfile(BaseDocument):
    TERM = 'alipay'

    __collection__ = 'alipay_profile'
    structure = {
        'open_id': unicode,  # soopro_open_id
        'pid': unicode,
        'key': unicode,
        'seller_email': unicode
    }

    required_fields = ['open_id']

    default_values = {
        'pid': u'',
        'key': u'',
        'seller_email': u''
    }

    def find_one_by_open_id(self, open_id):
        return self.one({
            "open_id": open_id
        })
