'use strict';

/**
 * @ngdoc function
 * @name url4Client.controller:DashboardCtrl
 * @description
 * # DashboardCtrl
 * Controller of the url4Client
 */
angular.module('paymentClient')
.controller('DashboardCtrl', [
  'Config',
  '$scope',
  'restAPI',
  '$location',
  function (
    Config, 
    $scope,
    restAPI,
    $location
  ) {
    $scope.payments = new restAPI.payment.query();

    $scope.setBackground = function(payment){
      var status = payment.id ? 'active' : 'negative';
      return payment.term ? {"background-image": "url(styles/" + payment.term + '_' + status + '.png)'} : "";
    };

    $scope.jumpTo = function(route) {
      $location.path(route);
    };
}]);
