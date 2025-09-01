def pentaNumRange(n1, n2):
    penta_nums = []
    for n in range(n1, n2):
        penta_num = n * (3 * n - 1) // 2
        penta_nums.append(penta_num)
    return penta_nums


def main():
    print("enter first number:")
    try:
        num1 = int(input())
        print("enter second number:")
        num2 = int(input())
    except ValueError:
        print("invalid input")
        return
    print(pentaNumRange(num1, num2))

if __name__ == "__main__":
    main()