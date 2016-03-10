# coding=utf-8
from __future__ import absolute_import

from .controllers import *


urlpatterns = [
    # for admin
    ("/term", get_terms, "GET"),
    ("/term/<term_alias>/profile", get_profile, "GET"),
    ("/term/<term_alias>/profile", create_profile, "POST"),
    ("/term/<term_alias>/profile", update_profile, "PUT"),
    ("/term/<term_alias>/profile", delete_profile, "DELETE"),

    ("/order", get_all_orders, "GET"),

    # for customers
    ("/order", new_order, "POST"),
    ("/order/<order_id>", get_order, "GET"),
    # ("/order/<order_id>", save_order, "PUT"),
    ("/order/<order_id>", delete_order, "DELETE"),

    ("/term/<term_alias>/pay", pay, "POST"),

]
