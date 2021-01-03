from collections import deque

WEIGHT, VALUE = 0, 1
PROFIT, LEVEL = 2, 3

def greedy_sol(arr, n, max_weight, items):

	if arr[WEIGHT] >= max_weight:
		return 0

	greedy_profit = arr[PROFIT]
	print(greedy_profit)
	lvl = arr[LEVEL] + 1
	total_weight = arr[WEIGHT]

	while lvl < n and total_weight + items[lvl][WEIGHT] <= max_weight:
		total_weight += items[lvl][WEIGHT]
		greedy_profit += items[lvl][VALUE]
		lvl += 1

	if lvl < n:
		greedy_profit += int((max_weight - total_weight) * 
							 items[lvl][VALUE] / items[lvl][WEIGHT])

	return greedy_profit

def knapsack(max_weight, items, n):
	items.sort(key=lambda item: -1.0*item[VALUE] / item[WEIGHT])
	queue = deque()
	u, v = [-99999 for i in range(4)], [-99999 for i in range(4)]
	
	u[LEVEL] = -1
	u[PROFIT] = u[WEIGHT] = 0
	queue.append(u[:])

	max_profit = 0
	while len(queue) > 0:

		u = queue.popleft()

		if u[LEVEL] == -1:
			v[LEVEL] = 0

		if u[LEVEL] == n - 1:
			continue

		v[LEVEL] = u[LEVEL] + 1

		v[WEIGHT] = u[WEIGHT] + items[v[LEVEL]][WEIGHT]
		v[PROFIT] = u[PROFIT] + items[v[LEVEL]][VALUE]

		if v[WEIGHT] <= max_weight and v[PROFIT] > max_profit:
			max_profit = v[PROFIT]

		v[VALUE] = greedy_sol(v, n, max_weight, items)
		
		if v[VALUE] > max_profit:
			queue.append(v[:])

		v[WEIGHT] = u[WEIGHT]
		v[PROFIT] = u[PROFIT]
		v[VALUE] = greedy_sol(v, n, max_weight, items)

		if v[VALUE] > max_profit:	
			queue.append(v[:])
		
	return max_profit

with open('input_knapsack.txt', 'r') as document:
	n = int(next(document).split()[0])
	items = [data.split() for data in document]

for item in items:
	item[WEIGHT], item[VALUE] = float(item[WEIGHT]), int(item[VALUE])

print(knapsack(10, items, n))



















