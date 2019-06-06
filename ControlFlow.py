"""
Basics of the;
    + if-statement
    + try-statement, not control flow but life bruh
    + while-statement
    + for-loop
"""

#if statement
num = 7
if num % 2 == 0:
    if num < 0:
        print("num is even and negative")
    elif num == 0:
        print("num is 0")
    else:
        print("num is even and positive")
else:
    if num < 0:
        print("num is odd and negative")
    else:
        print("num is odd and positive")

#getting input
raw = input("Enter anything: ")

#printing type of raw, always a string
print(type(raw))

#try statement
#checking if type of raw is actually an integer or not
try:
    val = int(raw)
    if val >= 0 or val < 0:
        print("You have entered a number")
except ValueError:
    print("You entered a string")

#checks variable if it's a digit
print(raw.isdigit())

#while statement, 'else' is optional and always executes unless a 'break' statement is used
i = 1
while i <= 10:
    print("i is {0}".format(i))
    i = i + 1
else:
    print("The while statement has ended")

#for loop, 'else' is also optional
for i in range(1, 11):
    if i == 3:
        continue
    print("{0}*{0} = {1}".format(i, i*i))
    if i == 6:
        break
else:
    print("The for loop ended")
