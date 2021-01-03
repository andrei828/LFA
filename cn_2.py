import numpy as np
import matplotlib.pyplot as plt

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

def sub_2():
    f = lambda x: 6 * np.sin(-x) + 2 * np.cos(- 3 * x) + 17.14 * x

    # Function interval
    left_margin = -np.pi
    right_margin = +np.pi

    # Polynom rank
    N = 20

    x = np.array([chebyshev_value(k, N, left_margin, right_margin) for k in range(N + 1)])

    # We get the y coords from f in x
    y = f(x)

    num_points = 500
    x_grafic = np.linspace(left_margin, right_margin, num_points)

    # We calcuate the y coefficients
    y_grafic = f(x_grafic)
    y_interpolat = [polynomial_value(t, x, y, N) for t in x_grafic]

    plt.figure('Interpolare cu polinoame Lagrange')
    plt.plot(x_grafic, y_grafic, label='Initial function')
    plt.plot(x_grafic, y_interpolat, label='Interpolation polynom')
    plt.scatter(x, y, label='Interpolation nodes')

    plt.legend()
    plt.show()

    
    plot_truncation_error(x_grafic, y_grafic, y_interpolat, left_margin, right_margin)
    

sub_2()