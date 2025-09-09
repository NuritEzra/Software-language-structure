from functools import reduce
import math
def Basis(base):
    def Appraiser(num):
        return (base ** num)/math.factorial(num)
    return Appraiser

def teylor(n, x):
    func=Basis(x)
    return reduce(lambda acc, val: acc + func(val), range(n), 0)


def main():
    n = int(input("Enter number of terms:"))
    x = float(input("Enter base:"))

    result = teylor(n, x)
    print(result)

if __name__ == "__main__":
    main()