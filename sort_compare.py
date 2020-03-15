#!python3
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
    return [a_list, end - start]


def shell_sort(a_list):
    start = time.time()
    sublistcount = len(a_list) // 2
    while sublistcount > 0:
        for start_position in range(sublistcount):
            gap_InsertionSort(a_list, start_position, sublistcount)

        # print("After increments of size",sublistcount, "The list is",nlist)

        sublistcount = sublistcount // 2
    end = time.time()
    return [a_list, end - start]


def gap_InsertionSort(nlist, start, gap):
    for i in range(start + gap, len(nlist), gap):

        current_value = nlist[i]
        position = i

        while position >= gap and nlist[position - gap] > current_value:
            nlist[position] = nlist[position - gap]
            position = position - gap

        nlist[position] = current_value


def python_sort(a_list):
    start = time.time()
    a_list.sort()
    end = time.time()
    return [a_list, end - start]


def main():
    listSizes = [500, 1000, 10000]  # size of the lists
    for i in listSizes:  # interate the list
        is_sum = 0  # sum for insertion sort
        ss_sum = 0  # sum for shell sort
        ps_sum = 0  # sum for pyton sort
        for j in range(100):  # the number of lists required
            randomList = random.sample(range(1, 100000), i)  # generate a list of size i
            # call sorting functions
            insertion_sort_return = insertion_sort(randomList)
            shell_sort_return = shell_sort(randomList)
            python_sort_return = python_sort(randomList)

            # calclating time taken
            is_sum = is_sum + insertion_sort_return[1]
            ss_sum = ss_sum + shell_sort_return[1]
            ps_sum = ps_sum + python_sort_return[1]

        # calculating the average for the 100 lists

        average_is = is_sum / 100
        average_ss = ss_sum / 100
        average_ps = ps_sum / 100

        print("Insertion Sort took %10.7f seconds to run, on average" % average_is)
        print("Shell Sort Search took %10.7f seconds to run, on average" % average_ss)
        print("Python Sort took %10.7f seconds to run, on average" % average_ps)

        print("\n")  # line break


# Calls the main function
if __name__ == "__main__":
    main()