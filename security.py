"""
Implementation of various security classes

Authors: Manu Jayadharan
       : Rishabh Gupta
       : Gaurav
"""
import inspect

class Base:
    def __init__(self):
        self.init_locals = locals()
        self.type_name = self.get_type_name()


    def get_type_name(self):
        type_name_l = str(__class__).split('.')
        type_name = type_name_l[-1][:type_name_l[-1].index("'")]
        return type_name
    def get_clone_dict(self):
        """
        Method for returning the name of the class and value of members needed to
        clone the instance of the class.
        :return: Dictionary containing the name of the class, and value of members to clone the object.
        """
        # init_sig = self.init_locals
        # init_sig["self"] = type(init_sig["self"])
        # object_description = {"class_name": __class__,
        #                       "init_dict": {}}
        object_description = {"class_name": type(self.init_locals["self"]),
                              "init_dict": {key : value for key,value in self.init_locals.items() if
                                            key not in ("__class__", "self")}}
        return object_description
    def display_info(self):
        return None

    def clone(self):
        clone_dict = self.get_clone_dict()
        clone_ = clone_dict["class_name"](**clone_dict["init_dict"])
        return clone_


class Security(Base):
    def __init__(self, type_name = "NullSecurity"):
        super().__init__()
        self.init_locals = locals()
        self.type_name = type_name



    def display_info(self):
        super().display_info()
        print("Security type:", self.type_name)

    def price(self):
        return None

    # def get_clone_dict(self):
    #     object_description = {"class_name": __class__,
    #                           "init_dict": {"type": self.type}}
    #     return object_description


class Option(Security):
    def __init__(self, ticker_name, expiry_date, strike, option_type):
        # Call the constructor of the parent class (Security)
        super().__init__("Option")
        self.init_locals = locals()


        # Initialize additional member variables specific to Option
        self.expiry_date = expiry_date
        self.ticker_name = ticker_name
        self.option_type = option_type
        self.strike = strike
        self.last_bid_price = None
        self.last_ask_price = None

    def add_bid_price(self, price):
        # Function to add bid price
        self.last_bid_price = price

    def add_ask_price(self, price):
        # Function to add ask price
        self.last_ask_price = price

    def get_all_info(self):
        # Function to retrieve all member variables
        info = {
            "Ticker Name": self.ticker_name,
            "option_type": self.option_type,
            "Expiry Date": self.expiry_date,
            "Strike": self.strike,
            "Last Bid Price": self.last_bid_price,
            "Last Ask Price": self.last_ask_price
        }
        return info

    def get_security_type(self):
        return self.type_name

    def get_expiry_date(self):
        return self.expiry_date

    def get_ticker_name(self):
        return self.ticker_name

    def get_strike(self):
        return self.strike

    def get_option_type(self):
        return self.option_type

    def get_last_bid_price(self):
        return self.last_bid_price

    def get_last_ask_price(self):
        return self.last_ask_price

    def display_info(self):
        print(self.get_all_info())

    def __str__(self):
        """
        Return a string representation of the option

        Returns:
            str: String representation of the option.
        """
        option_info = "<{}-{}-{}-{}>".format(self.ticker_name, self.option_type, self.expiry_date, self.strike)
        return option_info

    # def get_clone_dict(self):
    #     object_description = {"class_name": __class__,
    #                           "init_dict": {"type": self.type}}
    #     return object_description


class CallOption(Option):
    def __init__(self, ticker_name, expiry_date, strike):
        # Call the constructor of the parent class (Option) with type 'Call'
        super().__init__(ticker_name, expiry_date, strike, option_type="Call")


class PutOption(Option):
    def __init__(self, ticker_name, expiry_date, strike):
        # Call the constructor of the parent class (Option) with type 'Put'
        super().__init__(ticker_name, expiry_date, strike, option_type="Put")


class Portfolio(Security):
    """A class representing a portfolio of securities."""

    def __init__(self, security_list=[]):
        """
        Initialize the Portfolio object.
        Args:
            securities (list, optional): A list of Security objects representing the initial securities in the portfolio. Defaults to an empty list.
        """
        super().__init__()
        self.security_list = security_list

    def add_security(self, security):
        """
        Add a security to the portfolio.

        Args:
            security (Security): The Security object to add to the portfolio.
        """
        self.security_list.append(security)

    def get_securities(self):
        """
        Get the list of securities in the portfolio.

        Returns:
            list: A list of Security objects in the portfolio.
        """
        return self.security_list

    def sum_prices(self):
        """
        Calculate the total price of all securities in the portfolio.

        Returns:
            float: The total price of all securities in the portfolio.
        """
        return sum([security.price for security in self.security_list])

    def __str__(self):
        """
        Return a string representation of the portfolio.

        Returns:
            str: String representation of the portfolio.
        """
        securities_info = "\n".join([str(security) for security in self.security_list])
        return f"Portfolio:\n{securities_info}"


if __name__== "__main__":
    print("something")