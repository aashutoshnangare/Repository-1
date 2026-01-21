def area(No):
    pi = 3.14
    return (No * No) * pi

def main():

    print("Enter the radius of circle")
    radius = int(input())

    Ret = area(radius)
    print("The area of circle is :",Ret)

if __name__ == "__main__":
    main()