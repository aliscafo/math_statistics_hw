import math
import pylab
from matplotlib import mlab
import numpy as np
import functools as ft

const = 67

def get_values_uniform(k):
    samples = [get_theta_k_uniform(k) for _ in range(1, 1500)]
    summ = ft.reduce((lambda x, y: x + (y - const) ** 2), samples, 0)
    return (summ / len(samples)) ** 0.5
    
def get_theta_k_uniform(k):
    n = 1000
    samples = get_n_uniform_samples(n)
    k_moment = ft.reduce((lambda x, y: x + y ** k), samples, 0) / n
    theta = ((k + 1) * k_moment) ** (1 / k)
    return theta

def get_n_uniform_samples(n):
    return np.random.uniform(0, const, n)

def get_values_exponential(k):
    samples = [get_theta_k_exponential(k) for _ in range(1, 1500)]
    summ = ft.reduce((lambda x, y: x + (y - const) ** 2), samples, 0)
    return (summ / len(samples)) ** 0.5
    
def get_theta_k_exponential(k):
    n = 1000
    samples = get_n_exponential_samples(n)
    k_moment = ft.reduce((lambda x, y: x + y ** k), samples, 0) / n
    theta = (math.factorial(k) / k_moment) ** (1 / k)
    return theta

def get_n_exponential_samples(n):
    return np.random.exponential(1 / const, n)

xlist = [i for i in range(1, 100)]
ylist_uniform = [get_values_uniform(x) for x in xlist]
ylist_exponential = [get_values_exponential(x) for x in xlist]

pylab.plot (xlist, ylist_uniform)
pylab.savefig("uniform-chart.png")

pylab.clf()
pylab.plot (xlist, ylist_exponential)
pylab.savefig("exponential-chart.png")
