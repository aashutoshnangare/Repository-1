def Sum(No):

    Ans = 0

    while No != 0 :
        Digit = No %  10
        Ans = Ans + Digit
        No = No // 10

    return Ans

def main():

    print("Enter the Number :")
    Value = int(input())

    Ret = Sum(Value)
    print("The sum of Digits:",Ret)

if __name__ == "__main__":
    main()
