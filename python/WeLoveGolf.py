a = int(input())
b,c = map(int, input().split())

for i in range(b,c):
	if (i % a == 0):
		print('OK')
		break
	elif (i == c):
		print('NG')

