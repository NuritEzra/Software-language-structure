#Sara Borgen - 326000841
#Nurit Ezra - 327739637
def   sum_digit(num):
    x = num
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum



def main():
    print("enter number:")
    try:
        num = int(input())
    except ValueError:
        print("invalid input")
        return
    print(sum_digit(num))

if __name__ == "__main__":
    main()
