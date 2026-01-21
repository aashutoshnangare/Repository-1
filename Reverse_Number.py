def reverse(No):
    
    rev = 0

    while No != 0:
        digit = No % 10
        rev = rev * 10 + digit
        No = No // 10

    return rev

def main():

    print("Enter the Number to Reverse :")
    Value = int (input())

    Ret = reverse(Value)
    print("The Reverse of The Number: ",Ret)

if __name__ == "__main__":
    main()       