import random
import time

from timeit import default_timer as timer

def main():
    num = 1_000
    s = []

    for value in range(num):
        s.append(random.randint(0, num))

    key = random.randint(0, num)

    start = timer()
    # start_time=time.time()
    location = sequential_search(s, key)
    end = timer()
    # end_time=time.time()

    #print(s)
    print("[Sequential Search Result]")
    print("Key value {0}: location {1}".format(key, location))
    print("Elapsed Time: {}ms".format((end - start)))
    print("===================================")
    print("Start_timer Time: {}ms".format(start))
    print("End_timer Time: {}ms".format(end))
    # print("Start Time: {}ms".format(start_time))
    # print("End Time: {}ms".format(end_time))
    print("===================================")
    print()

    s.sort()

    start = time.time()
    location = binary_search(s, key)
    end = time.time()

    #print(s)
    print("[Binary Search Result]")
    print("Key value {0}: location {1}".format(key, location))
    print("Elapsed Time: {0:0.8f}ms".format((end - start) * 1_000))
    print()

    start = time.time()
    location = recursive_binary_search(s, key, 0, num - 1)
    end = time.time()

    #print(s)
    print("[Recursive Binary Search Result]")
    print("Key value {0}: location {1}".format(key, location))
    print("Elapsed Time: {0:0.8f}ms".format((end - start) * 1_000))
    print()


def sequential_search(s, key):
    num = len(s)
    location = 0
    # 코딩을 추가하세요.

    for idx, item in enumerate(s):
        if item == key:
            # print("key is {} {}".format(key, item))
            # print("key is {}".format(idx))
            return idx
    print("No key in list")
    return -1

def binary_search(s, key):
    num = len(s)
    low = 0
    high = num - 1
    location = -1
    # 코딩을 추가하세요.
    while low <= high:
        mid = (low + high) // 2
        if s[mid] > key:
            high = mid - 1
        if s[mid] == key:
            print("key = {} {}".format(key, s[mid]))
            return mid
        if s[mid] < key:
            low = mid + 1

    return location


def recursive_binary_search(s, key, low, high):
    mid = round((low + high) / 2)

    # 코딩을 추가하세요.


if __name__ == "__main__":
    main()
