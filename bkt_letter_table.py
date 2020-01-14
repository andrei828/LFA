with open('input_bkt_letter_table.txt', 'r') as document:
	n, m = [int(_) for _ in next(document).split()]
	matrix = [ [element for element in positions.split()] 
			   for positions in document ]

frequency = set()
final_solution = []
current_solution = []
possible_turns = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def print_matrix(matrix):
	for row in matrix:
		for element in row:
			print(element, end=' ')
		print()

def print_solution(solution):
	print("{} moves".format(len(solution)))
	for coord in solution:
		print(matrix[coord[0]][coord[1]], end=' ')
	print()

def paths(pos_x, pos_y):
	paths = []
	for turn in possible_turns:
		# print("y: ", pos_y, "\tx: ", pos_x, "\t", turn)
		if (pos_y + turn[0] < n and pos_y + turn[0] >= 0 and
			pos_x + turn[1] < m and pos_x + turn[1] >= 0 and
			matrix[pos_y + turn[0]][pos_x + turn[1]] not in frequency):
			
			paths.append(turn)
	
	return paths

def bkt_walk(pos_x, pos_y):
	global final_solution, current_solution, frequency

	frequency.add(matrix[pos_y][pos_x])
	current_solution.append((pos_y, pos_x))

	possible_paths = paths(pos_x, pos_y)
	
	if len(possible_paths) == 0 and len(current_solution) > len(final_solution):
		final_solution = current_solution.copy()
		
	else:
		for path in possible_paths:
			bkt_walk(pos_x + path[1], pos_y + path[0])
	
	current_solution.pop()
	frequency.discard(matrix[pos_y][pos_x])

bkt_walk(0, 0)
print_solution(final_solution)