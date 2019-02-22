from collections import defaultdict

file = open('LNFA.txt', 'r')
output = open('LNFA_result', 'w')

def is_in_LNFA(stare_i, litera):
	if not len(LNFA[(stare_i, litera)]) is 0:
		return True 
	del LNFA[(stare_i, litera)]
	return False

def lambda_inchidere(stare):
	return delta(stare, '.')

def delta(stare, litera):
	if is_in_LNFA(stare, litera):
		return LNFA[(stare, litera)]
	return set()

def delta_tilda(stare, cuvant):
	rezultat = set()
	multime = delta(stare, cuvant[0]) 
	
	for stare_lambda in lambda_inchidere(stare):
		multime = multime | delta(stare_lambda, cuvant[0])
	# print(multime)
	
	aux = set()
	for element in multime:
		aux = aux | lambda_inchidere(element)
	multime = multime | aux

	if len(cuvant) == 1:
		return multime

	for stare_viitoare in multime:
		rezultat = rezultat | delta_tilda(stare_viitoare, cuvant[1:])

	return rezultat

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

# implementare LNFA
LNFA = defaultdict(set)
numar_tranzitii = int(file.readline().split()[0])
for i in range(numar_tranzitii):
	tranzitie = file.readline().split()
	LNFA[(tranzitie[0], tranzitie[1])].add(tranzitie[2])

# multimea cuvintelor
cuvinte = []
numar_cuvinte = int(file.readline().split()[0])
for i in range(numar_cuvinte):
	cuvant = file.readline().split()[0]
	if delta_tilda(stare_initala, cuvant) & stari_finale:
		output.write('DA\n')
	else:
		output.write('NU\n')

file.close()
output.close()

