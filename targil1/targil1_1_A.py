def get_penta_num(num):
    if num < 1:
        return -1
    return int(num * (3 * num - 1) / 2)

def main():
    print("enter number:")
    try:
        num = int(input())
    except ValueError:
        print("invalid input")
        return
    print(get_penta_num(num))

if __name__ == "__main__":
    main()