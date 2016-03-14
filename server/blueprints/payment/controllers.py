# coding=utf-8
from __future__ import absolute_import

from flask import g, current_app
from .terms import get_term, terms
from utils.api_utils import output_json
from utils.request import get_param
from .errors import OrderNotFound


@output_json
def get_profile(term_alias):
    term = get_term(term_alias)
    return term.get_profile()


@output_json
def create_profile(term_alias):
    term = get_term(term_alias)
    return term.create_profile()


@output_json
def update_profile(term_alias):
    term = get_term(term_alias)
    return term.update_profile()


@output_json
def delete_profile(term_alias):
    term = get_term(term_alias)
    return term.delete_profile()


@output_json
def pay(term_alias):
    term = get_term(term_alias)
    return term.pay()


@output_json
def get_terms():
    return [term.get_profile() for term in terms]


@output_json
def get_all_orders():
    open_id = g.curr_user['open_id']
    orders = current_app.mongodb_conn.Order.find_all_by_open_id(open_id)

    return [output_order(order) for order in orders]


@output_json
def new_order():
    open_id = g.curr_user['open_id']
    subject = get_param('subject', required=True)
    price = get_param('price', required=True)
    amount = get_param('amount', required=True)
    total_fee = price * amount
    receive_name = get_param('receive_name', required=True)
    receive_tel = get_param('receive_tel', required=True)
    receive_address = get_param('receive_address', required=True)

    member_id = get_param('member_id', default=u"anonymous")
    body = get_param('body', default=u"")

    # payment_term = get_param('payment_term', required=True)
    # trade_id = get_param('trade_id', required=True)

    order = current_app.mongodb_conn.Order()
    order['open_id'] = open_id
    order['subject'] = subject
    order['body'] = body
    order['price'] = price
    order['amount'] = amount
    order['total_fee'] = total_fee
    order['receive_name'] = receive_name
    order['receive_tel'] = receive_tel
    order['receive_address'] = receive_address
    order['member_id'] = member_id

    order.save()

    return output_order(order)


@output_json
def get_orders():
    member_id = g.current_member['id']
    orders = current_app.mongodb_conn.Order.find_all_by_member_id(member_id)

    return [output_order(order) for order in orders]


@output_json
def get_order(order_id):
    member_id = g.current_member['id']
    order = current_app.mongodb_conn.\
        Order.find_one_by_id_and_mid(order_id, member_id)
    if not order:
        raise OrderNotFound

    return output_order(order)


# @output_json
# def save_order(order_id):
#     open_id = g.curr_user['open_id']
#     subject = get_param('subject', required=True)
#     price = get_param('price', required=True)
#     amount = get_param('amount', required=True)
#     total_fee = price * amount
#     receive_name = get_param('receive_name')
#     receive_tel = get_param('receive_tel')
#     receive_address = get_param('receive_address', required=True)
#
#     member_id = get_param('member_id', default=u"anonymous")
#     body = get_param('body', default=u"")


@output_json
def delete_order(order_id):
    member_id = g.current_member['id']
    order = current_app.mongodb_conn.\
        Order.find_one_by_id_and_mid(order_id, member_id)
    if not order:
        raise OrderNotFound

    order.remove()

    return output_order(order)


def output_order(order):
    return {
        'id': order['_id'],
        'open_id': order['open_id'],
        'member_id': order['member_id'],
        'subject': order['subject'],
        'body': order['body'],
        'price': order['price'],
        'amount': order['amount'],
        'total_fee': order['total_fee'],
        'receive_name': order['receive_name'],
        'receive_tel': order['receive_tel'],
        'receive_address': order['receive_address'],
        'payment_term': order['payment_term'],
        'trade_id': order['trade_id'],
        'extra': order['extra'],
        'deleted': order['deleted'],
        'status': order['status']
    }
