from re import T
from timeit import default_timer as timer
# import matplotlib.pyplot as plt

def main():
    # num = 30
    # searchInstance(num, True)

    time_record=[]
    fibonacci=[]
    for i in range(num):
        time_record.append(searchInstance(i, False))
        fibonacci.append(i)
    viz(fibonacci, time_record)
    return

def searchInstance(num, printmode=False):
    time = []

    start = timer()
    result = iterative_fibonacci(num)
    end = timer()
    time.append(end-start)
    if printmode:
        print_result(num, result, start, end)

    start = timer()
    result = recursive_fibonacci(num)
    end = timer()
    time.append(end-start)
    if printmode:
        print_result(num, result, start, end)


    return time
def print_result(num, result, start, end):
    print("[Recursive Fibonacci]")
    print("Num {0} : Fibonacci Number {1}".format(num, result))
    print("Elapsed Time: {0:08f}s".format((end - start)))
    print()

def viz(x, y):
    axis_list = [[],[], []]
    legend_name = ["iterative_fibonacci", "recursive_fibonacci", "f(x) = n^2 * scale(10^-10)"]

    
    for idx, item in enumerate(y):
        axis_list[0].append(item[0])
        axis_list[1].append(item[1])
        axis_list[2].append(pow(2, idx)/10000000000)
    for idx, item in enumerate(axis_list):
        if idx==2:
            # plt.plot(x, item, label=legend_name[idx], linestyle="--")
            continue
        else:
        #     continue
            plt.plot(x, item, label=legend_name[idx], linewidth=5)
    
    plt.rc('font', size=10) 
    plt.legend(loc = 'upper left')
    plt.title("Raw result")
    plt.xlabel("fibonacci num", fontsize=7) 
    plt.ylabel("time (ms)", fontsize=7) 

    plt.show()
    return

# 반복 피보나치
def iterative_fibonacci(num):
    item1=0
    item2=1
    for i in range(num):    # 입력받은 횟수만큼 반복
        item1, item2 =item2, item1+item2
    return item1

# 재귀 피보나치
def recursive_fibonacci(num):
    if num==0:              # 0일경우 0 반환
        return 0
    if num==1 or num==2:    # 첫 번째나 두 번째항일 경우 1 반환
        return 1
    return recursive_fibonacci(num-1) + recursive_fibonacci(num-2)


if __name__ == "__main__":
    main()
