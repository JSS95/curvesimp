import matplotlib.pyplot as plt
import numpy as np

from curvesimp.agarwal import min_err

x = np.linspace(0, 5, 100)
f = np.exp(-x) * np.cos(2 * np.pi * x)
curve = np.column_stack([x, f])

plt.plot(*curve.T, label="original (n=100)")
for n in [50, 25]:
    vert, err = min_err(curve, n)
    plt.plot(*vert.T, "--", label=f"n={n} (err={err:.2f})")
plt.legend()
