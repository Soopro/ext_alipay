/* -------------------------------
 * Server Conf: sup ext url4cc 
/* ------------------------------- */

if (sup_ext_url4cc == 'undefined' || !sup_ext_url4cc){
   var sup_ext_url4cc = {}
}

var test = {
  'api': "http://127.0.0.1:6002",
  'auth_api': "http://127.0.0.1:6002/user",
  'qrcode_api': "http://127.0.0.1:6002/fwd/qrcode?text="
}

var dev = {
  'api': "http://127.0.0.1:6002",
  'auth_api': "http://127.0.0.1:6002/user",
  'qrcode_api': "http://127.0.0.1:6002/fwd/qrcode?text="
}

var prd = {
  'api': "http://ext.soopro.com/url4/server",
  'auth_api': "http://ext.soopro.com/url4/server/user",
  'qrcode_api': "http://ext.soopro.com/url4/server/fwd/qrcode?text="
}

sup_ext_url4cc.server = dev
sup_ext_url4cc.cookie_domain = ".sup.local"
sup_ext_url4cc.is_debug = true;
