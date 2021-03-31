
#A
a = [int(i) for i in input().split()]

print(min(a[0], a[1], a[2], a[3]))

#B
a = [int(i) for i in input().split()]
print(pow(a[0], a[1]))

#C
def xor(x, y):
    if (x == 1 and y == 0) or (x == 0 and y == 1): return 1
    return 0
x, y = map(int, input().split())
print(xor(x, y))
