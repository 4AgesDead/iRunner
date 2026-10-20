n = input().strip()
n = n.zfill(4)
print(1 if n == n[::-1] else 0)