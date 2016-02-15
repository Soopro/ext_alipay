angular.module "payApp"

.controller "checkoutCtrl", [
  '$scope'
  'restAPI'
  '$route'
  '$routeParams'
  '$location'
  '$window'
  (
    $scope
    restAPI
    $route
    $routeParams
    $location
    $window
  ) ->
#    params_obj =
#      app_id: "54acc04ff596b130ad71b6c9"
#      member_id: "53102b43bf1044ed8b0ba36b"
#      subject: "一分钱测试物品"
#      body: "一分钱测试物品，这是商品描述！！！"
#      price: 1  # unit: fen
#      express:
#        receive_name: ''
#        receive_tel: ''
#        receive_address: ''
#      extra:
#        redirect_uri:
#          value: 'http://www.baidu.com/path?name=xxx'
#          display: '回调地址'
#    console.log encodeURIComponent(JSON.stringify(params_obj))

    if $routeParams
      $scope.order = $routeParams
      $scope.order.amount = 1
      #      change unit from yuan(float) to fen(int)
      $scope.order.price = Math.round($scope.order.price*100)
      $scope.order.total_fee = Math.round($scope.order.total_fee*100)

    else
      alert "URL Params required!"

    restAPI.shop.get app_id:$scope.order.app_id
    .$promise
    .then (cb_data) ->
      $scope.shop_name = cb_data.shop_name
      $scope.shop_logo = cb_data.shop_logo

    $scope.submit_order = ->
#      amount must be int type
      $scope.order.amount = Math.round($scope.order.amount)
      $scope.order.total_fee = $scope.order.price * $scope.order.amount

      restAPI.order.post {}
      , $scope.order
      .$promise
      .then (cb_data) ->
        $scope.order = cb_data.order
        $scope.pay_url = cb_data.pay_url
        $window.location.href = $scope.pay_url

    $scope.cancel_order = ->
      $window.close()
]
