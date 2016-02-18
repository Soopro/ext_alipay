# coding=utf-8
from __future__ import absolute_import

from .controllers import *


urlpatterns = [
    # for admin
    ("/term/<term_alias>/profile", get_profile, "GET"),
    ("/term/<term_alias>/profile", save_profile, "POST"),
    ("/term/<term_alias>/profile", delete_profile, "DELETE"),

    ("/order", get_all_orders, "GET"),
    
    # for customers
    ("/order", new_order, "POST"),
    ("/order", get_orders, "GET"),
    ("/order/<order_id>", get_order, "GET"),
    ("/order/<order_id>", save_order, "PUT"),
    ("/order/<order_id>", delete_order, "DELETE"),
    
    ("/term/<term_alias>/pay", pay, "POST"),

]