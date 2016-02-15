angular.module "paymentConsoleApp"

.run [
  "$rootScope"
  "$location"
  "Auth"
  "Config"
  "restAPI"
  (
    $rootScope
    $location
    Auth
    Config
    restAPI
  ) ->

]