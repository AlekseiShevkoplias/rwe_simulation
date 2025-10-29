import numpy as np
import pandas as pd
from scipy.stats import truncnorm
import matplotlib.pyplot as plt
import seaborn as sns

seed = 42
rng = np.random.default_rng(seed)


def generate_age(n_samples=1000, mean=58, std=12, lower=24, upper=90):
    a, b = (lower - mean) / std, (upper - mean) / std
    age_base = truncnorm(a, b, loc=mean, scale=std)

    samples = age_base.rvs(size=n_samples, random_state=rng)
    return samples

def generate_wealth():

def generate_smoking(n_samples=1000)


def generate_CCI(n_samples=1000, baseline_lambda=1.2, age_coefficient=0.015, upper_bound=8):



    
