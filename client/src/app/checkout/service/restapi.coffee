angular.module "payApp"

.factory 'restAPI', [
  "supResource"
  "Config"
  (
    supResource
    Config
  ) ->
    ext_api = "#{Config.api}/alipay"

    shop: do ->
      supResource "#{ext_api}/shop/:app_id"

    order: do ->
      supResource "#{ext_api}/order/:order_no"
      , order_no: "@order_no"

    payment: do ->
      supResource "#{ext_api}/log_payment"
]