number = 0
number = int(input("Input value: "))

if (number%2==0) and (number!=0):
    print("The number is even and non-zero")
elif (number%2!=0):
    print("The number is odd and non-zero")
else:
    print("The number is even and equal to zero")