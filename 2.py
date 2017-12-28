x = int(input())
if x % 2 == 0:
	if x > 2 and x < 6:
		print('Not Weird')
	elif x > 6 and x < 21:
		print('Weird')
	else:
		print('Not Weird')
else:
	print('Weird')