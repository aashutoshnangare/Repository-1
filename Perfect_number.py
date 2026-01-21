def perfect(No):

    sum = 0

    for i in range(1,No):
        if No % 2 == 0:
            sum = sum + i

    return sum

def main():

    print("Enter the number :")
    value = int(input())

    Ret = perfect(value)
    if Ret:
        print("It is the perfect number")
    
    else:
        print("It is not the perfect number")

if __name__ == "__main__":
    main()