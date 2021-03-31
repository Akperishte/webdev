#A
n = int(input())
value = 1
cur_sq = value * value

while cur_sq <= n:
	print(str(cur_sq) + ' ')
	value = value + 1
	cur_sq = value*value
  
  #B
  n = int(input())
i = 2
while n % i != 0:
    i += 1
print(i)

#C
n = int(input())
pow = 1
while pow <= n:
	print(str(pow) + ' ')
	pow = pow * 2
  
 #D
a = int(input())
n = 2
while a != n and a >= n:
	n = n * 2
if a == n or a == 1:
	print('YES')
else:
	print('NO')
  
 #E
n = int(input())
pow = 1
k = 0

while pow < n:
	pow <<=1
	k = k+1
print(k)

  
