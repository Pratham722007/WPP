a=input("enter the string : ")
target=input("enter the character you want to count : ")
start=int(input("start : "))
end=int(input("end : "))
count=0
for i in range(start,end):
    if(a[i:i+len(target)]==target):
        count+=1

 
print(count)