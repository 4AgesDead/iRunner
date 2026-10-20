lenght = int(input())
array=list(map(int,input().split()))
inputer=list(map(int,input().split()))
num,place = [inputer[0]],inputer[1]

arrayfirst=array[:place-1]
arrayend=array[place-1:]
array = arrayfirst+num+arrayend

print(array)