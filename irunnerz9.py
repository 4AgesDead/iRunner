n=int(input())
sum=0
i=0
while i<n:
    i+=1
    sum+=((-1)**(i+1))/i
print(round(sum,6))