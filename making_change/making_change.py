#!/usr/bin/python

import sys

def making_change(amount, denominations, cache = {}):
    if amount == 0:
        return 1
    elif amount < 0:
        return 0
    else:
        if amount in cache.keys():
            return cache[amount]
        else:
            total = 0
            for denom in denominations:
                value = making_change(amount - denom, denominations)
                # print(f'Amount: {amount - denom} returned: {value} for Denom: {denom}')
                cache[amount - denom] = value
                total += value
            print(f'Total: {total}')
            return total


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")