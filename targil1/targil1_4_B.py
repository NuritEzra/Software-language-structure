#Sara Borgen - 326000841
#Nurit Ezra - 327739637

def twin(num):
    if prime(num)==True:
        if prime(num+2)==True:
            return num+2
        else:
            print("invalid input")
            return -1
    else:
        print("invalid input")
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
    num = int(input())
    temp=twin(num)
    if temp!=-1:
        print(temp)

if __name__ == "__main__":
    main()