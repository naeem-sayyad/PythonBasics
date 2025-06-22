print("fibonacci series code - eternal blez")

print("Fibonacci Series Generator")

n = int(input("How many numbers to print? "))

a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c


