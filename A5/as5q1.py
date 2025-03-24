l=int(input())
r=int(input())
a=list()
for i in range(l,r+1):
    for j in range(l,r+1):
        a.append(i^j)
print(max(a))
