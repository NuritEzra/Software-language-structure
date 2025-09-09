def Appraiser(num):
    def Basis(base):
        return base**num
    return Basis


def map_powers(n):
    return map(Appraiser, range(n))


def main():
    n = int(input("Enter number of powers:"))
    result =map_powers(n)
    base = int(input("Enter base:"))

    print(type(result))
    power_funcs = list(result)
    results = tuple(map(lambda func: func(base), power_funcs))
    print(results)
if __name__ == "__main__":
    main()
