import numpy as np
import matplotlib.pyplot as plt

__author__ = 'alexpashevich'

def show_plot(x, y, title="Plot", x_name="x", y_name="y"):
    plt.figure()
    plt.plot(x, y)
    plt.grid()
    # if not do_not_show_title:
        # plt.title(title)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    # if save_fig:
    #     plt.savefig('images/' + title.replace(' ', '_') + '.png')
    plt.show()


def show_arr(y, title="Plot", x_name="x", y_name="y"):
    show_plot(range(len(y)), y, title, x_name, y_name)

def show_complex_array(y):
    plt.figure()
    plt.plot(range(len(y)), np.abs(y), 'g', label='abs')
    plt.plot(range(len(y)), np.real(y), 'r', label='real')
    plt.plot(range(len(y)), np.imag(y), 'b', label='imag')
    plt.plot(range(len(y)), np.angle(y), 'y', label='angle')

    plt.legend()
    plt.grid()
    plt.show()

def myDFT1D(x):
    n = len(x)
    x_transf = [complex(0,0)] * n
    for k in range(n):
        sum = 0.
        for j in range(n):
            sum += x[j] * np.exp(-2 * np.pi * complex(0,1) * j * k / n)
            # if j == 8:
                # print('x[j] = ' + str(x) + ', exp = ' + str(np.exp(-2 * np.pi * complex(0,1) * j * k / n)))
        x_transf[k] = sum
    # i=complex(0,1)
    return x_transf

def myInvDFT1D(x_transf):
    n = len(x_transf)
    x = []
    for k in range(n):
        sum = 0.
        for j in range(n):
            sum += x_transf[j] * np.exp(2 * np.pi * 1j * j * k / n)
        x.append(sum / n)
    return x

def generateDelta(IdxSampleWhereImpuls, numberOfSamples):
    d = [0.] * numberOfSamples
    d[IdxSampleWhereImpuls] = 1
    return d


if __name__ == "__main__":
    # question 2.3 (and 2.5 as well)
    d_0 = generateDelta(0, 50)
    d_0_transf = myDFT1D(d_0)
    show_complex_array(d_0_transf)

    # question 2.6
    d_4 = generateDelta(4, 50)
    d_4_transf = myDFT1D(d_4)
    show_complex_array(d_4_transf)

    # question 2.7
    d_8 = generateDelta(8, 50)
    d_8_transf = myDFT1D(d_8)
    show_complex_array(d_8_transf)

    # question 2.8
    d_0_inverse = myInvDFT1D(d_0_transf)
    show_arr(d_0_inverse)
    d_4_inverse = myInvDFT1D(d_4_transf)
    show_arr(d_4_inverse)
    d_8_inverse = myInvDFT1D(d_8_transf)
    show_arr(d_8_inverse)
