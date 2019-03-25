file = open('DFA_complement.txt', 'r')
output = open('DFA_complement_result.txt', 'w')

def este_limbaj_vid(stare_initiala, DFA, stari_finale, stari_vizitate):
	if stare_initiala in stari_finale:
		return True

	este_vid = False
	stari_vizitate[stare_initiala] = True
	for (stare, litera) in DFA:
		if  este_vid is False and stare is stare_initiala and stari_vizitate[DFA[(stare, litera)]] is False:
			este_vid = este_limbaj_vid(DFA[(stare, litera)], DFA, stari_finale, stari_vizitate)

	return este_vid


def delta(stare, litera, DFA):
	return DFA[(stare, litera)]

def delta_tilda(stare, cuvant, DFA):
	if len(cuvant) == 1:
		return delta(stare, cuvant[0], DFA)
	return delta_tilda(delta(stare, cuvant[0]), cuvant[1:], DFA)

# multimea nodurilor
DFA_1 = {}
numar_stari = int(file.readline().split()[0])
stari_1 = set(file.readline().split())

# multimea tipurilor de muchii
numar_litere = int(file.readline().split()[0])
alfabet_1 = set(file.readline().split())

# nod initial
stare_initala_1 = file.readline().split()[0]

# multimea nodurilor finale
numar_stari_finale = int(file.readline().split()[0])
stari_finale_1 = set(file.readline().split())

# implementare DFA
numar_tranzitii_1 = int(file.readline().split()[0])
for i in range(numar_tranzitii_1):
	tranzitie = file.readline().split()
	DFA_1[(tranzitie[0], tranzitie[1])] = tranzitie[2]

# multimea nodurilor
DFA_2 = {}
numar_stari = int(file.readline().split()[0])
stari_2 = set(file.readline().split())

# multimea tipurilor de muchii
numar_litere = int(file.readline().split()[0])
alfabet_2 = set(file.readline().split())

# nod initial
stare_initala_2 = file.readline().split()[0]

# multimea nodurilor finale
numar_stari_finale = int(file.readline().split()[0])
stari_finale_2 = set(file.readline().split())

# implementare DFA
numar_tranzitii_2 = int(file.readline().split()[0])
for i in range(numar_tranzitii_2):
	tranzitie = file.readline().split()
	DFA_2[(tranzitie[0], tranzitie[1])] = tranzitie[2]


#		*** INTERSECTIE ***


# completare DFA-uri
alfabet = alfabet_1 | alfabet_2

for stare in stari_1:
	for litera in alfabet:
		DFA_1[('E', litera)] = 'E'
		if (stare, litera) not in DFA_1:
			DFA_1[(stare, litera)] = 'E'

for stare in stari_2:
	for litera in alfabet:
		DFA_2[('E', litera)] = 'E'
		if (stare, litera) not in DFA_2:
			DFA_2[(stare, litera)] = 'E'

# multimea starilor in intersectie
stari_inter = set()
for stare_1 in stari_1:
	for stare_2 in stari_2:
		stari_inter.add((stare_1, stare_2))

# starea initiala in intersectie
stare_init_inter = (stare_initala_1, stare_initala_2)

# multimea starilor finale in intersectie
stari_finale_inter = set()
for stare_1 in stari_finale_1:
	for stare_2 in stari_finale_2:
		stari_finale_inter.add((stare_1, stare_2))

# crearea grafului in intersectie
DFA_inter = {}
for stare_inter in stari_inter:
	for litera in alfabet:
		DFA_inter[(stare_inter, litera)] = (delta(stare_inter[0], litera, DFA_1), 
											delta(stare_inter[1], litera, DFA_2))

# DFS
stari_vizitate = {}
for stare in stari_inter:
	stari_vizitate[stare] = False

print(este_limbaj_vid(stare_init_inter, DFA_inter, stari_finale_inter, stari_vizitate))

file.close()




















