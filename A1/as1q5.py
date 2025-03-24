a=int(input("enter no of students in your class:"))
stlist=['']
strev=['']
ch=''
for i in range(1,a+1):
    ch=input("enter name of student:")
    
    if(len(ch)>15):
        stlist.append(ch[:15:1])
        strev.append(ch[:15:-1])
    else:
        stlist.append(ch)
        strev.append(ch[::-1])

    
    ch=''
stlist.pop(0)
strev.pop(0)
print(stlist)
print(strev)





