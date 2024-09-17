s=int(input("Enter starting point = "))
e=int(input("Enter ending point = "))
u=int(input("Enter updation choice = "))

print("Choice 'H' for horizantol")
print("Choise 'V' for vertical")

n=input("Enter your choice = ")

if (n=="H"):
    print("Choice 'F' for forward order")
    print("choice 'R' for reverse order")

    m=input("Enter your choice = ")

    if (m=="F"):
        for i in range(s,(e+1),u):
            print(i,end=' ')

    elif (m=="R"):
        for i in range(e,(s-1),-u):
            print(i,end=' ')

    else:
        print("Invalid Choice")

elif (n=="V"):
    print("Choice 'F' for forward order")
    print("choice 'R' for reverse order")

    m=input("Enter your choice = ")

    if (m=="F"):
        for i in range(s,(e+1),u):
            print(i)

    elif (m=="R"):
        for i in range(e,(s-1),-u):
            print(i)

    else:
        print("Invalid Choice")


else:
    print("Invalid choice")
