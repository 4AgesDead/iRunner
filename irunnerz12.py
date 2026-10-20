A = int(input())
B = int(input())
if A > B:
    A, B = B, A
i=A
while i != B+1:
    if str(i) == str(i)[::-1]:
        print(i)
    i+=1
