a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("enter number"))
d=0
for i in range(1,a+1):
    if(i%b==0 and i%c==0):
        d+=1
print("answer is",d)        
