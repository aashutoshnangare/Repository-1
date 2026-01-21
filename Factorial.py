def Factorial(No):

    Fact = 0

    for i in range(1,No+1):
        Fact = Fact + i

    return Fact

def main():

    print("Enter the Number :")
    Value = int(input())

    Ret = Factorial(Value)

    print("The Factorial of the Numeber is :",Ret)

if __name__ == "__main__":
    main()