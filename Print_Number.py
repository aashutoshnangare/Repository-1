def Numbers(No):

    data = []
    for i in range(1,No+1):
        data.append(i)

    return data

def main():

    print("Enter The Number :")
    Value = int(input())

    Ret = Numbers(Value)
    print("The list of Numbers",Ret)

if __name__ == "__main__":
    main()