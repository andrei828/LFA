import numpy as np
import matplotlib.pyplot as plt

def int_spline_cubica(left_margin, right_margin, f, df):

    N = 200
    x = np.linspace(left_margin, right_margin, N + 1)
    y = np.zeros((N + 1, 1))
    for i in range(len(x)):
        y[i] = f(x[i])

    # We copy y to get the a coefficent
    a = y.copy()

    # We calculate the B matrix
    B = np.zeros((N+1, N+1))
    B[0][0], B[N][N] = 1, 1
    for i in range(1, N):
        B[i][i - 1] = 1
        B[i][i] = 4
        B[i][i + 1] = 1

    # echidistant distance 
    h = x[1] - x[0]

    # We solve the system
    W = np.zeros((N + 1, 1))
    W[0], W[N] = df(x[0]), df(x[N])
    for i in range(1, N):
        W[i] = 3 * (y[i + 1] - y[i - 1]) / h
    
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
    x_grafic = np.linspace(left_margin, right_margin, num_points)
    y_grafic = f2(x_grafic)
    get_polynom = lambda j: lambda X: a[j] + b[j] * (X - x[j]) + c[j] * (X - x[j]) ** 2 + d[j] * (X - x[j]) ** 3

    # We get the y aproximation 
    # using the piecewise method
    y_aproximat = np.piecewise(
        x_grafic,
        [
            # conditions
            (x[i] <= x_grafic) & (x_grafic < x[i + 1])
            for i in range(N - 1)
        ],
        [
            # get all polynomials
            get_polynom(i)
            for i in range(N)
        ]
    )

    plt.plot(x_grafic, y_grafic, linestyle='--', label="Initial function")
    plt.plot(x_grafic, y_aproximat, label="Spinal cubic interpolation")
    plt.scatter(x, y, label='Interpolation nodes')
    plt.legend()
    plt.show()

    # eroare de trunchiere
    plot_truncation_error(x_grafic, y_grafic, y_aproximat, left_margin, right_margin)

def plot_truncation_error(x_grafic, y_real, y_approx, left_margin, right_margin):
    error = np.abs(y_real - y_approx)
    max_error = np.max(error)

    EPS = 1e-5
    plt.figure('Truncation error')
    plt.plot(x_grafic, error)
    plt.hlines(EPS, xmin=left_margin, xmax=right_margin)
    plt.hlines(max_error, label='Max error', xmin=left_margin, xmax=right_margin)
    plt.legend()
    plt.show()


def sub_3():
    f = lambda x: -6 * np.sin(-x) - 6 * np.cos(-4 * x) - 20.16 * x
    df = lambda x: 6 * np.cos(-x) - 24 * np.sin(-4 * x) - 20.16

    left = -np.pi
    right = np.pi

    int_spline_cubica(left, right, f, df)

sub_3()