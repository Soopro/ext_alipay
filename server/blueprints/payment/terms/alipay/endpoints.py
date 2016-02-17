# coding=utf-8
from __future__ import absolute_import


def get_profile(self):
    profile = current_app.mongo_conn.AlipayProfile.\
                find_one_by_app_id(g.current_user['open_id'])
    if not profile:
        raise Exception()
    return output_profile(profile)
    
    
def save_profile(self):
    open_id = g.current_user['open_id']
    alipay_pid = get_request_json('alipay_pid', required=True)
    alipay_key = get_request_json('alipay_key', required=True)
    seller_email = get_request_json('seller_email', required=True)
    
    Profile = current_app.mongo_conn.AlipayProfile
    profile = Profile.find_one_by_app_id(open_id) or Profile()
    
    profile['open_id'] = open_id
    profile['alipay_pid'] = alipay_pid
    profile['alipay_key'] = alipay_key
    profile['seller_email'] = seller_email
        
    profile.save()
    return output_profile(profile)
    
    
def delete_profile(self):
    profile = current_app.mongo_conn.AlipayProfile.\
                find_one_by_app_id(g.current_user['open_id'])
    if not profile:
        raise Exception()
    profile.delete()
    return output_profile(profile)
    
    
def pay(self):
    pass
    
    
def output_profile(profile):
    return {
        'id': profile['_id'],
        'open_id': profile['open_id'],
        'alipay_pid': profile['alipay_pid'],
        'alipay_key': profile['alipay_key'],
        'seller_email': profile['seller_email']
    }