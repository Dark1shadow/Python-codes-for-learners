
import random

count = 0

while True:
    number = random.randint(0, 10)
    print(number)
    count += 1
    if number == 0:
        break

print("Total numbers generated:", count)
