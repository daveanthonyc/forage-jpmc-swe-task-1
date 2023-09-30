import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    stock, bid_price, ask_price, price1 = getDataPoint(quotes[0])
    stock1, bid_price1, ask_price1, price2 = getDataPoint(quotes[1])
    self.assertEqual(price1, (ask_price+bid_price)/2)
    self.assertEqual(price2, (ask_price1+bid_price1)/2)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    stock, bid_price, ask_price, price = getDataPoint(quotes[0])
    stock1, bid_price1, ask_price1, price1 = getDataPoint(quotes[1])
    self.assertEqual(price, ask_price)
    self.assertEqual(price1, (bid_price1+ask_price1)/2)

  """ ------------ Add more unit tests ------------ """
  def test_getRatio_priceOfZeroDoesntThrowError(self):
     self.assertEqual(getRatio(0,0.123), None)
     self.assertEqual(getRatio(0.123, 0), None)

  def test_getRatio_returnsCorrectRatio(self):
     self.assertEqual(getRatio(1,2), 0.5)

if __name__ == '__main__':
    unittest.main()
