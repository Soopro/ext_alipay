'use strict';

/**
 * @ngdoc overview
 * @name url4Client
 * @description
 * # url4Client
 *
 * Main module of the application.
 */
angular.module('paymentClient')
.config(function ($routeProvider) {
  $routeProvider
    .when('/', {
      templateUrl: 'views/dashboard.html',
      controller: 'DashboardCtrl'
    })
    .when('/auth', {
      templateUrl: 'views/auth/auth.html',
      controller: 'AuthCtrl'
    })
    .when('/redirect', {
      templateUrl: 'views/auth/redirect.html',
      controller: 'RedirectCtrl'
    })
    .when('/404', {
      templateUrl: 'views/404.html'
    })
    .otherwise({
      redirectTo: '/404'
    });
});
