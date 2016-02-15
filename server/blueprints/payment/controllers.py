# coding=utf-8
from __future__ import absolute_import


@output_json
def get_profile(term_alias):
    term = helper_get_term(term_alias)
    return term.get_profile()
    

@output_json
def save_profile(term_alias):
    


@output_json
def delete_profile(term_alias):
    
    

@output_json
def pay(term_alias):
    
    

def helper_get_term(term_alias):
    class alipay(object):
        def get_profile(self):
            pass
            
        def save_profile(self):
            pass
            
        def delete_profile(self):
            pass
            
        def pay(self):
            pass
            
        @staticmethod
        def output_profile(profile):
            
            
    TERMS = {
        'alipay': alipay
    }
    
    term = TERMS.get(term_alias)
    if not term:
        raise Exception
        
    return term