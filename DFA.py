file = open('DFA.txt', 'r')
output = open('DFA_result', 'w')

def delta(stare, litera):
	if (stare, litera) in DFA:
		return DFA[(stare, litera)]
	return None

def delta_tilda(stare, cuvant):
	if len(cuvant) == 1:
		return delta(stare, cuvant[0])
	return delta_tilda(delta(stare, cuvant[0]), cuvant[1:])

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
DFA = {}
numar_tranzitii = int(file.readline().split()[0])
for i in range(numar_tranzitii):
	tranzitie = file.readline().split()
	DFA[(tranzitie[0], tranzitie[1])] = tranzitie[2]

# multimea cuvintelor
cuvinte = []
numar_cuvinte = int(file.readline().split()[0])
for cuvant in range(numar_cuvinte):
	cuvant = file.readline().split()[0]
	if delta_tilda(stare_initala, cuvant) in stari_finale:
		output.write('DA\n')
	else:
		output.write('NU\n')

file.close()
output.close()