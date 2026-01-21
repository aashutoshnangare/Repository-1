def Odd(No):

    Data = []

    for i in range(1,No+1,2):
        Data.append(i)

    return Data

def main():

    print("Enter the Number :")
    Value = int(input())

    Ret = Odd(Value)
    print("The Odd Numbers are :",Ret) 

if __name__ == "__main__":
    main()