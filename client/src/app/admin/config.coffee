angular.module "paymentConsoleApp"

.constant "Config",
  base_url: payment.server.host
  api: payment.server.api

  path:
    default: "/order"
    auth: "/auth"
    notify: "notify"
    login: "/login"

  sup_auth_uri: payment.server.sup_auth