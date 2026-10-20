n=int(input())
x=float(input())
i=0
sum=0
while(i<=n):
    a=float(input())
    if i ==n:
        sum+=a
    else:
        sum+=a*(x**(n-i))
    i+=1
print(round(sum,2))