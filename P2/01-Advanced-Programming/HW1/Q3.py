class Bank:
    def __init__(self):
        self.data = {}
        self.currency = ["IRT"]
        self.market = {}
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
        elif side == "sell" and int(amount) > self.data[trader_name][market_name[:-3]]:
            print("trader has not enough balance!")
        else:
            self.market[market_name][side].update({str(self.id): [price, amount, trader_name]})
            if side == "Buy":
                self.data[trader_name]["IRT"] -= int(amount) * int(price)
            elif side == "Sell":
                self.data[trader_name][market_name[:-3]] -= int(amount)
            print("new order created successfully!")
            self.id += 1
            self._check(market_name)

    def _check(self, market_name):
        for name1, value1 in self.market[market_name]["Sell"].items():
            for name2, value2 in self.market[market_name]["Buy"].items():
                if value1[0] == value2[0]:
                    if value1[1] > value2[1]:
                        amount = value2[1]
                        self.market[market_name]["Sell"][name1][1] = value1[1] - value2[1]
                        del self.market[market_name]["Buy"][name2]
                    elif value1[1] < value2[1]:
                        amount = value1[1]
                        self.market[market_name]["Buy"][name2][1] = value2[1] - value1[1]
                        del self.market[market_name]["Sell"][name1]
                    else:
                        amount = value1[1]
                        del self.market[market_name]["Buy"][name2]
                        del self.market[market_name]["Sell"][name1]
                    self.cash.append(f"trade {value1[2]} {value2[2]} {amount} {value1[0]}")
                    print("YEAHHHHHHHHHHHHHHHHHHHHhh")
                    print(f"new trade: maker is {value1[2]}, taker is {value2[2]}, price: {value1[0]}, amount: {amount}")

    def currency_deposit(self, currency_name: str, trader_name: str, amount: str) -> None:
        if trader_name not in self.data.keys():
            print("trader with this username does not exist.")
        elif currency_name not in self.currency:
            print("currency with this name does not exist.")
        else:
            self.data[trader_name][currency_name] += int(amount)

    def orderbook(self, market_name: str) -> None:
        if market_name not in self.market.keys():
            print("market with this name does not exist.")
        else:
            # print(self.market[market_name]["Sell"])
            sor_sell = sorted(self.market[market_name]["Sell"], key=lambda x: x[0])
            sor_buy = sorted(self.market[market_name]["Buy"], key=lambda x: x[0])
            # print(sor_buy)
            print(f"Sell:")
            for i in sor_sell:
                price = self.market[market_name]["Sell"][i][0]
                amount = self.market[market_name]["Sell"][i][1]
                print(f"{price} {amount}")
            print(f"Buy:")
            for i in sor_buy:
                price = self.market[market_name]["Buy"][i][0]
                amount = self.market[market_name]["Buy"][i][1]
                print(f"{price} {amount}")

    def trades(self, market_name: str) -> None:
        if market_name not in self.market.keys():
            print("market with this name does not exist.")
        else:
            for i in self.cash:
                print(i)


main = Bank()
command = ""
lines = []
while True:
    get = input()
    if get == "exit":
        break
    if not get:
        continue
    lines.append(get)
lines_stable = lines.copy()


def read() -> str:
    line = lines.pop(0)
    if line[0:2] == "\n":
        return read()
    try:
        if line[0] == " ":
            final_line = line[:-2] + read()
            return final_line
        elif lines[0][0] != " ":
            return line
    except:
        return line


while lines:

    command = read().split()
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
    else:
        print("invalid command")
