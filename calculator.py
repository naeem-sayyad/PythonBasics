print("welcome to the calculator by naeem sayyad")

a = float(input("enter first number"))
b = float(input("enter second number"))

print("enter the math operation number, ex - 1 for add, 1-add, 2-subtract, 3-multiply, 4-divide")
f = int(input("enter the number: "))
if f == 1:
       add = a + b
       print(add)
elif f == 2:
       sub = a - b
       print(sub)
elif f == 3:
       multi = a*b
       print(multi)
elif f == 4:
       div = a/b
       print(div)
else:
       print("invalid entry")

