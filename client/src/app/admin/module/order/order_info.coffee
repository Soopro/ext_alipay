angular.module "paymentConsoleApp"

.controller "orderInfoCtrl",[
  "$rootScope"
  "$scope"
  "restAPI"
  "$route"
  "$routeParams"
  "$location"
  (
    $rootScope
    $scope
    restAPI
    $route
    $routeParams
    $location
  ) ->
    $scope.order_no = $routeParams.order_no
    restAPI.get_order.get order_no:$scope.order_no
    .$promise
    .then (cb_data) ->
      console.log(cb_data.order)
      $scope.current_order = cb_data.order
      $scope.current_order.create_time = new Date($scope.current_order.created*1000).toLocaleString()

    $scope.delete_order = () ->
      restAPI.get_order.remove order_no:$scope.order_no
      .$promise
      .then ->
        $location.path("/order")
]
