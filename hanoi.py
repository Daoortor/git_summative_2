def hanoi(n, start=1, end=3):
	if n == 1:
		return [(start, end)]
	else:
		if set(start, end) == set(1, 2):
			free = 3
		elif set(start, end) == set(1, 3):
			free = 2
		else:
			free = 1
		return hanoi(n - 1, start, free) + [(start, end)] + hanoi(n - 1, free, end)
