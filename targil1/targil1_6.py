def double(x):
    return x * 2
def pow(x):
    return x*x
def inverse(x):
    if x==0:
        return 0
    return 1/x

list_func=[double,pow,inverse]

def apply_all(func_list, num_list):
    result = {}
    for func in func_list:
        s = set()
        for num in num_list:
            s.add(func(num))
        result[func.__name__] = s
    return result

def main():

    numbers = [1, 2, 3, 0]
    result = apply_all(list_func, numbers)
    print(result)

if __name__ == "__main__":
    main()
