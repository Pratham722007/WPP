import random
count=0
rowofzero=[0]
random_integers = [random.randint(0, 1) for _ in range(100)]
print(random_integers)
for i in range(0,100):
    if random_integers[i] == 0:
        count+=1
    else:
        rowofzero.append(count)
        count=0
    
print("the maximum number of zeroes in a row is ",max(rowofzero))  
