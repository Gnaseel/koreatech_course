from math import ceil
import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt
def main():

    # time = searchInstance(num = 1000000, s=[], printmode=True)
    # print(time)
    # return
    search_count_record=[]
    time_record=[]
    search_range = 1000000
    for i in range(1, search_range, 1):
        search_count_record.append(i)
        time_record.append(searchInstance(num = i, s=[]))
    viz(search_count_record, time_record)
    return

def searchInstance(num, s, printmode=False):
    time = []
    for value in range(num):
        s.append(random.randint(0, num))

    key = random.randint(0, num)

    start = timer()
    location = sequential_search(s, key)
    end = timer()
    time.append((end - start) * 1_000)
    
    if printmode:
        print_result(key, location, s, start, end)

    s.sort()

    start = timer()
    location = binary_search(s, key)
    end = timer()
    time.append((end - start) * 1_000)

    if printmode:
        print_result(key, location, s, start, end)
    start = timer()
    location = recursive_binary_search(s, key, 0, num - 1)
    end = timer()
    time.append((end - start) * 1_000)

    if printmode:
        print_result(key, location, s, start, end)

    return time

def print_result(key, location, s, start, end):
    print("[Sequential Search Result]")
    print("Key value {0}: location {1}: check {2}".format(key, location, s[location]))
    print("Elapsed Time: {0:0.8f}msms".format((end - start) * 1_000))
    print()
    return

def MAfilter(list, window_size):
    re_list=[]
    for i in range(len(list)-window_size):
        list[i] = sum(list[i:i+window_size])/window_size
    for i in range(len(list)-window_size, len(list)):
        list[i] = sum(list[len(list)-window_size:len(list)])/window_size
    return list

def viz(x, y):
    axis_list = [[],[],[]]
    legend_name = ["sequential_search", "binary_search", "recursive_binary_search"]

    
    for item in y:
        axis_list[0].append(item[0])
        axis_list[1].append(item[1])
        axis_list[2].append(item[2])
    for idx, item in enumerate(axis_list):
        # if idx==0:
        #     continue
        plt.subplot(1,2,1)
        plt.plot(x, item, label=legend_name[idx])
        plt.subplot(1,2,2)
        item = MAfilter(item, 80)
        plt.plot(x, item, label=legend_name[idx])
        if idx==1000 or idx == 10000 or idx == 100000 or idx == 1000000:
            print("idx = {} time = {}".format(idx, item))
    
    plt.subplot(1,2,1)
    plt.rc('font', size=20) 
    plt.legend(loc = 'upper left')
    plt.title("Raw result")
    plt.xlabel("search size", fontsize=15) 
    plt.ylabel("time (ms)", fontsize=15) 
    plt.subplot(1,2,2)
    plt.rc('font', size=20) 
    plt.legend(loc = 'upper left')
    plt.title("Moving average filter (window = 80)")
    plt.xlabel("search size", fontsize=15) 
    plt.ylabel("time (ms)", fontsize=15) 
    plt.show()
    return

def sequential_search(s, key):
    num = len(s)
    location = 0

    # ????????? ???????????????.

    # ??????????????? ????????? ????????? ????????????.
    for idx, item in enumerate(s):
        if item == key:
            return idx
    return -1

def binary_search(s, key):
    num = len(s)
    low = 0
    high = num - 1
    location = -1

    # ????????? ???????????????.

    # ???????????? ?????? ???????????? ??????????????? ??????
    while low <= high:
        mid = (low + high) // 2
        if s[mid] > key:
            high = mid - 1
        if s[mid] == key:
            return mid
        if s[mid] < key:
            low = mid + 1

    return location


def recursive_binary_search(s, key, low, high):
    mid = round((low + high) / 2)

    # ????????? ???????????????.
    # round ????????? ???????????? ?????? ????????? ????????? ?????? ????????? ??????. ?????? ??????????????? ??????????????? ceil ??????
    mid = ceil((low + high) / 2)

    if s[mid] == key:   # ??????????????? ??? ????????? ??????
        return mid
    if low == high:     # ???????????? ?????? ?????? ??????
        return -1
    if s[mid] > key:    # ?????? ???????????? ???????????? ????????? ??????
        return recursive_binary_search(s, key, low, mid-1)
    if s[mid] < key:    # ?????? ??? ?????? ???????????? ????????? ??????
        return recursive_binary_search(s, key, mid, high)

if __name__ == "__main__":
    main()
