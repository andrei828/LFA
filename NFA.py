from collections import defaultdict

file = open('NFA.txt', 'r')
output = open('NFA_result', 'w')

def is_in_DFA(stare_i, litera):
	if not len(DFA[(stare_i, litera)]) is 0:
		return True 
	del DFA[(stare_i, litera)]
	return False

def delta(stare, litera):
	if is_in_DFA(stare, litera):
		return DFA[(stare, litera)]
	return set()

def delta_tilda(stare, cuvant):
	stari_urmatoare = delta(stare, cuvant[0])
	
	if len(cuvant) == 1:
		return stari_urmatoare

	multime = set()
	for stare_urmatoare in stari_urmatoare:
		submultime = set(delta_tilda(stare_urmatoare, cuvant[1:]))
		multime = multime | submultime
	return multime

# multimea nodurilor
numar_stari = int(file.readline().split()[0])
stari = set(file.readline().split())

# multimea tipurilor de muchii
numar_litere = int(file.readline().split()[0])
alfabet = set(file.readline().split())

# nod initial
stare_initala = file.readline().split()[0]

# multimea nodurilor finale
numar_stari_finale = int(file.readline().split()[0])
stari_finale = set(file.readline().split())

# implementare DFA
DFA = defaultdict(set)
numar_tranzitii = int(file.readline().split()[0])
for i in range(numar_tranzitii):
	tranzitie = file.readline().split()
	DFA[(tranzitie[0], tranzitie[1])].add(tranzitie[2])

# multimea cuvintelor
cuvinte = []
numar_cuvinte = int(file.readline().split()[0])
for cuvant in range(numar_cuvinte):
	cuvant = file.readline().split()[0]
	if delta_tilda(stare_initala, cuvant) & stari_finale:
		output.write('DA\n')
	else:
		output.write('NU\n')

file.close()
output.close()

