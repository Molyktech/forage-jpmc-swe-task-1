import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            stock = quote['stock']
            bid_price = float(quote["top_bid"]["price"])
            ask_price = float(quote["top_ask"]["price"])
            expected_price = (bid_price + ask_price) / 2
            expected_output = (stock, bid_price, ask_price, expected_price)
            actual_output = getDataPoint(quote)

            self.assertEqual(actual_output, expected_output, f"Expected {expected_output} to equal {actual_output}")

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            stock = quote['stock']
            bid_price = float(quote["top_bid"]["price"])
            ask_price = float(quote["top_ask"]["price"])
            if bid_price > ask_price:
                expected_price = (bid_price + ask_price) / 2
                expected_output = (stock, bid_price, ask_price, expected_price)
                actual_output = getDataPoint(quote)
                self.assertEqual(actual_output, expected_output, f"Expected {expected_output} to equal {actual_output}")
            else:
                print(
                    f"Test Result: bid price {bid_price} is less than or equal to ask price {ask_price} for stock {quote['stock']}")

    """ ------------ Add more unit tests ------------ """

    def test_getRatio(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        # lets define prices
        price_a = (quotes[0]["top_bid"]["price"] + quotes[0]["top_ask"]["price"]) / 2
        price_b = (quotes[1]["top_bid"]["price"] + quotes[1]["top_ask"]["price"]) / 2

        expected_ratio = price_a / price_b if price_b != 0 else None
        actual_ratio = getRatio(price_a, price_b)

        self.assertEqual(expected_ratio, actual_ratio, f"Expected {expected_ratio} to equal {actual_ratio}")


if __name__ == '__main__':
    unittest.main()

# my different approach to avoid repeated code
# class ClientTest(unittest.TestCase):
#
#   def dataSetUp(self):
#     self.quotes = [
#       {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
#       {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
#     ]
#
#   def validate_getDataPoint(self, quotes):
#     for quote in quotes:
#       stock = quote['stock']
#       bid_price = float(quote["top_bid"]["price"])
#       ask_price = float(quote["top_ask"]["price"])
#       expected_price = (bid_price + ask_price) / 2
#       expected_output = (stock, bid_price, ask_price, expected_price)
#       actual_output = getDataPoint(quote)
#
#       self.assertEqual(actual_output,expected_output, f"Expected {expected_output} to equal {actual_output}")
#
#   def test_getDataPoint_calculatePrice(self):
#     self.validate_getDataPoint(self.quotes)
#
#   def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
#    """ Test for only when top bid > top ask"""
#    quotes_with_valid_bids = [quote for quote in self.quotes if
#                                float(quote['top_bid']['price']) > float(quote['top_ask']['price'])]
#    self.validate_getDataPoint(quotes_with_valid_bids)
#
#
#   """ ------------ Add more unit tests ------------ """
#   def test_getRatio(self):
#     # lets define prices
#     price_a = (self.quotes[0]["top_bid"]["price"] + self.quotes[0]["top_ask"]["price"]) / 2
#     price_b = (self.quotes[1]["top_bid"]["price"] + self.quotes[1]["top_ask"]["price"]) / 2
#
#     expected_ratio = price_a / price_b if price_b != 0 else None
#     actual_ratio = getRatio(price_a, price_b)
#
#     self.assertEqual(expected_ratio, actual_ratio, f"Expected {expected_ratio} to equal {actual_ratio}")
