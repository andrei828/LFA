import numpy as np
import matplotlib.pyplot as plt

def simetric_matrix(M):
    return np.all(M == M.T)

def positive_definite(M):
    for i in range(M.shape[0]):
        # We use the Sylvester criteria
        if np.linalg.det(M[:i, :i]) <= 0:
            return False
    return True


def descendent_step(A, b):
	# We choose a point close to the result
	# based on the previously plotted graph
	x0 = np.array([[-1], [2]])

	# The end result threshold
	EPS = 1e-7
	res = b - A @ x0

	# We store the points in the array
	gradient_result = [x0]

	# We choose L2 as the norm
	norm = lambda x: np.linalg.norm(x, ord=2)

	iterations = 0
	x = x0
	# We start the algorithm
	while norm(res) > EPS:
	    # Choosing how far the next step will be
	    learning_rate = (res.T @ res) / (res.T @ A @ res)

	    # We calculate the x(i+1) from x(i)
	    x = x + learning_rate * res
	    res = b - A @ x

	    gradient_result.append(x)
	    iterations += 1

	print("Număr de iterații:", iterations)
	print("Punct de minim:", x.ravel())

	return gradient_result

def conjugate_gradient(A, b):
	x0 = np.array([[-1], [2]])

	# Rețin punctele prin care trec
	conjugate_gradient_result = [x0]

	# The end result threshold
	EPS = 1e-7
	res = b - A @ x0
	direction = res

	# We choose L2 as the norm
	norm = lambda x: np.linalg.norm(x, ord=2)

	iterations = 0
	x = x0
	# We start the algorithm
	while norm(res) > EPS:
		# Choosing how far the next step will be
	    learning_rate = (direction.T @ res) / (direction.T @ A @ direction)
	    
	    # We calculate the x(i+1) from x(i)
	    x = x + learning_rate * direction
	    next_res = res - learning_rate * A @ direction
	    
	    direction_rate = (next_res.T @ next_res) / (res.T @ res)
	    direction = next_res + direction_rate * direction
	    
	    res = next_res
	    
	    conjugate_gradient_result.append(x)
	    iterations += 1

	print("Număr de iterații:", iterations)
	print("Punct de minim:", x.ravel())
	
	return conjugate_gradient_result


def sub_1():

	f = lambda x, y: 24.5 * (x**2) - (42.0 * x * y) + 4 * x + 58.5 * (y**2) + 3 * y
	df_x = lambda x, y: 49 * x - 42.0 * y + 4	
	df_y = lambda x, y: -42.0 * x + 117 * y  + 3

	A = np.array([
	    [49, -42],
	    [-42, 117]
	], dtype=float)

	b = np.array([
	    [4],
	    [3]
	], dtype=float)

	fig = plt.figure()
	ax = fig.add_subplot(projection='3d')

	step = 0.1
	X, Y = np.mgrid[-4:5:step, -3:3:step]

	Z = f(X, Y)

	ax.plot_surface(X, Y, Z)

	plt.show()
	

	if not simetric_matrix(A):
		print('Matricea nu este simetrica')
	elif not positive_definite(A):
		print('Matricea nu este pozitiv definita')
	else:
		print('Matricea este simtrica si pozitiv definita')
		points_gradient_descent = descendent_step(A, b)
		points_conjugate_gradient =  conjugate_gradient(A, b)

		plt.figure()

		cs = plt.contour(X, Y, Z)
		plt.clabel(cs)

		pgd = np.array(points_gradient_descent)
		plt.plot(pgd[:, 0], pgd[:, 1], marker='*', label='Coborârea pe gradient')

		pcg = np.array(points_conjugate_gradient)
		plt.plot(pcg[:, 0], pcg[:, 1], marker='x', label='Metoda gradienților conjugați')

		plt.legend()
		plt.show()

sub_1()