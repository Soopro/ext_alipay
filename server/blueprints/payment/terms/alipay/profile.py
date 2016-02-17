# coding=utf-8
from __future__ import absolute_import

from utils.models import BaseDocument


class AlipayProfile(BaseDocument):
    __collection__ = 'alipay_profile'
    structure = {
        'open_id': unicode,  # soopro_open_id
        'alipay_pid': unicode,
        'alipay_key': unicode,
        'seller_email': unicode
    }

    def find_one_by_open_id(self, open_id):
        return self.one({
            "open_id": open_id
        })