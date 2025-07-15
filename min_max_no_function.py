print (" welcome to min max without function")

arr  = [4,5,3,4,3,6,7,5,4,88,77,66,999,2000]

max = arr[0]
min = arr[0]

for num in arr:
    if num > max:
        max = num
    if num < min:
        min = num

print(f"max is {max}")
print(f"min is {min}")