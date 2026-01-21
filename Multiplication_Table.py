def Mul_Table(No,Data):
   
    Result = []
    Ans = 0

    for i in range(1,Data+1):
        Ans  = No * i
        Result.append(Ans)
        
    return Result

def main():

    print("Enter the Number")
    Value = int(input())

    Datax = 10

    Ret = Mul_Table(Value,Datax)
    print("The Multiplication Table is :",Ret)
\

if __name__ == "__main__":
    main()
