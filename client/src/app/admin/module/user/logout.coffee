angular.module "paymentConsoleApp"
.controller "logoutCtrl", [
  "$location"
  "Auth"
  "Config"
  "$scope"
  (
    $location
    Auth
    Config
    $scope
  ) ->
    $scope.logout = () ->
      console.log 'logout'
      Auth.clean_auth()
      $location.path Config.path.login
]