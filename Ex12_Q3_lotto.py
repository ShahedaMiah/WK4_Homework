import random

lottery = tuple(range(1, 51))
# 'range' generates an immutable sequence of numbers starting from the given start integer to the stop integer. Will start at 1 as that is the start integer given and stop at 50 as that is the 51st integer as we start counting from 0
print(lottery)\

count = 1
# this the number  of times the loop is completed
numbers_needed = 6
# number of loops allowed

print('\nLottery Numbers: ', end ="")
# 'end =""' prints the next print without a newline
while count <= numbers_needed:
    print(random.choice(lottery), end =" ")
    # space add inbetween the double quotes so there is a space between the result of each loop
    count += 1
    # add 1 to the count each time the loop is completed

