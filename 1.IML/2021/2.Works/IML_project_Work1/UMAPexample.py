from time import time

import inline as inline
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import umap
matplotlib inline


sns.set(style='white', context='poster', rc={'figure.figsize':(14,10)})

np.random.seed(42)
data = np.random.rand(800, 4)

fit = umap.UMAP()
u = fit.fit_transform(data)

plt.scatter(u[:,0], u[:,1], c=data)
plt.title('UMAP embedding of random colours');

