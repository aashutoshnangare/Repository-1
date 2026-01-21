def area(length,breadth):
    return length * breadth

def main():

    print("Enter The Length of rectangle")
    lent = int(input())

    print("Enter The Breadth of rectangle")
    bre = int(input())

    Ret = area(lent,bre)
    print("The Area of Rectangle is :",Ret)

if __name__ == "__main__":
    main()
