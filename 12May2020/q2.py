a=int(input("enter number"))
b=int(input("enter number"))
l=0
gcd=0
if a<=b:
    l=a;
else:
    l=b
if a==1 and b==1:
    gcd=1
else:
    for i in range(l,0,-1):
        if a%i==0 and b%i==0:
            gcd=i
            break
print("gcd of number is:",gcd)
