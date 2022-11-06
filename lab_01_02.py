# Задание 2

import matplotlib.pyplot as plt
import numpy as np 
from scipy import stats 
import seaborn as sns 

np.random.seed(2016) # replicate random

# aesthetic parameters of seaborn
sns.set_palette("deep", desat=.6)
sns.set_context(rc={"figure.figsize": (8, 4)})



N, p = 30, 0.4 # shape parameters
binomial = stats.binom(N, p) # Distribution

# histogram
random = binomial.rvs(1000)  # generate random
cuenta = plt.hist(random, 20)
plt.ylabel('частота')
plt.xlabel('значение')
plt.title('Биномиальная Гистограмма')
plt.show()


print( "\n",len(random), " случайных чисел с биномиальным распределением\n", random)
print("\n Дисперсия\n", np.var(random))
print("\n Математическое ожидание\n", np.mean(random))
