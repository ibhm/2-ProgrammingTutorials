import numpy as np
import matplotlib.pyplot as plt

greyhounds = 500
labs = 500

greyh = 28+4*np.random.randn(greyhounds)
labh = 22+4*np.random.randn(labs)

plt.hist([greyh,labh], stacked=True, color=['b','r'])
plt.show()
