import math
import pylab
import numpy as np
import functools as ft
import scipy.stats as st

gamma = 0.5
mu, sigma = 0, 0.7

def get_values_first(n):
    samples = get_n_normal_samples(n)
    length = get_length_first(samples)
    return length
    
def get_length_first(samples):
    lambda1 = st.chi2.ppf((1 + gamma)/2, len(samples))
    lambda2 = st.chi2.ppf((1 - gamma)/2, len(samples))
    left = ft.reduce((lambda x, y: x + y ** 2), samples, 0) / lambda1
    right = ft.reduce((lambda x, y: x + y ** 2), samples, 0) / lambda2
    return right - left

def get_n_normal_samples(n):
    return np.random.normal(mu, sigma, n)

def get_values_second(n):
    samples = get_n_normal_samples(n)
    length = get_length_second(samples)
    return length
    
def get_length_second(samples):
    z1 = st.norm.ppf((3 + gamma)/4)
    z2 = st.norm.ppf((3 - gamma)/4)
    left = ft.reduce((lambda x, y: x + y), samples, 0) ** 2 / (len(samples) * z1 ** 2)
    right = ft.reduce((lambda x, y: x + y), samples, 0) ** 2 / (len(samples) * z2 ** 2)
    return right - left

xlist = [i for i in range(1, 250)]
ylist_first = [get_values_first(i) for i in xlist]
ylist_second = [get_values_second(i) for i in xlist]

pylab.clf()
pylab.plot (xlist, ylist_first)
pylab.savefig("first-chart.png")

pylab.clf()
pylab.plot (xlist, ylist_second)
pylab.savefig("second-chart.png")
