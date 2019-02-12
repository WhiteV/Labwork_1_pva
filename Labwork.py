import random
i = 0
arr = ['Hello', 'Im Groot', 'Im Batman']
while i != 5:
    temp = random.randint(0, 2)
    print(arr[temp])
    i += 1
