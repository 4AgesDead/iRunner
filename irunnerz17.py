from math import factorial
n=int(input())
k=int(input())
print(factorial(n)/(factorial(k)*factorial(n-k)))