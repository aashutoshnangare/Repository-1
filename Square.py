def Sqr(No):
    SQr = 0
    SQr = No ** 2

    return SQr

def main():

    print("Enter the Number:")
    Value = int(input())

    Ret = Sqr(Value)
    print("The Square of The number is :",Ret)

if __name__ == "__main__":
    main()

