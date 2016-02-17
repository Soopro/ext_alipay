# coding=utf-8
from __future__ import absolute_import

from .terms import helper_get_term


@output_json
def get_profile(term_alias):
    term = helper_get_term(term_alias)
    return term.get_profile()


@output_json
def save_profile(term_alias):
    term = helper_get_term(term_alias)
    return term.save_profile()


@output_json
def delete_profile(term_alias):
    term = helper_get_term(term_alias)
    return term.delete_profile()
    

@output_json
def pay(term_alias):
    term = helper_get_term(term_alias)
    return term.pay()
    
