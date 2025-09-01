def dictionaryPrime(num):

    dictionary={
    }
    for i in range(1,num+1):
        if prime(i)==True:
            tp=twin(i)
            if tp==-1:
                dictionary[i]=None
            else:
                dictionary[i]=twin(i)
    return dictionary

def twin(num):
    if prime(num)==True:
        if prime(num+2)==True:
            return num+2
        else:
            if prime(num-2)==True:
                return num-2
            else:
                return -1
    else:
        return -1

def prime(n):
    if n < 1:
        return False
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True


def main():
    print("enter number:")
    try:
        num = int(input())
    except ValueError:
        print("invalid input")
        return
    print(dictionaryPrime(num))


if __name__ == "__main__":
    main()