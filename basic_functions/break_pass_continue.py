# break and pass
## in two functions the "for" loop is broken because both "break" and "pass" interrupt with the condition of the "if" function

number1 = 0
number2 = 0

for number1 in range(10):
    if number1 == 5:
        break
    print('Number: ' + str(number1))
print('out of the loop\n')

for number2 in range(10):
    if number2 == 5:
        pass
    print('Number: ' + str(number2))
print('out of the loop\n')


# continue
## in the "continue" function executes the entire "for" function ignoring the condition of the "if" function

number3 = 0

for number1 in range(10):
    if number1 == 5:
        continue
    print('Number: ' + str(number1))
print('out of the loop')