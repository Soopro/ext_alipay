angular.module "paymentConsoleApp"

.controller "settingsCtrl", [
  "$scope"
  "restAPI"
  (
    $scope
    restAPI
  ) ->
    $scope.settings = restAPI.profile.get()

    $scope.update_settings = ()->
      console.log 'update'
      console.log $scope.settings
      $scope.settings.$save()
]