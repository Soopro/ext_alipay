'use strict';

/**
 * @ngdoc function
 * @name url4Client.controller:DashboardCtrl
 * @description
 * # DashboardCtrl
 * Controller of the url4Client
 */
angular.module('paymentClient')
.controller('TermCtrl', [
  'Config',
  '$scope',
  'restAPI',
  '$location',
  '$routeParams',
  function (
    Config, 
    $scope,
    restAPI,
    $location,
    $routeParams
  ) {
    var alias = $routeParams['alias'];
    $scope.payment = restAPI.payment.get({'alias': alias});

    $scope.setBackground = function(payment){
      if(payment.term){
        return 'styles/' + payment.term + '_active.png'
      }else{
        return ''
      }
      
    };

    $scope.jumpTo = function(route) {
      $location.path(route);
    };
    $scope.setTemplate = function(payment){
      if(payment.term){
        return '/views/terms/' + payment.term + '.html';
      }else{
        return "";
      }
    };
    $scope.submit = function(route) {
      if($scope.payment.id){
        $scope.payment.$update({'alias': $scope.payment.term});
      }
      else{
        $scope.payment.$save({'alias': $scope.payment.term});
      }
    };
}]);
