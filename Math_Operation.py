def Add(No1,No2):
    return No1 + No2

def Sub(No1,No2):
    return No1 - No2

def Mul(No1,No2):
    return No1 * No2

def Div(No1,No2):
    return No1 / No2

def main():
     
    print("Enter the Number 1 :")
    Value1 = int(input())

    print("Enter the Number 2 :")
    Value2 = int(input())

    print("Addition is :", Add(Value1, Value2))
    print("Subtraction is :", Sub(Value1, Value2))
    print("Multiplication is :", Mul(Value1, Value2))
    print("Division is :", Div(Value1, Value2))

if __name__ == "__main__":
    main()

