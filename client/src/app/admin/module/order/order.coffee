angular.module "paymentConsoleApp"

.controller "orderCtrl", [
  "$rootScope"
  "$scope"
  "$route"
  "$location"
  "restAPI"
  (
    $rootScope
    $scope
    $route
    $location
    restAPI
  ) ->
    restAPI.app_id_order.get()
    .$promise
    .then (cb_data) ->
      for order in cb_data.orders
        order.create_time = new Date(order.created*1000).toLocaleString()
      $scope.orders = cb_data.orders


    $scope.filter_current_month = ->
      myDate = new Date()
      $scope.current_year = myDate.getFullYear()
      $scope.current_month = myDate.getMonth()
      $scope.current_date = myDate.getDate()
      $scope.dateFilter = (order) ->
        create_time = new Date(order.created*1000)
        create_year = create_time.getFullYear()
        create_month = create_time.getMonth()
        console.log order.create_time,create_time,create_year,create_month
        create_month is $scope.current_month and create_year is $scope.current_year

    $scope.filter_all = ->
      $scope.dateFilter = ""

    $scope.current_order_info = (order_no) ->
      $location.path("/order_info/#{order_no}")
]