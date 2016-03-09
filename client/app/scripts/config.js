'use strict';

/**
 * @ngdoc service
 * @name paymentClient.config
 * @description
 * # config
 * Constant in the paymentClient.
 */
angular.module('paymentClient')
.constant('Config', function(){
  var test = {
    api: "http://127.0.0.1:5003/payment",
    auth_api: "http://127.0.0.1:5003/payment/user",
    qrcode_api: "http://127.0.0.1:5003/payment/qrcode?text="
  }
  
  var dev = {
    api: "http://127.0.0.1:5003/payment",
    auth_api: "http://127.0.0.1:5003/payment/user",
    qrcode_api: "http://127.0.0.1:5003/payment/qrcode?text="
  }
  
  var prd = {
    api: "http://ext.soopro.com/payment/server/payment",
    auth_api: "http://ext.soopro.com/payment/server/payment/user",
    qrcode_api: "http://ext.soopro.com/payment/server/payment/qrcode?text="
  }
  
  var config = dev
  
  return config

}());
