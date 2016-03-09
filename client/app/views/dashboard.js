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

    $scope.alipay = new restAPI.payment({'alias': 'alipay'});
    $scope.alipay.$get().then(function(data){
      $scope.alipay.background = 
    })

    
    

    $scope.setBackground = function(payment){
      console.log(payment);
      var status = payment.alipay_pid ? 'active' : 'negative';
      var imageUrl = "styles/" + payment.name + '_' + status + '.png';
      return {'background-image': 'url(' + imageUrl + ')'};
    };

    $scope.jumpTo = function(route) {
      $location.path(route);
    };
}]);
