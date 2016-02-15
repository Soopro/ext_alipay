# coding=utf-8
from __future__ import absolute_import

from utils.models import BaseDocument


class Order(BaseDocument):
    __collection__ = 'payment_order'
    structure = {
        'open_id': unicode,  # soopro_open_id
        'member_id': unicode,  # soopro_member_id
        'subject': unicode,
        'body': unicode,
        'price': int,
        'amount': int,
        'total_fee': int,
        'receive_name': unicode,
        'receive_tel': unicode,
        'receive_address': unicode,
        'payment_term': int,
        'trade_id': unicode,
        'extra': dict,
        'deleted': bool,
        'status': int 
    }
    required_fields = [
        'open_id',
        'subject',
        'price',
        'amount',
        'total_fee',
        'receive_name',
        'receive_tel',
        'receive_address',
        'payment_term',
        'trade_id',
    ]
    default_values = {
        'status': 0,
        'member_id': u"anonymous",
        'body': u"",
        'deleted': False
    }

    def find_all_by_open_id(self, open_id):
        return self.find({
            "open_id": open_id
        })

    def find_all_by_member_id(self, member_id):
        return self.find({
            "member_id": member_id
        })
