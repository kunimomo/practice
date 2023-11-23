a,b = map(int, input().split())
i = list(map(int, input().split()))

for j in range(b):
  a = a - i[j]
 

if (a >= 0):
  print(a)
else:
  print(-1)


