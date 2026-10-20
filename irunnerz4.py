a = int(input())
b = int(input())
c = int(input())

if a + b <= c or a + c <= b or b + c <= a:
    print('impossible')
else:
    sides = sorted([a, b, c])
    x, y, z = sides[0], sides[1], sides[2]
    if x*x + y*y == z*z:
        print('rectangular')
    elif x*x + y*y < z*z:
        print('obtuse')
    else:
        print('acute')
