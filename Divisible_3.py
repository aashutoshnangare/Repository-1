def Divisble(No):
    
    if No % 3 == 0 and No % 5 == 0 :
        return True
    
    elif No % 3 == 0 and No % 5 != 0:
        return "Three"
    
    elif No % 5 == 0 and No % 3 != 0:
        return "Five"
    
    else:
        return False
    
def main():

    print("Enter the number:")
    Value = int(input())

    Ret = Divisble(Value)
    
    if Ret == True:
        print("The Number is Divisble by 3 & 5")

    elif Ret == "Three":
        print("The Number is Divsible by 3 & not 5 ")

    elif Ret ==  "Five":
        print("The Number is Divsible by 5 & not 3 ")

    else:
        print("The Number is not Divisble by 3 & 5")

if __name__ == "__main__":
    main()