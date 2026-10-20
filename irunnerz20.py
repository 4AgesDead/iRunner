inputer=list(map(int,input().split()))
N,K = inputer[0],inputer[1]
pin=['I']*N
for i in range(K):
    inputer=list(map(int,input().split()))
    li,ri = inputer[0],inputer[1]
    for j in range(li-1,ri):
        pin[j]='.'
realpin=''
for i in pin:
    realpin+=i
print(realpin)
