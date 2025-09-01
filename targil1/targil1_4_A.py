def prime(n):
    if n < 1:
        return False
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True


def main():
    print("enter prime number:")
    try:
        num = int(input())
    except ValueError:
        print("invalid input")
        return
    if prime(num)==True:
        print("prime number")
    else:
        print("not a prime number")
        return

if __name__ == "__main__":
    main()