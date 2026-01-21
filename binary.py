def decimal(No):

    binary = ""

    while No > 0:

        binary = str(No % 2) + binary
        No = No // 2

    return binary

def main():

    print("The number is :")
    value = int(input())

    Ret = decimal(value)
    print("The decimal of number is :",Ret)

if __name__ == "__main__":
    main()