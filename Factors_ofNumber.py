def ChkFactor(No):
    
    Factors = []

    for i in range(1,No+1):
        if No % i == 0:
            Factors.append(i)

    return Factors

def main():

    print("Enter the Number :")
    Value = int(input())

    Ret  =  ChkFactor(Value)
    print("The factors of Number are :",Ret)

if __name__ == "__main__":
    main()

