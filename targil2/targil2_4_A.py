def Appraiser(num):
    def Basis(base):
        return base ** num
    return Basis

def main():
    pow_2=Appraiser(2)
    print (pow_2(3))
    print(pow_2(4))
    print(pow_2(5))
    print(pow_2(6))
if __name__ == "__main__":
    main()