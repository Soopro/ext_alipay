angular.module "payApp"

.config [
  "$routeProvider"
  (
    $routeProvider
  ) ->
    $routeProvider
    .when "/",
      templateUrl: "app/checkout/module/checkout.html"
      controller: "checkoutCtrl"
    .when "/notify",
      templateUrl: "app/checkout/module/notify.html"
      controller: "notifyCtrl"
    .otherwise {
      redirectTo: '/'
      }

]