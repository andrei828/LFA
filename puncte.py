import sys
import numpy as np
from math import sqrt, pi, cos, acos
import matplotlib.pyplot as plt

def CCW(p1, p2, p3):
	if ( (p3[1] - p1[1]) * (p2[0] - p1[0]) >=
		 (p2[1] - p1[1]) * (p3[0] - p1[0]) ):
		return True
	return False

def Jarvis(S):
	n = len(S)
	P = [None] * n
	l = np.where(S[:,0] == np.min(S[:,0]))
	pointOnHull = S[l[0][0]]
	i = 0
	while True:
		P[i] = pointOnHull
		endpoint = S[0]
		for j in range(1, n):
			if ( (endpoint[0] == pointOnHull[0] and endpoint[1] == pointOnHull[1]) or 
				 (not CCW(S[j], P[i], endpoint)) ):
				endpoint = S[j]
		i += 1
		pointOnHull = endpoint
		if endpoint[0] == P[0][0] and endpoint[1] == P[0][1]:
			break

	while P[-1] == None:
		del P[-1]
	
	return np.array(P)


def get_dist(a, b):
	return sqrt((b[1] - a[1])**2 + (b[0] - a[0])**2)

# def get_cos(a, b, c):
# 	dist_1 = get_dist(a, b)
# 	dist_2 = get_dist(a, c)
# 	dist_3 = get_dist(b, c)

# 	return ( (dist_1 + dist_2 - dist_3)    / 
# 			 (2.0 * sqrt(dist_1 * dist_2)) )

def get_norm(a, b):
	return a[0] * b[0] + a[1] * b[1]

def get_mod(a, b):
	return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def get_cos(a, b, c):
	# angle for b
	norm = get_norm((a[0] - b[0], a[1] - b[1]), (b[0] - c[0], b[1] - c[1]))
	mult = get_mod(a, b) * get_mod(c, b)
	return cos(1.0 * norm / mult)

def define_circle(p1, p2, p3):
	temp = p2[0]**2 + p2[1]**2
	bc = (p1[0]**2 + p1[1]**2 - temp) / 2
	cd = (temp - p3[0]**2 - p3[1]**2) / 2

	det = (p1[0] - p2[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p2[1])

	if abs(det) < 1.0e-6:
		return (None, np.inf)

	cx = (bc * (p2[1] - p3[1]) - cd * (p1[1] - p2[1])) / det
	cy = ((p1[0] - p2[0]) * cd - (p2[0] - p3[0]) * bc) / det

	radius = np.sqrt((cx - p1[0])**2 + (cy - p1[1])**2)
	return ((cx, cy), radius)


n = 4
P = np.array([ (np.random.randint(0, 10), 
				np.random.randint(0, 10)) 
				for _ in range(n)])
# P = np.array([[1, 1], [1, 2], [2, 2], [2, 1]])
# P = np.array([[5, 9], [1, 9], [8, 5], [2, 3]])
# P = np.array([[5, 0], [2, 7], [2, 4], [3, 3]])
# P = np.array([[8, 0], [9, 1], [5, 0], [3, 6]])
L = Jarvis(P)

# subpunctul a
ok = True
k = 0

if len(L) != len(P):
	ok = False

else:
	while L[k][0] != P[0][0] or L[k][1] != P[0][1]:
		k += 1

	if k == 0:
		if ( L[1][0] == P[2][0] and L[1][1] == P[2][1] or
			 L[3][0] == P[2][0] and L[3][1] == P[2][1] ):
			ok = False
	elif k == 3:
		if ( L[0][0] == P[2][0] and L[0][1] == P[2][1] or
			 L[2][0] == P[2][0] and L[2][1] == P[2][1] ):
			ok = False
	else:
		if ( L[k - 1][0] == P[2][0] and L[k - 1][1] == P[2][1] or
			 L[k + 1][0] == P[2][0] and L[k + 1][1] == P[2][1] ):
			ok = False

print(ok)

# subpunctul b
delta = 0.01
c = define_circle(P[0], P[1], P[2])
if abs(get_dist([c[0][0], c[0][1]], P[3]) - c[1]) < delta:
	print("Punctul A4 este pe cerc")
elif get_dist([c[0][0], c[0][1]], P[3]) - c[1] > delta:
	print("Punctul A4 este in exteriorul cercului")
else:
	print("Punctul A4 este in interiorul cercului")

# A2 = get_cos(P[0], P[1], P[2])
# A4 = get_cos(P[2], P[3], P[1])
# print(acos(A2) + acos(A4))
# if acos(A2) + acos(A4) + pi < delta:
# 	print("Punctul A4 este pe cerc")
# elif acos(A2) + acos(A4) > pi:
# 	print("Punctul A4 este in interiorul cercului")
# else:
# 	print("Punctul A4 este in exteriorul cercului")
# if abs(cos2 + cos4) < delta:
# 	print("Punctul A4 este pe cerc")
# elif cos2 + cos4 < -delta:
# 	print("Punctul A4 este in interiorul cercului")
# else:
# 	print("Punctul A4 este in exteriorul cercului")

print(P)
print()
print(L)

# plot config
plt.figure()
plt.margins(1) 

# points definition
plt.scatter(P[0][0], P[0][1], color="blue")
plt.scatter(P[1][0], P[1][1], color="yellow")
plt.scatter(P[2][0], P[2][1], color="orange")
plt.scatter(P[3][0], P[3][1], color="red")

# circle definition
c = define_circle(P[0], P[1], P[2])
circle1 = plt.Circle(c[0], c[1], color='r', fill=False)
plt.gcf().gca().add_artist(circle1)

plt.show()