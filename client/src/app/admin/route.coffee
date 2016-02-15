angular.module "paymentConsoleApp"

.config [
  "$routeProvider"
  (
    $routeProvider
  ) ->
    $routeProvider

    .when "/auth",
      templateUrl: "app/admin/module/user/auth.html"
      controller: "AuthCtrl"
    .when "/notify",
      templateUrl: "app/admin/module/user/notify.html"
      controller: "NotifyCtrl"

    .when "/login",
      templateUrl: "app/admin/module/order/login.html"
    .when "/settings",
      templateUrl: "app/admin/module/order/settings.html"
      controller: "settingsCtrl"
    .when "/order",
      templateUrl: "app/admin/module/order/order.html"
      controller: "orderCtrl"
    .when "/order_info/:order_no",
      templateUrl: "app/admin/module/order/order_info.html"
      controller: "orderInfoCtrl"
    .otherwise redirectTo: "/auth"

]
