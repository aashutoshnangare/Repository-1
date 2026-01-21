def display_grade(marks):

    if marks >= 75:
        return "Distinction"

    elif marks >= 60:
        return "First Class"
    
    elif marks >= 50:
        return "Second Class"
    
    elif marks < 50:
        return False
    
def main():

    print("Enter the mark :")
    value = int(input())

    Ret = display_grade(value)

    if Ret == "Distinction":
        print("You got Distinction")

    elif Ret == "First Class":
        print("You got First Class")

    elif Ret == "Second Class":
        print("You got Second Class")

    else:
        print("You are Failed")

if __name__ == "__main__":
    main()