import numpy as np
import math
import matplotlib.pyplot as plt


def f(t, y, eqn):          # Equation Inputs (Has to be configured within the code below)

    # 1) t = independent variable
    # 2) y = dependent variable
    # 3) eqn is only for selecting which equation to execute
    # 4) add/remove equations as necessary
    # 5) adjust value of m in the main() function accordingly

    if eqn == 0:
        # x0 = right hand side of equation 0
        yp0 = 9 * y[1, 0]
        return yp0
    elif eqn == 1:
        # x1 = right hand side of eqn 1
        yp1 = - y[0, 0]
        return yp1
    # elif eqn == ..... continue like this
    else:
        return 0   # idiot-proofing


def main():     # Main driver function
    m: int = 2  # number of variables or equations
    print("Solver is currently configured for", m, "equations which are predefined in the code.")

    print("Specify start point")    # time duration
    a = float(input())
    print("Specify end point")
    b = float(input())

    print("Step size")
    h = float(input())  # step size

    t = np.arange(start=a, stop=b, step=h, dtype=float)  # time array
    n = len(t)

    y_app = np.ones([m, n])  # array for approximations

    print("Input initial conditions")   # initial conditions
    for i in range(0, m):
        print("y (", i, ", 0 ) = ?")
        y_app[i, 0] = float(input())

    k1 = np.zeros([m, 1])
    k2 = np.zeros([m, 1])
    k3 = np.zeros([m, 1])
    k4 = np.zeros([m, 1])
    k_avg = np.zeros([m, 1])

    input_column = np.zeros([m, 1])

    for i in range(1,n):
        for j in range(0, m):
            input_column[j, 0] = y_app[j, i - 1]
        for j in range(0, m):
            k1[j, 0] = f(t[i - 1], input_column, j)

        for j in range(0, m):
            input_column[j, 0] = y_app[j, i - 1] + h * 0.5 * k1[j, 0]
        for j in range(0, m):
            k2[j, 0] = f(t[i - 1] + 0.5 * h, input_column, j)

        for j in range(0, m):
            input_column[j, 0] = y_app[j, i - 1] + h * 0.5 * k2[j, 0]
        for j in range(0, m):
            k3[j, 0] = f(t[i - 1] + 0.5 * h, input_column, j)

        for j in range(0, m):
            input_column[j, 0] = y_app[j, i - 1] + h * k3[j, 0]
        for j in range(0, m):
            k4[j, 0] = f(t[i - 1] + h, input_column, j)

        for j in range(0, m):
            k_avg[j, 0] = k1[j, 0]/6 + k2[j, 0]/3 + k3[j, 0]/3 + k4[j, 0]/6

        for j in range(0, m):
            y_app[j, i] = y_app[j, i - 1] + h * k_avg[j, 0]

    plt.plot(t, y_app[0, :], label = "Equation 0")  # plotting y0
    plt.plot(t, y_app[1, :], label = "Equation 1")  # plotting y1
    plt.title("Coupled ODE system")
    plt.xlabel("independent variable")
    plt.ylabel("dependent variables")
    plt.legend()    # showing legend
    plt.show()      # showing plot


main()
