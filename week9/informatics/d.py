
#A
n = int(input())
l = list(input().split())
for i in range(0, n):
    if i % 2 == 0:
        print(l[i], end=" ")
        
#B
n = int(input())
l = list(input().split())
for i in range(0, n):
    if int(l[i]) % 2 == 0:
        print(l[i], end=" ")
        
#C

n = int(input())
l = list(input().split())
cnt = 0
for i in range(0, n):
    if int(l[i]) > 0:
        cnt += 1
print(cnt)

#D
n = int(input())
l = list(input().split())
cnt = 0
for i in range(1, n):
    if int(l[i]) > int(l[i-1]):
        cnt += 1
print(cnt)

#E
n = int(input())
list = input().split()
cnt = 0
for i in range(1, n):
    if (int(list[i]) <= 0 and int(list[i - 1]) <= 0) or (int(list[i]) > 0 and int(list[i - 1]) > 0):
        cnt += 1
if (cnt > 0):
    print("YES")
else:
    print("NO")
