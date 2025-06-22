print("welcome to code of largest no. checking")

a = float(input("enter first number"))
b = float(input("enter second number"))
c = float(input("enter third number"))


if a>=b and a>=c:
    print(f"{a} is largest")
elif b>=a and b>=c:
    print(f"{b} is largest")
else:
    print(f"{c} is largest")