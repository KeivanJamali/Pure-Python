import re


class Account:
    def __init__(self, username, password, nationalcode, creditcard, email):
        self.username = self.username_validation(username)
        self.password = self.password_validation(password)
        self.nationalcode = self.nationalcode_validation(nationalcode)
        self.creditcard = self.creditcard_validation(creditcard)
        self.email = self.email_validation(email)

    def username_validation(self, username):
        """
        Validates the given username.

        Args:
            username (str): The username to be validated.

        Returns:
            str: The validated username.

        Raises:
            Exception: If the username is invalid.
        """
        if not re.match(r"^[A-Za-z]+[_.][A-Za-z]+$", username):
            raise Exception("invalid UserName")
        else:
            return username

    def password_validation(self, password):
        """
        Validates the given password against a set of rules.

        Parameters:
            password (str): The password to be validated.

        Returns:
            str: The validated password.

        Raises:
            Exception: If the password does not meet the required criteria.
        """
        if not re.match(
            r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@!#$])[A-Za-z\d@!#$].{8,}$", password
        ):
            raise Exception("invalid Password")
        else:
            return password

    def nationalcode_validation(self, nationalcode):
        """
        Validates a national code.

        Args:
            nationalcode (str): The national code to be validated.

        Raises:
            Exception: If the length of the national code is not equal to 10 or the last digit is not valid.

        Returns:
            str: The validated national code.

        """
        same = 0
        for i in range(len(str(nationalcode)) - 1):
            if str(nationalcode)[i] != str(nationalcode)[i + 1]:
                break
            else:
                same += 1

        if same == len(str(nationalcode)) - 1:
            raise Exception("invalid NationalCode")

        if len(str(nationalcode)) != 10:
            raise Exception("invalid NationalCode")
        else:
            control = sum(
                [
                    (10 - i) * int(list(str(nationalcode))[i])
                    for i in range(len(str(nationalcode)) - 1)
                ]
            )
            remain = divmod(control, 11)[1]
            if remain < 2:
                control = remain
            else:
                control = 11 - remain
            if int(list(str(nationalcode))[-1]) != control:
                raise Exception("invalid NationalCode")
            else:
                return nationalcode

    def creditcard_validation(self, creditcard):
        """
        Validates a credit card number.

        Parameters:
            creditcard (str): The credit card number to be validated.

        Returns:
            str: The validated credit card number.

        Raises:
            ValueError: If the credit card number is invalid.
        """
        control_c = 0
        if len(str(creditcard)) != 16:
            raise Exception("invalid CreditCard")
        for i in range(len(str(creditcard))):
            if (i + 1) % 2 == 0:
                control_c += int(str(creditcard)[i])
            else:
                if int(str(creditcard)[i]) * 2 > 9:
                    control_c += int(str(creditcard)[i]) * 2 - 9
                else:
                    control_c += int(str(creditcard)[i]) * 2
        A = divmod(control_c, 10)[1]
        if A != 0:
            raise Exception("invalid CreditCard")
        else:
            return creditcard

    def email_validation(self, email):
        """
        Validates a credit card number.

        Parameters:
            email (str): The email to be validated.

        Returns:
            str: The validated email.

        Raises:
            ValueError: If the email is invalid.
        """
        count = 0
        email_s = email.split("@")
        username = email_s[0]
        domain_tld = email_s[1]
        if not re.match(r"^[A-Za-z0-9_.]", username):
            raise Exception("invalid Email")
        if not re.match(r"^[A-Za-z]+\.[A-Za-z]{2,3}$", domain_tld) and not re.match(
            r"^[0-9]+\.[A-Za-z]{2,3}$", domain_tld
        ):
            raise Exception("invalid Email")

        for i in str(email):
            if i == ".":
                count += 1
        if count > 2:
            raise Exception("invalid Email")
        
        return email


class Order:
    def __init__(self, name, price, products: dict):
        self.name = name
        self.price = price
        self.products = products
        self.posted = False

    def add_product(self, product, amount, price_product):
        if self.posted:
            raise ValueError(
                "Unfortunately, your products have been sent by truck and you can't change anything."
            )
        elif product in self.products:
            self.products[product] += amount
            self.price += amount * price_product
        else:
            self.products[product] = amount
            self.price += amount * price_product

    def remove_product(self, product, amount, price_product):
        if self.posted:
            raise ValueError(
                "Unfortunately, your products have been sent by truck and you can't change anything."
            )
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
        products_s = ", ".join(
            [f"{key}: {value}" for key, value in self.products.items()]
        )
        return f"Hi {self.name} ,You have ordered {products_s} and the price will be {self.price}$."
