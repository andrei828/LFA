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


def delta(stare, litera):
	return DFA[(stare, litera)]

def delta_tilda(stare, cuvant):
	if len(cuvant) == 1:
		return delta(stare, cuvant[0])
	return delta_tilda(delta(stare, cuvant[0]), cuvant[1:])


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

# completare DFA-uri
alfabet = alfabet_1 + alfabet_2

for stare in stari_1:
	for litera in alfabet:
		DFA_1[('E', litera)] = 'E'
		DFA_1[(stare, litera)] = 'E'

for stare in stari_2:
	for litera in alfabet:
		DFA_2[('E', litera)] = 'E'
		DFA_2[(stare, litera)] = 'E'

#DFS
stari_vizitate = {}
for stare in stari:
	stari_vizitate[stare] = False

# print(este_limbaj_vid(stare_initala, DFA, stari_finale, stari_vizitate))

file.close()