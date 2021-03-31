#A

a = int(input())
b = int(input())
print(max(a,b))

#B

y = int(input())
if (y % 4 == 0) and (y % 100 != 0) or (y % 400 == 0):
    print('YES')
else:
    print('NO')
    
#C
x = int(input())
y = int(input())
if x != 1 and y != 1 or x == 1 and y == 1:
    print("YES")
else:
    print("NO")
   
#D
x = int(input())

if x > 0:
    print(1)
if x < 0:
    print(-1)
if (x==0):
    print(0)
    
#E
a = int(input())
b = int(input())

if a > b:
    print(1)
if a < b:
    print(2)
if a == b:
    print(0)
