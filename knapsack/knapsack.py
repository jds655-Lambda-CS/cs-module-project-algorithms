#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])


def knapsack_solver(items, capacity):
    remaining_capacity = capacity
    cost = 0
    selected_items = []
    value = 0
    items.sort(key=lambda x: x[2]/x[1], reverse=True)
    # Place in knapsack (if room allows) from highest to lowest
    for item in items:
        if item.size <= remaining_capacity:
            remaining_capacity -= item.size
            selected_items.append(item.index)
            cost += item.size
            value += item.value
    # print(f'Weight: {cost}  Value: {value}')
    selected_items.sort()
    return {'Value': value, 'Chosen': selected_items}


if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')