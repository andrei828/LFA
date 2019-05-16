def write_non_terminals(matrix, line, col, CFG_help, word):
	for i in range(line + 1, len(word)):
		for x, y in zip(matrix[len(word) - i + line][col], matrix[i][col + i - line]):
			add_element(matrix, x, y, line, col, CFG_help, word, i)
		
def add_element(matrix, tuple1, tuple2, line, col, CFG_help, word, i):
	if tuple1[0]+tuple2[0] in CFG_help:
		for element in CFG_help[tuple1[0] + tuple2[0]]:
			matrix[line][col].add((
					element, len(word) - i + line, 
					col, i, col + i - line))

def cyk(matrix, CFG, CFG_help, word):
	for col in range(len(word)):
		for element in CFG_help[word[col]]:
			matrix[len(word)-1][col].add((element, 0, 0, 0, 0))

	for line in range(len(word) - 2, -1, -1):
		for col in range(line + 1):
			write_non_terminals(matrix, line, col, CFG_help, word)

file = open("input.txt", "r")
text_file = file.read().split("\n")

CFG = {}
CFG_help = {}
word = text_file[0]
word = word.split()
word = list(word)[0]

for relation in text_file[1:]:
	rel = relation.split()
	if rel[0] not in CFG:
		CFG[rel[0]] = []
	
	terminal_string = ''.join(rel[1:])
	CFG[rel[0]].append(terminal_string)

	if terminal_string not in CFG_help:
		CFG_help[terminal_string] = []
	CFG_help[terminal_string].append(rel[0])

curr_col_size = len(word)
matrix = [[set()  for i in range(0, j + 1)]for j in range(curr_col_size)]
cyk(matrix, CFG, CFG_help, word)

for i in matrix:
	print([j for j in i])
	


