def reverse(No):
    
    OrgNo = No
    rev = 0

    while No != 0:
        digit = No % 10
        rev = rev * 10 + digit
        No = No // 10
   

    if rev == OrgNo:
        return True
    else:
        return False

    return rev

def main():

    print("Enter the Number to Reverse :")
    Value = int (input())

    Ret = reverse(Value)

    if Ret:
        
        print(Value,"The number is palindrome")
    else:
        print(Value,"is not palindrome")
   

if __name__ == "__main__":
    main()       