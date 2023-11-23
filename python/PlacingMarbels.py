a = input()
b = a[-1]
c = a[-2]
d = a[-3]
sum = 0
list = []
list.append(b)
list.append(c)
list.append(d)

for i in list:
  if (i == '1'):
    sum += 1

print(sum)