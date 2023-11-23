i = list(map(int, input().split()))

if (i[1] > i[0] or i[1] == i[0]):
	print('unsafe')
else:
	print('safe')