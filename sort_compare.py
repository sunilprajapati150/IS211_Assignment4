#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Sort and Compare """

import time
import random

def insertion_sort(a_list):
    
    start = time.time()
    for index in range(1, len(a_list)):

        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
            a_list[position] = current_value
        end = time.time()
        return a_list, end-start

def insertion_gap(a_list, start, gap):
 
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value
        
def shell_sort(a_list): 
   
    start = time.time()
    sublist_count = len(a_list) // 2

    while sublist_count > 0:
        for start_position in range(sublist_count):
            insertion_gap(a_list, start_position, sublist_count)
        sublist_count = sublist_count // 2
    end = time.time()
    return a_list, end-start

def python_sort(a_list): 
    start = time.time()
    a_list.sort()
    end = time.time()
    return a_list, end-start

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
        output = {'insert':0,
                  'shell':0,
                  'pyth':0}
        while iter_count > 0:
            output['insert'] += insertion_sort(random_list)[1]
            output['shell'] += shell_sort(random_list)[1]
            output['pyth'] += python_sort(random_list)[1]
            iter_count -= 1

        print "List of %s length the test timed:" % test
        print "Insertion Sort took %10.7f seconds to run on average" % \
              (float(output['insert'] / 100))
        print "Shell Sort took %10.7f seconds to run on average" % \
              (float(output['shell'] / 100))
        print "Python Sort took %10.7f seconds to run on average" % \
              (float(output['pyth'] / 100))
        print '\n'

if __name__ == '__main__':
    main()
