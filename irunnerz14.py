linia=input()
G=[]
for i in range(len(linia)):
    if linia[i]=='f':
        G.append(i)
if len(G)==1:
    print(G[0])
if len(G)>=2:
    print(G[0], G[-1])