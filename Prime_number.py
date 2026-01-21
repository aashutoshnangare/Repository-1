def PrimeN(No):

    if No < 2:
        return False

    for i in range(2,No):
        if No % i == 0:
            return False

    return True

def main():

    print("Enter the Number :")
    Value = int(input())

    Ret = PrimeN(Value)

    if Ret:
        print(Value,"is a prime number")
    
    else:
        print(Value,"is not a prime number")

if __name__ == "__main__":
    main()
