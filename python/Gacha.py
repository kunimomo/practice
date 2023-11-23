import collections
a = int(input())
list = []

for b in range(a):
	i = input()
	list.append(i)

c = collections.Counter(list)
print(len(c))