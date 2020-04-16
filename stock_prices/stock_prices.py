#!/usr/bin/python
"""
For example, `find_max_profit([1050, 270, 1540, 3800, 2])` should return 3530, which is the maximum profit that can be made from a single buy and then sell of these stock prices. 
"""
import argparse

def find_max_profit(prices):
  lowest = prices[0]
  highest = prices[1]
  # Max Profit set to 3 to begin
  maximum_profit = highest - lowest # 3 to begin
  # Loop through all of the prices
  for price in prices[1:]:
    diff = price - lowest 
    if price > highest:
      highest = price
    if price < lowest:
      lowest = price
    if diff > maximum_profit:
      maximum_profit = diff
  
  return maximum_profit

test = [2, 5, 1005, 2008, 3, 1, 0, 7]

print(find_max_profit(test))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))