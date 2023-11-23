a,b = map(int,input().split())
c = list(map(int,input().split()))
d = sorted(c)[:a]
sum = 0

for i in range(b):
  sum += d[i]

print(sum)
