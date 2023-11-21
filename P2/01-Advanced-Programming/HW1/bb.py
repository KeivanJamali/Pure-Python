"""
new_trader walterwhite walterwhite@123
new_trader jessepinkman jessepinkman@123
new_trader gustavo gustavo@123
new_currency nano
new_currency eth
new_currency slp
new_currency btc
new_currency eth

currency_deposit nano walterwhite 100
currency_deposit IRT walterwhite 2000
currency_deposit nano jessepinkman 200
currency_deposit IRT jessepinkman 3000
currency_deposit nano gustavo 500
currency_deposit IRT gustavo 0
currency_deposit nano saul 331
currency_deposit IRT saul 409

new_market base_currency IRT quote_currency nano
new_market base_currency IRT quote_currency eth
new_market base_currency nano quote_currency eth

new_order jessepinkman jessepinkman@123 Buy 50 100 nanoIRT
new_order jessepinkman jessepinkman@123 Buy 50 51 nanoIRT
new_order walterwhite walterwhite@123 Sell 100 10 nanoIRT
new_order gustavo gustavo@123 Sell 10 100 nanoIRT
new_order gustavo gustavo@123 Buy 50 51 nanoIRT
new_order walterwhite walterwhite@123 Sell 10 100 nanoIRT
new_order jessepinkman jessepinkman@123 Buy 1 1000 nanoIRT
trades btcIRT
trades nanoIRT
trades usdtIRT
trades ethIRT
trades usdcIRT
orderbook nanoIRT
orderbook ethIRT
orderbook nanoIRT
exit"""