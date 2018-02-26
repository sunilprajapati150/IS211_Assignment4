#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Search Algorithm Comparison """

import time
import random

def sequential_search(a_list, item):
    """
    Args:
        a_list(list): List of numbers.
        item(int): numbers in the list.
    """
    start = time.time()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    end = time.time()
    return found, end-start

def ordered_sequential_search(a_list, item):
    """
    Args:
        a_list(list): List of numbers.
        item(int): numbers in the list.
    """
    start = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos+1

    end = time.time()
    return found, end-start

def binary_search_iterative(a_list, item):
    """
    Args:
        a_list(list): List of numbers.
        item(int): numbers in the list.
    """
    start = time.time()
    a_list.sort()
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2

        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    end = time.time()
    return found, end-start

def binary_search_recursive(a_list, item):
    """
    Args:
        a_list(list): List of numbers.
        item(int): numbers in the list.
    """
    start = time.time()
    a_list.sort()

    if len(a_list) == 0:
        found = False
    else:
        midpoint = len(a_list) // 2

        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                return binary_search_iterative(a_list[:midpoint], item)
            else:
                return binary_search_iterative(a_list[midpoint + 1:], item)

    end = time.time()
    return found, end-start

def ran_number(value):
   
    random_list = random.sample(range(0, value), value)
    return random_list

def main():
  
    tests = {'test1': 500,
             'test2': 10000,
             'test3': 1000}

    for test in tests.values():
        random_list = ran_number(test)
        iter_count = 100
        output = {'seq':0,
                  'ord_seq':0,
                  'bin_iter':0,
                  'bin_recur':0}
        while iter_count > 0:
            output['seq'] += sequential_search(random_list, -1)[1]
            output['ord_seq'] += ordered_sequential_search(random_list, -1)[1]
            output['bin_iter'] += binary_search_iterative(random_list, -1)[1]
            output['bin_recur'] += binary_search_recursive(random_list, -1)[1]
            iter_count -= 1

        print "List of %s length\:" % test

        print "Sequential Search took %10.7f seconds to run" % \
              (float(output['seq']/ 100))
        print "Ordered Sequential Search took %10.7f seconds to run" % \
              (float(output['ord_seq'] / 100))
        print "Iterative Binary Search took %10.7f seconds to run" % \
              (float(output['bin_iter']/ 100))
        print "Recursive Binary took %10.7f seconds to run" % \
        (float(output['bin_recur']/ 100))
        print '\n'


if __name__ == '__main__':
    main()
