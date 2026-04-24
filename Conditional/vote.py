# program to get eligble for vote in india

age=int(input("enter age: "))
nation=input("enter nationality: ")

if(age>=18):
    
    if(nation == "indian"):
        print("eligble for vote")       # nested conditional
    elif(nation == "INDIAN"):
        print("eligble for vote")
    else:
        print("sorry !! you are from different country")
        print("not eligble for vote")

else:
    print("not eligble for vote \n age must be 18 or above!!")

