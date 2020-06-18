import random
def rolldicey(rolls):
    for i in range(0,rolls):
        number=random.randint(1,6)
        print("---")
        print("-"+str(number)+"-")
        print("---")
def menu():
    print("1.Roll a die")
    print("2.Roll dice n number of times") 
    print(".............")
    print("3.exit program")
    print()
    choice=int(input("enter your choice: "))

    if (choice==1):
        rolldicey(1)

    if (choice==2):
        rolls=int(input("How many rolls do u want:"))
        rolldicey(rolls)
        

    if (choice==3):
        exit()        



menu()    