class Bank:
    def __init__(self):
        self.data = {}
        self.currency = ["IRT"]
        self.market = {}
        self.orders = {}
        self.cash = []
        self.id = 1

    def new_trader(self, team_name: str, trader_password: str) -> None:
        if team_name in self.data.keys():
            print("trader with this name already exists")
        else:
            self.data[team_name] = {"password": trader_password, "IRT": 0}
            print("new trader created successfully!")

    def new_currency(self, currency_name: str) -> None:
        if currency_name in self.currency:
            print("currency with this name already exists")
        else:
            self.currency.append(currency_name)
            for name, value in self.data.items():
                value.update({currency_name: 0})
            print("new currency created successfully!")

    def new_market(self, base_currency: str, quote_currency: str) -> None:
        if quote_currency not in self.currency:
            print(f"currency {quote_currency} does not exist")
        elif base_currency not in self.currency:
            print(f"currency {base_currency} does not exist")
        elif base_currency != "IRT":
            print("base currency should be IRT")
        elif quote_currency + base_currency in self.market.keys():
            print("market with these currencies already exists")
        else:
            self.market[quote_currency + base_currency] = {"Buy": {}, "Sell": {}}
            self.orders[quote_currency + base_currency] = {}
            print("new market created successfully!")

    def new_order(self, trader_name: str, trader_password: str, side: str, price: str, amount: str,
                  market_name: str) -> None:
        if trader_name not in self.data.keys():
            print("trader with this username and password does not exist.")
        elif trader_password != self.data[trader_name]["password"]:
            print("trader with this username and password does not exist.")
        elif market_name not in self.market.keys():
            print("market with this name does not exist.")
        elif side == "Buy" and int(amount) * int(price) > self.data[trader_name]["IRT"]:
            print("trader has not enough balance!")
        elif side == "Sell" and int(amount) > self.data[trader_name][market_name[:-3]]:
            print("trader has not enough balance!")
        else:
            self.market[market_name][side].update({str(self.id): [price, amount, trader_name]})
            self.orders[market_name][str(self.id)] = [side, price, amount, trader_name]
            if side == "Buy":
                self.data[trader_name]["IRT"] -= int(amount) * int(price)
            elif side == "Sell":
                self.data[trader_name][market_name[:-3]] -= int(amount)
            print("new order created successfully!")
            self.id += 1
        #     self._check(market_name)

    def _check(self, market_name):
        omit_sell = []
        omit_buy = []
        for name1, value1 in self.orders[market_name].items():
            for name2, value2 in self.orders[market_name].items():
                if int(name2) > int(name1):
                    if value1[0] == "Buy" and value2[0] == "Sell":
                        if name1 not in omit_buy and name2 not in omit_sell and int(value1[1]) >= int(value2[1]):
                            if int(value1[2]) > int(value2[2]):
                                amount = int(value2[2])
                                self.market[market_name]["Buy"][name1][1] = int(value1[2]) - int(value2[2])
                                self.orders[market_name][name1][2] = int(value1[2]) - int(value2[2])
                                self.data[value1[3]][market_name[:-3]] += int(amount)
                                self.data[value2[3]]["IRT"] += int(amount) * int(value1[1])
                                omit_sell.append(name2)
                            elif int(value1[2]) < int(value2[2]):
                                amount = int(value1[2])
                                self.market[market_name]["Sell"][name2][1] = int(value2[2]) - int(value1[2])
                                self.orders[market_name][name2][2] = int(value2[2]) - int(value1[2])
                                self.data[value1[3]][market_name[:-3]] += int(amount)
                                self.data[value2[3]]["IRT"] += int(amount) * int(value1[1])
                                omit_buy.append(name1)
                            else:
                                amount = int(value1[2])
                                self.data[value1[3]][market_name[:-3]] += int(amount)
                                self.data[value2[3]]["IRT"] += int(amount) * int(value1[1])
                                omit_buy.append(name1)
                                omit_sell.append(name2)
                            self.cash.append(f"trade {value1[3]} {value2[3]} {amount} {value1[1]}")
                            print(
                                f"new trade: maker is {value1[3]}, taker is {value2[3]}, price: {value1[1]}, amount: {amount}")
                    if value1[0] == "Sell" and value2[0] == "Buy":
                        if name1 not in omit_sell and name2 not in omit_buy and int(value1[1]) <= int(value2[1]):
                            if name1 not in omit_sell and name2 not in omit_buy and int(value1[1]) <= int(value2[1]):
                                if int(value1[2]) > int(value2[2]):
                                    amount = int(value2[2])
                                    self.market[market_name]["Sell"][name1][1] = int(value1[2]) - int(value2[2])
                                    self.orders[market_name][name1][2] = int(value1[2]) - int(value2[2])
                                    self.data[value2[3]][market_name[:-3]] += int(amount)
                                    self.data[value1[3]]["IRT"] += int(amount) * int(value1[1])
                                    omit_buy.append(name2)
                                elif int(value1[2]) < int(value2[2]):
                                    amount = int(value1[2])
                                    self.market[market_name]["Buy"][name2][1] = int(value2[2]) - int(value1[2])
                                    self.orders[market_name][name2][2] = int(value2[2]) - int(value1[2])
                                    self.data[value2[3]][market_name[:-3]] += int(amount)
                                    self.data[value1[3]]["IRT"] += int(amount) * int(value1[1])
                                    omit_sell.append(name1)
                                else:
                                    amount = int(value1[2])
                                    self.data[value2[3]][market_name[:-3]] += int(amount)
                                    self.data[value1[3]]["IRT"] += int(amount) * int(value1[1])
                                    omit_buy.append(name2)
                                    omit_sell.append(name1)
                                self.cash.append(f"trade {value1[3]} {value2[3]} {amount} {value1[1]}")
                                print(
                                    f"new trade: maker is {value1[3]}, taker is {value2[3]}, price: {value1[1]}, amount: {amount}")

        for name in omit_buy:
            del self.market[market_name]["Buy"][name]
            del self.orders[market_name][name]
        for name in omit_sell:
            del self.market[market_name]["Sell"][name]
            del self.orders[market_name][name]

    def currency_deposit(self, currency_name: str, trader_name: str, amount: str) -> None:
        if trader_name not in self.data.keys():
            print("trader with this username does not exist.")
        elif currency_name not in self.currency:
            print("currency with this name does not exist.")
        else:
            self.data[trader_name][currency_name] += int(amount)

    def orderbook(self, market_name: str) -> None:
        pass
        # if market_name not in self.market.keys():
        #     print("market with this name does not exist.")
        # else:
        #     # print(self.market[market_name]["Sell"])
        #     sor_sell = sorted(self.market[market_name]["Sell"], key=lambda x: x[0])
        #     sor_buy = sorted(self.market[market_name]["Buy"], key=lambda x: x[0])
        #     # print(sor_buy)
        #     print(f"Sell:")
        #     for i in sor_sell:
        #         price = self.market[market_name]["Sell"][i][0]
        #         amount = self.market[market_name]["Sell"][i][1]
        #         print(f"{price} {amount}")
        #     print(f"Buy:")
        #     for i in sor_buy:
        #         price = self.market[market_name]["Buy"][i][0]
        #         amount = self.market[market_name]["Buy"][i][1]
        #         print(f"{price} {amount}")

    def trades(self, market_name: str) -> None:
        pass
        # if market_name not in self.market.keys():
        #     print("market with this name does not exist.")
        # else:
        #     for i in self.cash:
        #         print(i)


main = Bank()

while True:
    read = input()
    command = read.split()
    if command[0] == "new_trader":
        main.new_trader(command[1], command[2])
    elif command[0] == "new_currency":
        main.new_currency(command[1])
    elif command[0] == "new_market":
        main.new_market(command[2], command[4])
    elif command[0] == "new_order":
        main.new_order(command[1], command[2], command[3], command[4], command[5], command[6])
    elif command[0] == "currency_deposit":
        main.currency_deposit(command[1], command[2], command[3])
    elif command[0] == "trades":
        main.trades(command[1])
    elif command[0] == "orderbook":
        main.orderbook(command[1])
    elif command[0] == "exit":
        break
    else:
        print("invalid command")
