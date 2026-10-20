n=int(input())
array=[]
gay=[]
for i in range(n):
    gay=[]
    for j in range(i, -(n-i),-1):
        gay.append(abs(j))
    array.append(gay)
print(array)
