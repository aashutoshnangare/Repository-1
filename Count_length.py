def Count(No):

    Duplicate = No
    count = 0

    while Duplicate !=0:

        Duplicate = Duplicate // 10 
        count += 1

    return count


def main():

    print("Enter the number")
    Value = int(input())

    Ret = Count(Value)
    print("The Count of number is: ",Ret)

if __name__ == "__main__":
    main()

