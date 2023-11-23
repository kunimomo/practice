a,b,c = map(int,input().split())
d = list(map(int,input().split()))
e = list(map(int,input().split()))
f = c
count = 0

while c > 0:
  if(len(d) > 0):
    if((c-d[0]) >= 0):
      c = c - d[0]
      del d[0]
      count += 1
  if(len(e) > 0):
    if((c-e[0]) >= 0):
      c = c - e[0]
      del e[0]
      count += 1
  if(f == c):
    break
    
print(count)