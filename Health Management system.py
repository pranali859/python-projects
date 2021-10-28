print("Health Management System")
print("Do you want to log or retrieve data?")
i = int(input("Press 1 to log or 2 to retrieve:"))
k = input("Press D for diet or  E for exercise:")
x = int(input("Press\n 1 for Harry\n 2 for Rohan\n 3 for Hammad\n:"))


def getdate():
    import datetime
    return datetime.datetime.now()

def logDiet(x):
    if x==1:
        a = input()
        with open("HarryDiet.txt", "a") as f:
            f.write(str([str(getdate())])+f"{a}"+"\n")

    elif x==2:
        a = input()
        with open("RohanDiet.txt", "a") as fp:
            fp.write(str([str(getdate())])+f"{a}"+"\n")

    elif x==3:
        a = input()
        with open("HammadDiet.txt", "a") as ff:
            ff.write(str([str(getdate())])+f"{a}"+"\n")

    else:
        print("enter valid input")

def logExercise(x):
    if x==1:
        a = input()
        with open("HarryExercise.txt", "a") as f:
            f.write(str([str(getdate())])+f"{a}"+"\n")

    elif x==2:
        a = input()
        with open("RohanExercise.txt", "a") as f:
            f.write(str([str(getdate())])+f"{a}"+"\n")

    elif x==3:
        a = input()
        with open("HammadExercise.txt", "a") as f:
            f.write(str([str(getdate())])+f"{a}"+"\n")

    else:
        print("enter valid input")

def RetrieveDiet(x):
    if x==1:
        f = open("HarryDiet.txt")
        for item in f:
            print(item , end=" ")
        f.close()

    elif x==2:
        f = open("RohanDiet.txt","r+")
        for item in f:
            print(item , end=" ")
        f.close()

    elif x==3:
        f = open("HammadDiet.txt","r+")
        for item in f:
            print(item , end=" ")
        f.close()

    else:
        print("enter valid input")

def RetrieveExercise(x):
    if x==1:
        f = open("HarryExercise.txt", "r+")
        for item in f:
            print(item , end=" ")
        f.close()

    elif x == 2:
        f = open("RohanExercise.txt", "r+")
        for item in f:
            print(item , end=" ")
        f.close()

    elif x==3:
        f = open("HammadExercise.txt","r+")
        for item in f:
            print(item , end=" ")
        f.close()

    else:
        print("enter valid input")

if k=="D" and i==1:
    logDiet(x)

elif k == "D" and i == 2:
    RetrieveDiet(x)

elif k == "E" and i == 1:
    logExercise(x)

elif k == "E" and i == 2:
    RetrieveExercise(x)

else:
    print("enter valid inputs")

