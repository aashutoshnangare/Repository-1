def Even(No):
    
    Data = []
    
    for i in range (2,No+2,2):
        Data.append(i)

    return Data


def main():

    Result = 0 

    print("Enter the Number: ")
    Value = int(input())

    Ret = Even(Value)

    print("The Even Numbers are :",Ret)

if __name__ == "__main__":
    main()
        
    



