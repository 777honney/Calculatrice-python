print("Voici le calculateur")
operation=input("Choisi un une opération (+,-,*/): ")

if operation == "+" :
    a= float(input("choisi un nombre : "));
    b=float(input("choisi un second nombre : "));
    c=a+b
    print(c)

elif operation == "-" :
    a= float(input("choisi un nombre : "));
    b=float(input("choisi un second nombre : "));
    c=a-b
    print(c)

elif operation == "/" :
    a= float(input("choisi un nombre : "));
    b=float(input("choisi un second nombre : "));
    c=a/b
    print(c)

elif operation == "*" :
    a= float(input("choisi un nombre : "));
    b=float(input("choisi un second nombre : "));
    c=a*b
    print(c)
else :
    print("???")
