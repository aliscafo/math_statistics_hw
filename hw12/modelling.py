import numpy as np
import matplotlib.pyplot as plt

a = 0.42
c = 1 / (2 * a + 2 * np.exp(-a)) # We want F(+~) = 1, so 2 * c * np.exp(-a) + 2 * c * a = 1

n = 228942

def inverse(n):
    vals = []

    for _ in range(n):
        alpha = np.random.uniform()
        
        if alpha < c * np.exp(-a):
            vals.append(np.log(alpha / c))
        elif alpha < c * np.exp(-a) + 2 * c * a:
            vals.append(alpha / c - np.exp(-a) - a)
        else:
            vals.append(-np.log((2 * c * a + 2 * c * np.exp(-a) - alpha) / c))

    return vals


def decomposition(n):
    vals = []

    for _ in range(n):
        alpha = np.random.uniform()
        
        if alpha < c * np.exp(-a):
            vals.append(- np.random.exponential() - a)
        elif alpha < c * np.exp(-a) + 2 * c * a:
            vals.append(np.random.uniform() * 2 * a - a)
        else:
            vals.append(np.random.exponential(1) + a)

    return vals

plt.clf()
plt.hist(inverse(n), bins=6000)
plt.axvline(a, color='red')
plt.axvline(-a, color='red')
plt.savefig('inverse_method')

plt.clf()
plt.hist(decomposition(n), bins=6000)
plt.axvline(a, color='red')
plt.axvline(-a, color='red')
plt.savefig('decomposition_method')