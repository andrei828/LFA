class Automat:
	def __init__(self, stari, alfabet, DFA, stare_initiala, stari_finale):
		self.DFA = DFA
		self.stari = stari
		self.alfabet = alfabet
		self.stari_finale = stari_finale
		self.stare_initiala = stare_initiala

def delta(stare, litera, DFA):
	return DFA[(stare, litera)]

def delta_tilda(stare, cuvant, DFA):
	if len(cuvant) == 1:
		return delta(stare, cuvant[0], DFA)
	return delta_tilda(delta(stare, cuvant[0]), cuvant[1:], DFA)

# complete function ****
def este_limbaj_vid(automat, stari_vizitate):
	if automat.stare_initiala in automat.stari_finale:
		return False

	este_vid = True
	stari_vizitate[automat.stare_initiala] = True
	for (stare, litera) in automat.DFA:
		if (este_vid is True and stare is automat.stare_initiala 
			and stari_vizitate[automat.DFA[(stare, litera)]] is False):
			
			automat.stare_initiala = automat.DFA[(stare, litera)]
			este_vid = este_limbaj_vid(automat, stari_vizitate)

	return este_vid

def completare_automat(automat):
	for stare in automat.stari:
		for litera in automat.alfabet:
			automat.DFA[('E', litera)] = 'E'
			if (stare, litera) not in automat.DFA:
				automat.DFA[(stare, litera)] = 'E'

def complement(automat):
	stari_finale = automat.stari - automat.stari_finale
	return Automat(automat.stari, automat.alfabet, automat.DFA, automat.stare_initiala, stari_finale)

def intersectie(automat_1, automat_2):
	# multimea starilor in intersectie
	stari_inter = set()
	for stare_1 in automat_1.stari:
		for stare_2 in automat_2.stari:
			stari_inter.add((stare_1, stare_2))

	# starea initiala in intersectie
	stare_init_inter = (automat_1.stare_initiala, automat_2.stare_initiala)

	# multimea starilor finale in intersectie
	stari_finale_inter = set()
	for stare_1 in automat_1.stari_finale:
		for stare_2 in automat_2.stari_finale:
			stari_finale_inter.add((stare_1, stare_2))

	# crearea grafului in intersectie
	DFA_inter = {}
	for stare_inter in stari_inter:
		for litera in automat_1.alfabet:
			DFA_inter[(stare_inter, litera)] = (delta(stare_inter[0], litera, automat_1.DFA), 
												delta(stare_inter[1], litera, automat_2.DFA))

	return Automat(stari_inter, automat_1.alfabet, DFA_inter, stare_init_inter, stari_finale_inter)

def echivalenta(automat_1, automat_2):
	# completare automate
	automat_1.alfabet = automat_1.alfabet | automat_2.alfabet
	automat_2.alfabet = automat_1.alfabet
	completare_automat(automat_1)
	completare_automat(automat_2)

	# complementelor automatelor
	complement_automat_1 = complement(automat_1)
	complement_automat_2 = complement(automat_2)

	# verificarea limbajului prin intersectia automatelor
	stari_vizitate1 = {}
	stari_vizitate2 = {}
	if (este_limbaj_vid(intersectie(automat_1, complement_automat_2), stari_vizitate1) 
		and este_limbaj_vid(intersectie(complement_automat_1, automat_2), stari_vizitate2)):
		return True
	return False

# deschidere fisier
file = open('DFA_complement.txt', 'r')
output = open('DFA_complement_result.txt', 'w')

# multimea nodurilor
DFA_1 = {}
numar_stari = int(file.readline().split()[0])
stari_1 = set(file.readline().split())

# multimea tipurilor de muchii
numar_litere = int(file.readline().split()[0])
alfabet_1 = set(file.readline().split())

# nod initial
stare_initiala_1 = file.readline().split()[0]

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
stare_initiala_2 = file.readline().split()[0]

# multimea nodurilor finale
numar_stari_finale = int(file.readline().split()[0])
stari_finale_2 = set(file.readline().split())

# implementare DFA
numar_tranzitii_2 = int(file.readline().split()[0])
for i in range(numar_tranzitii_2):
	tranzitie = file.readline().split()
	DFA_2[(tranzitie[0], tranzitie[1])] = tranzitie[2]

#inchidere fisiere
file.close()
output.close()

automat_1 = Automat(stari_1, alfabet_1, DFA_1, stare_initiala_1, stari_finale_1)
automat_2 = Automat(stari_2, alfabet_2, DFA_2, stare_initiala_2, stari_finale_2)

print(echivalenta(automat_1, automat_2))









