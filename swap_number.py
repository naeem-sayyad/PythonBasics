print("welcome to swap number code by EternalBlez")

x =float(input("enter first number: "))
y =float(input("enter second number: "))

print("do you want to swap the numbers? Enter Y/N")
p = input("enter Y/N")
if p.upper() == "Y":
    z=x
    x=y
    y=z
    print("the first number is now", x)
    print("the second number is now", y)
else:
    print("code ended")

