import matplotlib.pyplot as plt
import numpy as np

from curvesimplify.imaiiri import min_err

x = np.linspace(0, 5, 50)
f = np.exp(-x) * np.cos(2 * np.pi * x)
curve = np.column_stack([x, f])

plt.plot(*curve.T, label=f"original (n={len(x)})")
for n in [25, 10]:
    vert, err = min_err(curve, n)
    plt.plot(*vert.T, "--", label=f"n={n} (err={err:.2f})")
plt.legend()
