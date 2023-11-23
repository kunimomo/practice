i = list(map(int, input().split()))

while (i[0] > 0 or i[2] > 0):
	i[2] = i[2] - i[1]
	if (i[2] <= 0):
		print('Yes')
		break
	i[0] = i[0] - i[3]
	if (i[0] <= 0):
		print('No')
		break
	