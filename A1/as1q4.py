items=[0]
rem0=[0]
rem1=[0]
rem2=[0]
rem3=[0]
rem4=[0]

for i in range(1,1001):
    items.append(i)
items.pop(0)
for i in range(1,1001):
    if(i%5==0):
        rem0.append(i)
    if(i%5==1):
        rem1.append(i)
    if(i%5==2):
        rem2.append(i)
    if(i%5==3):
        rem3.append(i)
    if(i%5==4):
        rem4.append(i)
rem0.pop(0)
rem1.pop(0)
rem2.pop(0)
rem3.pop(0)
rem4.pop(0)
remlist=rem0+rem1+rem2+rem3+rem4
remlist.sort()
if(remlist==items):
    print("equivalence relation")
else:
    print("not equivalence relation")
