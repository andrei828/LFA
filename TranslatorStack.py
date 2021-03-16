from collections import defaultdict

'''
O stare este formata din (valoare_nod, stiva, cuvant_iesire)

Dictionarul 'Translator' are chei de forma (valoare_nod, litera, varf_stiva) 
si returneaza un set de valori (valoare_nod, varf_stiva_nou, litera_iesire)
Type: Translator[(valoare_nod, litera, varf_stiva)] = set({(valoare_nod, varf_stiva_nou, litera_iesire)})

Astfel, in functia 'delta' plecam de la starea din nodul 'x' cu varful stivei 'y' si prin
dictionarul 'Translator' obtinem toate starile posibile ce permit acest input. Pentru
fiecare element din multime, cream o noua stare in care scoatem elementul 'y' din stiva 
si il inlocuim cu noul varf specific nodului.

Functia delta_tilda este metoda recursiva prin care translatam 
intregul input folosindu-ne de functia delta dar si alte 
functii ajutatoare (lambda_inchidere si este_in_Translator)
'''

file = open('TranslatorStack.txt', 'r')
output = open('TranslatorStackResult.txt', 'w')

NODE, STACK, OUTPUT, LAMBDA = 0, 1, 2, '.'

def este_in_Translator(stare, litera, top_stiva):
	if not len(Translator[(stare, litera, top_stiva)]) is 0:
		return True 
	del Translator[(stare, litera, top_stiva)]
	return False

def lambda_inchidere(stare, stiva, iesire):
	lambda_multime = delta(stare, LAMBDA, stiva, iesire)
	result = lambda_multime
	lungime = len(result)
	while True:
		for stare_lambda in lambda_multime:
			result = result | delta(stare_lambda[NODE], LAMBDA, stare_lambda[STACK], stare_lambda[OUTPUT])
		
		if len(result) == lungime:
			break
		lungime = len(result)
	return result

def lambda_handler(element):
	if element == LAMBDA:
		return ('')
	return (element)

'''
Translator[(stare, litera, top_stiva)] = set({(stare, stiva_top_nou, litera_iesire)})
build result = set({(stare, stiva, iesire)})
'''
def delta(stare, litera, stiva, iesire):
	result = set()

	if este_in_Translator(stare, litera, stiva[-1]):
		NODE, NEW_TOP_STACK, NEW_OUTPUT = 0, 1, 2

		# starile cu legaturi la starea curenta
		stari = Translator[(stare, litera, stiva[-1])]
		
		# verificam daca 'Z' este varful stivei
		noua_stiva = stiva[:] if stiva[-1] == 'Z' else stiva[:-1]

		# construim noile stari
		for stare in stari:
			result.add((
				stare[NODE], 
				noua_stiva + lambda_handler(stare[NEW_TOP_STACK]),
				iesire[:] + lambda_handler(stare[NEW_OUTPUT])
			))

	return result

def delta_tilda(stare, cuvant, stiva, iesire):
	aux = set()
	rezultat = set()

	# starile obtinue de la prima litera din input
	multime = delta(stare, cuvant[0], stiva, iesire) 
	
	lungime_multime = len(multime)

	while True:
		# calculam delta si pentru lambda inchiderea primei stari
		for stare_lambda in lambda_inchidere(stare, stiva, iesire):
			multime = multime | delta(stare_lambda[NODE], cuvant[0], stare_lambda[STACK], stare_lambda[OUTPUT])
		
		# calculam lambda inchiderea de la fiecare stare
		# obtinuta dupa parsarea primei litere din input
		for element in multime:
			aux = aux | lambda_inchidere(element[NODE], element[STACK], element[OUTPUT])
		multime = multime | aux

		if lungime_multime == len(multime):
			break

		lungime_multime = len(multime)
		
	# daca cuvantul are doar 
	# o litera returnam setul
	if len(cuvant) == 1:
		return multime

	# pentru fiecare stare obtinuta 
	# dupa operatiile de mai sus,
	# translatam restul inputului
	# in mod recursiv
	for stare_viitoare in multime:
		rezultat = rezultat | delta_tilda(stare_viitoare[NODE], cuvant[1:], stare_viitoare[STACK], stare_viitoare[OUTPUT])
	
	return rezultat

'''
. 1 SbSa
a . SbS
. . SbS
'''

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

#   0         1              2            3          4            5
# stare, litera_input, litera_output, top_stiva, stare_noua, top_stiva_nou
# implementare TranslatorStiva
Translator = defaultdict(set)
numar_tranzitii = int(file.readline().split()[0])
for _ in range(numar_tranzitii):
	tranzitie = file.readline().split()
	Translator[(tranzitie[0], tranzitie[1], tranzitie[3])].add((tranzitie[4], tranzitie[5], tranzitie[2]))

# multimea cuvintelor
cuvinte = []
numar_cuvinte = int(file.readline().split()[0])
for _ in range(numar_cuvinte):
	cuvant = file.readline().split()[0]
	stari_output = delta_tilda(stare_initala, cuvant, ('Z'), (''))
	print('---------------------------------------')
	print([stare[OUTPUT] for stare in stari_output if stare[NODE] in stari_finale])
	# print([stare[OUTPUT] for stare in stari_output if stare[NODE] in stari_finale and stare[STACK][-1] == 'Z'])

file.close()
output.close()

