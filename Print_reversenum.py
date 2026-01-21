def reverse(No):
    Data = []

    for i in range(No,0,-1):
        Data.append(i)

    return Data 

def main():

    print("Enter the Number :")
    Value = int(input())

    Ret = reverse(Value)
    print("The List of Reverse Number is :",Ret)

if __name__ == "__main__":
    main()