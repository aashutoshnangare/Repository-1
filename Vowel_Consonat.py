def CheckVowel(Letter):
    Letter = Letter.lower()

    if Letter == "a" or Letter == "e" or Letter == "i" or Letter == "o" or Letter == "u":
        return True
    
    else:
        return False
    
def main():

    print("Enter The Letter :")
    Character = input()

    Ret = CheckVowel(Character)

    if Ret:
        print(Character,"The Letter is vowel")

    else:
        print(Character,"The Letter is Consonant")

if __name__ == "__main__":
    main()