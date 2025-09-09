import time
from functools import reduce
def main():
    list1= range(1000)
    evens = list(filter(lambda x: x % 2 == 0, list1))
    odds = list(filter(lambda x: x % 2 != 0, list1))

    func1= lambda arr, num: map(lambda x: x * num, arr)

    scale= lambda x, num: x * num

if __name__ == "__main__":
    main()
