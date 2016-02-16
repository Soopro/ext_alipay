# coding=utf-8
from __future__ import absolute_import


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
    

def helper_get_term(term_alias):
    class alipay(object):
        def get_profile(self):
            profile = current_app.mongo_conn.\
                        AlipayProfile.find_one_by_app_id()
            if not profile:
                raise Exception()
            return output_profile(profile)
            
        def save_profile(self):
            alipay_pid = get_request_json('alipay_pid', required=True)
            alipay_key = get_request_json('alipay_key', required=True)
            seller_email = get_request_json('seller_email', required=True)
            
            Profile = current_app.mongo_conn.AlipayProfile
            profile = Profile.find_one_by_app_id() or Profile()
            
            profile['open_id'] = 
            profile['alipay_pid'] = alipay_pid
            profile['alipay_key'] = alipay_key
            profile['seller_email'] = seller_email
                
            profile.save()
            return output_profile(profile)
            
        def delete_profile(self):
            rofile = current_app.mongo_conn.\
                        AlipayProfile.find_one_by_app_id()
            if not profile:
                raise Exception()
            profile.delete()
            return output_profile(profile)
            
        def pay(self):
            pass
            
        @staticmethod
        def output_profile(profile):
            return {
                'id': profile['_id'],
                'open_id': profile['open_id'],
                'alipay_pid': profile['alipay_pid'],
                'alipay_key': profile['alipay_key'],
                'seller_email': profile['seller_email']
            }
            
    TERMS = {
        'alipay': alipay
    }
    
    term = TERMS.get(term_alias)
    if not term:
        raise Exception
        
    return term