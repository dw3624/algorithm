T = int(input())
for tc in range(T):
	k = int(input())
	n = int(input())

	floors = [[0]*(n+1) for _ in range(k+1)]
	floors[0] = list(range(n+1))

	for r in range(1, k+1):
		for c in range(1, n+1):
			if c == 1:
				floors[r][c] = 1
			else:
				floors[r][c] = floors[r][c-1] + floors[r-1][c]
			
	# [print(floor) for floor in floors]
	print(floors[k][n])