def Cube(No):

    Cubex = 0
    Cubex = No ** 3

    return Cubex

def main():

    print("Enter the Number :")
    Value = int(input())

    Ret = Cube(Value)
    print("Tne Cube of the Number is :",Ret)

if __name__ == "__main__":
    main()
