#!/usr/bin/env python3
# Author:Alex Li
'''
count = 0
while True:
    print("count:",count)
    count = count +1  #count +=1
    if count == 10:
        break
'''
count = 0
while count<10:
    print("count:",count)
    count +=1


'''
for i in range(0,10):
    print('i:',i)
    if i <3:
        print("loop ",i)
    else :
        # continue
        break
    print("hehe...")
'''
'''
for i in range(10):
    print('----------',i)
    for j in range(10):
        print(j)
        if j >5:
            break

'''
i = 1
print("-" * 50)
while i < 10:
    n = 1
    while n < 10:
        print("{:5d}".format(i * n),end='  ')
        n += 1
    print()
    i += 1
print("-" * 50)
