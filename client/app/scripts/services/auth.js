'use strict';

/**
 * @ngdoc service
 * @name url4Client.Auth
 * @description
 * # Auth
 * Service in the url4Client.
 */
angular.module('paymentClient')
  .service('Auth', ['$cookies', function ($cookie) {
  // AngularJS will instantiate a singleton by calling "new" on this function
  var ext_token = $cookie.get('token') ? $cookie.get('token') : null;

  return {
    isLoggedIn: function() {
      return ext_token? true : false;
    },
    setToken: function(token) {
      $cookie.put('token',token)
    },
    getToken: function() {
      return $cookie.get('token')
    },
    setOpenId: function(open_id) {
      $cookie.put('open_id', open_id);
    },
    getOpenId: function() {
      return $cookie.get('open_id')
    },
    cleanAuth: function() {
      $cookie.remove('token')
			$cookie.remove('open_id')
    }
  }
}]);
