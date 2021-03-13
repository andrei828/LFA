from collections import defaultdict

file = open('TranslatorStack.txt', 'r')
output = open('TranslatorStackResult.txt', 'w')

NODE, STACK, OUTPUT, LAMBDA = 0, 1, 2, '.'
'''
state (node, input, stack)

LNFA[(node, edge/letter, stack_top)] = set({(node, new_stack_top)})
'''

def is_in_LNFA(stare_i, litera, top_stiva):
	if not len(LNFA[(stare_i, litera, top_stiva)]) is 0:
		return True 
	del LNFA[(stare_i, litera, top_stiva)]
	return False


def lambda_inchidere(stare, stiva, iesire):
	return delta(stare, LAMBDA, stiva, iesire)

def lambda_handler(element):
	if element == LAMBDA:
		return ('')
	return (element)

'''
LNFA[(stare, litera, top_stiva)] = set({(stare, stiva_top_nou, litera_iesire)})
build result = set({(stare, stiva, iesire)})
'''
def delta(stare, litera, stiva, iesire):
	result = set()
	if is_in_LNFA(stare, litera, stiva[-1]):
		NODE, NEW_TOP_STACK, NEW_OUTPUT = 0, 1, 2
		stari = LNFA[(stare, litera, stiva[-1])]
		new_stack = stiva[:] if stiva[-1] == 'Z' else stiva[:-1]
		for stare in stari:
			result.add((stare[NODE], new_stack + lambda_handler(stare[NEW_TOP_STACK]), iesire[:] + lambda_handler(stare[NEW_OUTPUT])))
			
	return result

def delta_tilda(stare, cuvant, stiva, iesire):
	aux = set()
	rezultat = set()
	multime = delta(stare, cuvant[0], stiva, iesire) 

	for stare_lambda in lambda_inchidere(stare, stiva, iesire):
		multime = multime | delta(stare_lambda[NODE], cuvant[0], stare_lambda[STACK], stare_lambda[OUTPUT])
	
	for element in multime:
		aux = aux | lambda_inchidere(element[NODE], element[STACK], element[OUTPUT])
	multime = multime | aux

	if len(cuvant) == 1:
		return multime

	for stare_viitoare in multime:
		rezultat = rezultat | delta_tilda(stare_viitoare[NODE], cuvant[1:], stare_viitoare[STACK], stare_viitoare[OUTPUT])

	return rezultat


# multimea nodurilor (starilor)
numar_stari = int(file.readline().split()[0])
stari = set(file.readline().split())

# multimea tipurilor de muchii (alfabetul de intrare)
numar_litere = int(file.readline().split()[0])
alfabet = set(file.readline().split())

# alfabetul de iesire
numar_litere_iesire = numar_litere = int(file.readline().split()[0])
alfabet_iesire = set(file.readline().split())

# alfabetul stivei
numar_litere_stiva = numar_litere = int(file.readline().split()[0])
alfabet_stiva = set(file.readline().split())

# nod initial
stare_initala = file.readline().split()[0]

# multimea nodurilor finale
numar_stari_finale = int(file.readline().split()[0])
stari_finale = set(file.readline().split())

# implementare TranslatorStiva
#   0         1              2            3          4            5
# stare, litera_input, litera_output, top_stiva, stare_noua, top_stiva_nou
# LNFA[(stare, litera, top_stiva)] = set({(stare, stiva_top_nou, litera_iesire)})
LNFA = defaultdict(set)
numar_tranzitii = int(file.readline().split()[0])
for _ in range(numar_tranzitii):
	tranzitie = file.readline().split()
	LNFA[(tranzitie[0], tranzitie[1], tranzitie[3])].add((tranzitie[4], tranzitie[5], tranzitie[2]))

# multimea cuvintelor
cuvinte = []
numar_cuvinte = int(file.readline().split()[0])
for _ in range(numar_cuvinte):
	cuvant = file.readline().split()[0]
	stari_output = delta_tilda(stare_initala, cuvant, ('Z'), (''))
	print([stare[OUTPUT] for stare in stari_output if stare[NODE] in stari_finale and stare[STACK][-1] == 'Z'])
	

	# if delta_tilda(stare_initala, cuvant) & stari_finale:
	# 	output.write('DA\n')
	# else:
	# 	output.write('NU\n')

file.close()
output.close()

