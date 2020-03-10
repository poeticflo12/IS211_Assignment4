#!python3
import time
import random


# part 1
def sequential_search(a_list, item):
    start = time.process_time()
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    end = time.process_time()
    timeTaken = end - start

    return [found, timeTaken]
