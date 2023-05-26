import numpy as np
import matplotlib.pyplot as plt


def snRatio(s, x):
    s_sum = np.sum(s**2)
    x_sum = np.sum(x**2)

    sn = 10 * np.log10(x_sum / s_sum)

    return sn


def geneMixSignal(x, sn):
    x_sum = np.sum(x**2)
    s_sum = x_sum / (10 ** (sn / 10))

    length = len(x)

    """ s_sum = len * E[noise^2], E[noise^2] = V[noise], V[noise] = (2 * noise_amp)^2 * V[rand] """
    noise_amp = np.sqrt(3 * s_sum / length)
    noise = 2 * noise_amp * (np.random.rand(length)) - noise_amp

    """
    print("noise_amp: {}".format(noise_amp))
    plt.figure()
    plt.plot(np.arange(length), noise)
    plt.show()
    """

    print("snRatio: {}".format(snRatio(noise, x)))

    mix = x + noise
    return mix