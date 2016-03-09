'use strict';

/**
 * @ngdoc service
 * @name url4Client.restapi
 * @description
 * # restapi
 * Factory in the url4Client.
 */
angular.module('paymentClient')
  .factory('restAPI', function ($resource, Config) {
    // Service logic
    // ...
    var api = Config.api;
    var auth_api = Config.auth_api;

    // Public API here
    return {
      alias: (function () {
        return $resource(auth_api+"/alias");
      })(),
      payment: (function () {
        return $resource(api+"/term/:alias/profile", null, {
          "update": {method: "PUT"}
        });
      })(),
	  
      ext_token: (function () {
        return $resource(auth_api+"/ext_token/:open_id");
      })(),
      sup_auth: (function () {
        return $resource(auth_api+"/sup_auth");
      })(),
      token_check: (function () {
        return $resource(auth_api+"/token_check");
      })()
    };
  });
