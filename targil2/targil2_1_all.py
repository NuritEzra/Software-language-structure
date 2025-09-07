import time
from functools import reduce


def main():

    f = lambda x: x / 2 + 2

    # part 1
    list1 = list(map(f, range(10000)))
    print(list1)

    # part 2
    start = time.time()
    total_sum=reduce(lambda x,y: x+y, list1)
    end = time.time()
    print("Time taken by func2: ", end - start, "seconds")
    print(total_sum)

    # part 3
    start = time.time()
    total_sum=0
    for i in list1:
        total_sum+=i
    end = time.time()
    print("Time taken by func3: ", end - start, "seconds")
    print(total_sum)

    # part 4
    total_sum = reduce(lambda value, x: value + (x / 2 + 2), range(10000), 0)
    print(total_sum)

if __name__ == "__main__":
    main()
