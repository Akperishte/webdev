
#A
a = int(input())
b = int(input())
for i in range(a, b + 1):
    if i%2 == 0:
        print(str(i) + ' ')
     
#B
a = int(input())
b = int(input())
c = int(input())
d = int(input())

for i in range(a, b+1):
	if i % d == c:
		print(str(i) + ' ')
    
#C
import math
a = int(input())
b = int(input())
sqrta = int(math.sqrt(a) + 1)
sqrtb = int(math.sqrt(b))
for x in range(sqrta, sqrtb + 1):
   print(x * x)
    
#G
x = int(input())
i = 2
while x % i != 0:
    i += 1
print(i)

#H
x = int(input())

for i in range(1,x+1):
    if x % i ==0:
        print(str(i) + ' ')
      
 #I
x = int(input())
count = 0
i = 1
while i * i < x:
	if x % i == 0:
		count += 2
	i += 1
if i * i == x:
	count += 1
print(count)

#J
sum = 0

for i in range(1, 101):
	a = int(input())
	sum = sum + a
print(sum)

#K

sum =0
n = int(input())

for i in range(1,n+1):
    a = int(input())
    sum = sum + a
print(sum)

#M
n = int(input())
null = 0
for i in range(1,n+1):
    a = int(input())
    if a == 0:
        null = null + 1
        print(null)
        
