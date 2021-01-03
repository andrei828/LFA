import numpy as np
import matplotlib.pyplot as plt


# *********************************** Subiectul I *********************************
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
	    alpha = (res.T @ res) / (res.T @ A @ res)

	    # We calculate the x(i+1) from x(i)
	    x = x + alpha * res
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
	    alpha = (direction.T @ res) / (direction.T @ A @ direction)
	    
	    # We calculate the x(i+1) from x(i)
	    x = x + alpha * direction
	    next_res = res - alpha * A @ direction
	    
	    direction_rate = (next_res.T @ next_res) / (res.T @ res)
	    direction = next_res + direction_rate * direction
	    
	    res = next_res
	    
	    conjugate_gradient_result.append(x)
	    iterations += 1

	print("Număr de iterații:", iterations)
	print("Punct de minim:", x.ravel())
	
	return conjugate_gradient_result


def sub_1():

	# The input function
	f = lambda x, y: 24.5 * (x**2) - (42.0 * x * y) + 4 * x + 58.5 * (y**2) + 3 * y
	df_x = lambda x, y: 49 * x - 42.0 * y + 4	
	df_y = lambda x, y: -42.0 * x + 117 * y  + 3

	# We build A from df_x and df_y
	A = np.array([
	    [49, -42],
	    [-42, 117]
	], dtype=float)

	# We build b from df_x and df_y
	b = np.array([
	    [4],
	    [3]
	], dtype=float)

	fig = plt.figure()
	plot = fig.add_subplot(projection='3d')

	step = 0.1
	X, Y = np.mgrid[-4:5:step, -3:3:step]

	Z = f(X, Y)

	plot.plot_surface(X, Y, Z)

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





# *********************************** Subiectul II *********************************
def chebyshev_value(k, N, left_margin, right_margin):
    x = np.cos(np.pi * ((N - k) / N))
    return (left_margin + right_margin) / 2 + ((right_margin - left_margin) / 2) * x

def compute_coefficient(k, t, x, N):
    # We calculate all the 
    # coeffiecient using the Newton method
    coeffiecients = []
    for elem in range(N + 1):
        if elem != k:
            coeffiecients.append((t - x[elem]) / (x[k] - x[elem]))
    return np.prod(coeffiecients)

def polynomial_value(t, x, y, N):
    result = 0
    for elem in range(N + 1):
        result += compute_coefficient(elem, t, x, N) * y[elem]
    return result

def plot_truncation_error(x_graph, y_real, y_approx, left_margin, right_margin):
    error = np.abs(y_real - y_approx)
    max_error = np.max(error)

    # The end result threshold
    EPS = 1e-5
    plt.figure('Truncation error')
    plt.plot(x_graph, error)
    plt.hlines(EPS, label='Threshold', xmin=left_margin, xmax=right_margin, color='black')
    plt.hlines(max_error, label='Max error', xmin=left_margin, xmax=right_margin)
    plt.legend()
    plt.show()

def sub_2():
	# The input function
    f = lambda x: 6 * np.sin(-x) + 2 * np.cos(- 3 * x) + 17.14 * x

    # Polynom rank
    N = 20

    # Function interval
    left_margin = -np.pi
    right_margin = +np.pi

    x = np.array([chebyshev_value(k, N, left_margin, right_margin) for k in range(N + 1)])

    # We get the y coords from f in x
    y = f(x)

    # We choose the x coords with 500 points
    x_graph = np.linspace(left_margin, right_margin, 500)

    # We calcuate the y coefficients
    y_graph = f(x_graph)
    y_interpolation = [polynomial_value(t, x, y, N) for t in x_graph]

    plt.figure('Interpolare cu polinoame Lagrange')
    plt.plot(x_graph, y_graph, label='Initial function')
    plt.plot(x_graph, y_interpolation, label='Interpolation polynom')
    plt.scatter(x, y, label='Interpolation nodes')

    plt.legend()
    plt.show()

    # Truncation error
    plot_truncation_error(x_graph, y_graph, y_interpolation, left_margin, right_margin)



# *********************************** Subiectul III *********************************
def cubic_spline(left_margin, right_margin, f, df):

    N = 200
    x = np.linspace(left_margin, right_margin, N + 1)
    y = np.zeros((N + 1, 1))
    for i in range(len(x)):
        y[i] = f(x[i])

    # We copy y to get the a coefficent
    a = y.copy()

    # We calculate the B matrix
    B = np.zeros((N + 1, N + 1))
    B[0][0], B[N][N] = 1, 1
    for i in range(1, N):
        B[i][i - 1] = 1
        B[i][i] = 4
        B[i][i + 1] = 1

    # Echidistant distance 
    h = x[1] - x[0]

    # We solve the system by calculating W
    W = np.zeros((N + 1, 1))
    W[0], W[N] = df(x[0]), df(x[N])
    for i in range(1, N):
        W[i] = (3 * (y[i + 1] - y[i - 1])) / h
    
    # We get the b coefficient
    b = np.linalg.solve(B, W)
    
    c = np.zeros((N, 1))
    d = np.zeros((N, 1))
    # We get the c and d coefficients
    for i in range(N):
        c[i] = 3 * (y[i + 1] - y[i]) / (h * h) - (b[i + 1] + 2 * b[i]) / h
        d[i] = (-2) * (y[i + 1] - y[i]) / (h * h * h) + (b[i + 1] + b[i]) / (h * h)

    
    num_points = 100
    f2 = np.vectorize(f)
    x_graph = np.linspace(left_margin, right_margin, num_points)
    y_graph = f2(x_graph)
    get_polynom = lambda j: lambda X: a[j] + b[j] * (X - x[j]) + c[j] * (X - x[j]) ** 2 + d[j] * (X - x[j]) ** 3

    # We get the y aproximation 
    # using the piecewise method
    y_aprox = np.piecewise(
        x_graph,
        [
            # conditions
            (x[i] <= x_graph) & (x_graph < x[i + 1])
            for i in range(N - 1)
        ],
        [
            # get all polynomials
            get_polynom(i)
            for i in range(N)
        ]
    )

    plt.plot(x_graph, y_graph, label="Initial function")
    plt.plot(x_graph, y_aprox, label="Spinal cubic interpolation")
    plt.scatter(x, y, label='Interpolation nodes')
    plt.legend()
    plt.show()

    # truncation error
    plot_truncation_error(x_graph, y_graph, y_aprox, left_margin, right_margin)


def sub_3():
	# The input function
    f = lambda x: -6 * np.sin(-x) - 6 * np.cos(-4 * x) - 20.16 * x
    df = lambda x: 6 * np.cos(-x) - 24 * np.sin(-4 * x) - 20.16

    left = -np.pi
    right = np.pi

    cubic_spline(left, right, f, df)


print('Subiectul I')
sub_1()
print('Subiectul II (afisarile in matplotlib)')
sub_2()
print('Subiectul III (afisarile in matplotlib)')
sub_3()
