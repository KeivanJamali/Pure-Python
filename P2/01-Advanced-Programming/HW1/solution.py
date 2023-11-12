import re


class Account:
    def __init__(self, username, password, nationalcode, creditcard, email):
        self.username = self.username_validation(username)
        self.password = self.password_validation(password)
        self.nationalcode = self.nationalcode_validation(nationalcode)
        self.creditcard = self.creditcard_validation(creditcard)
        self.email = self.email_validation(email)


    def username_validation(self, username: str):
        if not re.match(r"^[A-Za-z]+[_.][A-Za-z]+$", username):
            raise Exception("invalid UserName")
        else:
            return username

    def password_validation(self, password: str):
        if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[#\$%!]).{8,}$", password):
            raise Exception("invalid Password")
        else:
            return password

    def nationalcode_validation(self, nationalcode: str):
        if len(nationalcode) != 10:
            raise Exception("invalid NationalCode")
        else:
            control = sum([(10 - i) * int(nationalcode[i]) for i in range(len(nationalcode) - 1)])
            remain = divmod(control, 11)[1]
            if remain < 2:
                control = remain
            else:
                control = 11 - remain
            if int(nationalcode[-1]) != control:
                raise Exception("invalid NationalCode")
            else:
                return nationalcode

    def creditcard_validation(self, creditcard: str):
        control_c = 0
        for i in range(len(creditcard)):
            if i % 2 == 0:
                control_c += int(creditcard[i])
            else:
                if int(creditcard[i]) * 2 > 9:
                    control_c += int(creditcard[i]) * 2 - 9
                else:
                    control_c += int(creditcard[i]) * 2
        A = divmod(control_c, 10)[1]
        if A != 0:
            raise ValueError("invalid CreditCard")
        else:
            return creditcard

    def email_validation(self, email: str):
        if not re.match(r"^[A-Za-z0-9_]+@[A-Za-z0-9]+\.[A-Za-z]{2,3}$", email) or email.split("").count(".") > 2:
            raise Exception("invalid Email")
        else:
            return email


class Order:
    def __init__(self, name, price, products: dict):
        self.name = name
        self.price = price
        self.products = products
        self.posted = False

    def add_product(self, product, amount, price_product):
        if self.posted:
            raise ValueError("Unfortunately, your products have been sent by truck and you can't change anything.")
        elif product in self.products:
            self.products[product] += amount
            self.price += amount * price_product
        else:
            self.products[product] = amount
            self.price += amount * price_product

    def remove_product(self, product, amount, price_product):
        if self.posted:
            raise ValueError("Unfortunately, your products have been sent by truck and you can't change anything.")
        elif product not in self.products:
            return f"{product} is not in your cart."
        else:
            if self.products[product] > amount:
                self.products[product] -= amount
                self.price -= amount * price_product
            else:
                raise ValueError("The request is over the limit.")

    def send_order(self):
        self.posted = True
        products_s = ', '.join([f"{key}: {value}" for key, value in self.products.items()])
        return f"Hi {self.name} ,You have ordered {products_s} and the price will be {self.price}$."
