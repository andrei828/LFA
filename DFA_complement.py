class Automat:
    def __init__(self, stari, alfabet, DFA, stare_initiala, stari_finale):
        self.DFA = DFA
        self.stari = stari
        self.stari.add(None)
        self.alfabet = alfabet
        self.stari_finale = stari_finale
        self.stare_initiala = stare_initiala

def delta(stare, litera, DFA):
	return DFA[(stare, litera)]

def este_limbaj_vid(automat):
    stiva = []
    stari_vizitate = { None: True }

    for stare in automat.stari:
        stari_vizitate[stare] = False
    
    stiva.append(automat.stare_initiala)

    while stiva:
        top = stiva.pop()

        if not stari_vizitate[top]:
            if top in automat.stari_finale:
                return False
            stari_vizitate[top] = True

        for litera in automat.alfabet:
            if not stari_vizitate[automat.DFA[(top, litera)]]:
                stiva.append(automat.DFA[(top, litera)])

    return True

def completare_automat(automat):
	for stare in automat.stari:
		for litera in automat.alfabet:
			automat.DFA[(None, litera)] = None
			if (stare, litera) not in automat.DFA:
				automat.DFA[(stare, litera)] = None

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
    # complementelor automatelor
    complement_automat_1 = complement(automat_1)
    complement_automat_2 = complement(automat_2)

    # reuniune alfabet
    automat_1.alfabet = automat_1.alfabet | automat_2.alfabet
    automat_2.alfabet = automat_1.alfabet
    
    # completare automate
    completare_automat(automat_1)
    completare_automat(automat_2)
    completare_automat(complement_automat_1)
    completare_automat(complement_automat_2)
    
	# verificarea limbajului prin intersectia automatelor
    if (este_limbaj_vid(intersectie(automat_1, complement_automat_2))
        and este_limbaj_vid(intersectie(complement_automat_1, automat_2))):
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









