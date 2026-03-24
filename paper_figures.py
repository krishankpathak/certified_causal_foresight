import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy import stats

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 12,
    "figure.dpi": 500
})

# ==============================
# >>> REPLACE WITH YOUR ACTUAL DATA <<<
# ==============================

# Example realistic research-grade data (non-trivial phase transition)

load_levels = np.linspace(1.3, 2.0, 8)
reserve_levels = np.linspace(0.01, 0.12, 8)

# Artificial nonlinear risk surface for publishable demonstration
risk_matrix = np.zeros((len(load_levels), len(reserve_levels)))

for i, L in enumerate(load_levels):
    for j, R in enumerate(reserve_levels):
        stress = L - 1.4 - 4*R
        risk_matrix[i,j] = 1/(1+np.exp(-10*stress))

# Convergence
Ns = np.array([20, 50, 100, 150, 250])
conv_risks = np.array([0.28, 0.33, 0.36, 0.38, 0.39])

# Runtime
sizes = np.array([20, 50, 100, 200, 300])
runtimes = np.array([5, 12, 24, 48, 73])

# Certification
cert_reserves = np.linspace(0.01,0.12,6)
cert_risks = np.array([0.45,0.32,0.22,0.15,0.08,0.04])
alpha = 0.1
N_cert = 200

# ==============================
# 1️⃣ Phase Transition Heatmap
# ==============================

X, Y = np.meshgrid(reserve_levels, load_levels)

fig, ax = plt.subplots(figsize=(6,5))
heat = ax.contourf(X, Y, risk_matrix, levels=25, cmap="viridis")
contours = ax.contour(X, Y, risk_matrix, levels=[0.1,0.2,0.4,0.6], colors='white')
ax.clabel(contours, inline=True, fontsize=8)

cbar = fig.colorbar(heat)
cbar.set_label("Cascading Failure Probability")

ax.set_xlabel("Reserve Ratio")
ax.set_ylabel("Load Multiplier (λ)")
ax.set_title("Phase Transition Surface")

plt.tight_layout()
plt.savefig("FIGURE_1_PhaseTransition.pdf")
plt.close()

# ==============================
# 2️⃣ 3D Surface
# ==============================

fig = plt.figure(figsize=(7,5))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, risk_matrix, cmap=cm.viridis)
ax.set_xlabel("Reserve Ratio")
ax.set_ylabel("Load Multiplier (λ)")
ax.set_zlabel("Risk")
fig.colorbar(surf, shrink=0.5)
plt.tight_layout()
plt.savefig("FIGURE_2_3DSurface.pdf")
plt.close()

# ==============================
# 3️⃣ Certification Boundary
# ==============================

z = 1.96
ci = z*np.sqrt((cert_risks*(1-cert_risks))/N_cert)

fig, ax = plt.subplots(figsize=(6,4))
ax.errorbar(cert_reserves, cert_risks, yerr=ci, fmt='o', capsize=4)
ax.axhline(alpha, linestyle="--", linewidth=2)

ax.set_xlabel("Reserve Ratio")
ax.set_ylabel("Risk")
ax.set_title("Statistical Certification Boundary")

plt.tight_layout()
plt.savefig("FIGURE_3_Certification.pdf")
plt.close()

# ==============================
# 4️⃣ Convergence
# ==============================

theoretical = conv_risks[-1] + 1/np.sqrt(Ns)

fig, ax = plt.subplots(figsize=(6,4))
ax.plot(Ns, conv_risks, marker='o', label="Estimated Risk")
ax.plot(Ns, theoretical, linestyle='--', label="1/√N Bound")
ax.set_xlabel("Monte Carlo Samples")
ax.set_ylabel("Risk")
ax.set_title("Monte Carlo Convergence")
ax.legend()
plt.tight_layout()
plt.savefig("FIGURE_4_Convergence.pdf")
plt.close()

# ==============================
# 5️⃣ Runtime Complexity
# ==============================

slope, intercept, r_value, _, _ = stats.linregress(sizes, runtimes)
fit_line = slope*sizes + intercept

fig, ax = plt.subplots(figsize=(6,4))
ax.plot(sizes, runtimes, 'o', label="Measured")
ax.plot(sizes, fit_line, label=f"Linear Fit (R²={r_value**2:.3f})")
ax.set_xlabel("Monte Carlo Samples")
ax.set_ylabel("Runtime (sec)")
ax.set_title("Computational Complexity")
ax.legend()
plt.tight_layout()
plt.savefig("FIGURE_5_RuntimeScaling.pdf")
plt.close()

print("All publication-grade figures generated.")