angular.module "payApp"


.controller "notifyCtrl", [
  '$scope'
  '$rootScope'
  '$route'
  '$routeParams'
  'restAPI'
  (
    $scope
    $rootScope
    $route
    $routeParams
    restAPI
  ) ->

    console.log($routeParams)
    $scope.payment = {}
    $scope.payment.subject = $routeParams.subject
    $scope.payment.total_fee = $routeParams.total_fee
    $scope.payment.order_no = $routeParams.out_trade_no
    $scope.payment.trade_no = $routeParams.trade_no
    $scope.payment.trade_status = $routeParams.trade_status
    restAPI.payment.post {}
      , $scope.payment
    if $scope.payment.trade_status is 'TRADE_FINISHED' or $scope.payment.trade_status is 'TRADE_SUCCESS'
      $scope.payment.paid = true

    $scope.close_notify = ->
      window.close()
]

