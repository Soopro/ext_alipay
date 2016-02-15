angular.module "paymentConsoleApp"

# AUTH
.service "Auth", [
  "$cookieStore"
  (
    $cookieStore
  ) ->
    @set_token = (token) ->
      $cookieStore.put "token", token

    @get_token = ->
      $cookieStore.get "token"

    @set_user = (user) ->
      $cookieStore.put "open_id", user

    @get_user = ->
      $cookieStore.get "open_id"

    @clean_auth = ->
      $cookieStore.remove "token"
      $cookieStore.remove "open_id"

    return @	# don"t forget!
]

.factory "restAPI", [
  "supResource"
  "Config"
  (
    supResource
    Config
  ) ->
    ext_api = "#{Config.api}/alipay"
    auth_api = "#{Config.api}/user"

    profile: do ->
      supResource "#{ext_api}/profile"

    order: do ->
      supResource "#{ext_api}/order"

    app_id_order: do ->
      supResource "#{ext_api}/order/:app_id"

    get_order: do ->
      supResource "#{ext_api}/order/:order_no"

    ext_token: do ->
      supResource "#{auth_api}/ext_token/:open_id"

    sup_auth: do ->
      supResource "#{auth_api}/sup_auth"

    token_check: do ->
      supResource "#{auth_api}/token_check"
]