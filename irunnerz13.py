A=int(input())
B=int(input())
i=A
while i!=B+1:
    if str(i)[0]==str(i)[1]==str(i)[2]!=str(i)[3] or str(i)[1]==str(i)[2]==str(i)[3]!=str(i)[0] or str(i)[0]==str(i)[3]==str(i)[2]!=str(i)[1] or str(i)[0]==str(i)[1]==str(i)[3]!=str(i)[2] :
        print(i)
    i+=1