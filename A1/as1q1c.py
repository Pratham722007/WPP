items=['a']
ch=''
k=0
for i in range(98,123):
    for j in range(0,i-96):
        ch=ch+chr(i)
        k+=1
        if(k==i-96):
            items.append(ch)
            k=0
            ch=''

        
print(items)