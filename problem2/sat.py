from satispy import Variable, Cnf
from satispy.solver import Minisat
from random import randint
v = []


for i in range(256):
	v.append(Variable('v' + str(i)))

k = [1] * 256

def random_clause():

	a1 = randint(0,1)
	a2 = randint(0,1)
	a3 = randint(0,1)

	if(a1+a2+a3 == 0):
		return random_clause()

	v1 = randint(0, 255)
	v2 = randint(0, 255)
	v3 = randint(0, 255)

	ev1; ev2; ev3;


	if(a1 == 0):
		ev1 = -v[v1]
	else:
		ev1 = v[v1]

	if(a2 == 0):
		ev2 = -v[v2]
	else:
		ev2 = v[v2]

	if(a3 == 0):
		ev3 = -v[v3]
	else:
		ev3 = v[v3]

	return (ev1 | ev2 | ev3)

def build_cnf(clauses):
	expr = clauses[0]
	for i in range(1, len(clauses)):
		expr = expr & clauses[i]
	return expr



exp = (-v[0] | v[2]) & v[3]

solver = Minisat()
solution = solver.solve(exp)

# if solution.success:
# 	print("hello")