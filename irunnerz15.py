n= int(input())
i=2
和=0
行=''
while(i<=n):
    if i ==2:行+=str(i-1)+'*'+str(i)
    else:行+='+'+str(i-1)+'*'+str(i)
    和+=(i-1)*i
    i+=1
print(行+'='+str(和))