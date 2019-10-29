import random
import numpy as np
import matplotlib.pyplot as plt
x, y = [], []
for i in range(10):
    x.append(random.randint(1, 10))
    y.append(random.randint(1, 10))

plt.plot(x, y)
plt.show()
