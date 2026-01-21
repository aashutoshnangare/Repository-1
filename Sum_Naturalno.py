def Sum_Natural(No,):
    Ans = 0

    for i in range (1,No+1):
        Ans = Ans + i

    return Ans

def main():
    
    print("Enter the number: ")
    Value = int(input())



    Ret = Sum_Natural(Value)
    print("The Sum of Natural Number is :",Ret)

if __name__ == "__main__":
    main()