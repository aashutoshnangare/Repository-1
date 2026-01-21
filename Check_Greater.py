def ChkGreater(No1,No2):

    if No1 > No2:
        return No1
    else:
        return No2
    
def main():
    
    Ret = ChkGreater(10,20)

    print("The Greater Number is",Ret)

if __name__ == "__main__":
    main()