import pycosat
from random import randint


num_var = 256
num_clauses = 181260

def generate_clause():
	a1 = randint(0,1)
	a2 = randint(0,1)
	a3 = randint(0,1)

	if(a1+a2+a3 == 0):
		return generate_clause()

	v1 = randint(1, 256)
	v2 = randint(1, 256)
	v3 = randint(1, 256)

	clause = []
	if(a1 == 0):
		clause.append(-v1)
	else:
		clause.append(v1)

	if(a2 == 0):
		clause.append(-v2)
	else:
		clause.append(v2)

	if(a3 == 0):
		clause.append(-v3)
	else:
		clause.append(v3)

	return clause

def cnf(x):
	cnf = []
	for i in range(x):
		cnf.append(generate_clause())
	return cnf

cnf = cnf(num_clauses)

f = open('minisat.in', 'w')
f.write('p cnf ' + str(num_var) + ' ' + str(num_clauses))
f.write('\n')

for x in cnf:
	f.write(" ".join(str(item) for item in x) + " 0\n")