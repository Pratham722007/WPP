a=input("enter the string : ")
target=input("enter the character you want to find index of : ")
start=int(input("start : "))
end=int(input("end : "))

for i in range(end,start,-1):
     if(a[i:i+len(target)]==target):
        print(i)
        break
     else:
         print("value error")
        

 
