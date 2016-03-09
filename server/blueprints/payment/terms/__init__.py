# coding=utf-8
from __future__ import absolute_import

from . import alipay

TERMS = {
    'alipay': alipay
}

profiles = [term.Profile for _, term in TERMS.items()]


def get_term(term_alias):
    term = TERMS.get(term_alias)
    if not term:
        raise Exception

    return term
