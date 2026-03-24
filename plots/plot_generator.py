import matplotlib.pyplot as plt
import numpy as np
import os


# Global styling
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 12,
    "axes.labelsize": 12,
    "axes.titlesize": 13,
    "legend.fontsize": 10,
    "figure.dpi": 300
})


def plot_heatmap(load_levels, reserve_levels, risk_matrix):

    os.makedirs("plots", exist_ok=True)

    load_levels = np.asarray(load_levels, dtype=float)
    reserve_levels = np.asarray(reserve_levels, dtype=float)

    fig, ax = plt.subplots(figsize=(6, 4))

    c = ax.imshow(
        risk_matrix,
        origin="lower",
        aspect="auto",
        extent=(
            reserve_levels[0],
            reserve_levels[-1],
            load_levels[0],
            load_levels[-1]
        ),
        cmap="viridis"
    )

    cb = fig.colorbar(c, ax=ax)
    cb.set_label("Cascading Failure Probability")

    ax.set_xlabel("Reserve Ratio")
    ax.set_ylabel("Load Multiplier (λ)")
    ax.set_title("Risk Surface Under Renewable Uncertainty")

    fig.tight_layout()
    fig.savefig("plots/risk_surface.pdf", bbox_inches="tight")
    fig.savefig("plots/risk_surface.png", bbox_inches="tight")
    plt.close(fig)


def plot_runtime(sizes, runtimes):

    fig, ax = plt.subplots(figsize=(5, 3.5))

    ax.plot(sizes, runtimes, marker="o", linewidth=2)

    ax.set_xlabel("Monte Carlo Samples (N)")
    ax.set_ylabel("Runtime (seconds)")
    ax.set_title("Computational Scaling of Certification")

    ax.grid(True, linestyle="--", alpha=0.4)

    fig.tight_layout()
    fig.savefig("plots/runtime_scaling.pdf", bbox_inches="tight")
    fig.savefig("plots/runtime_scaling.png", bbox_inches="tight")
    plt.close(fig)


def plot_strategy_bar(strategies, risks):

    fig, ax = plt.subplots(figsize=(5, 3.5))

    ax.bar(strategies, risks)

    ax.set_ylabel("Cascading Risk")
    ax.set_title("Dispatch Strategy Risk Comparison")

    fig.tight_layout()
    fig.savefig("plots/strategy_comparison.pdf", bbox_inches="tight")
    fig.savefig("plots/strategy_comparison.png", bbox_inches="tight")
    plt.close(fig)


def plot_convergence(Ns, risks):

    fig, ax = plt.subplots(figsize=(5, 3.5))

    ax.plot(Ns, risks, marker="o", linewidth=2)

    ax.set_xlabel("Monte Carlo Samples (N)")
    ax.set_ylabel("Estimated Risk")
    ax.set_title("Monte Carlo Convergence")

    ax.grid(True, linestyle="--", alpha=0.4)

    fig.tight_layout()
    fig.savefig("plots/convergence.pdf", bbox_inches="tight")
    fig.savefig("plots/convergence.png", bbox_inches="tight")
    plt.close(fig)


def plot_certification_boundary(reserves, risks, certified, alpha):

    reserves = np.asarray(reserves)
    risks = np.asarray(risks)

    fig, ax = plt.subplots(figsize=(5, 3.5))

    colors = ["green" if c else "red" for c in certified]

    ax.scatter(reserves, risks, c=colors, s=60)

    ax.axhline(alpha, linestyle="--", linewidth=2)

    ax.set_xlabel("Reserve Ratio")
    ax.set_ylabel("Risk Probability")
    ax.set_title("Statistical Certification Boundary")

    fig.tight_layout()
    fig.savefig("plots/certification_boundary.pdf", bbox_inches="tight")
    fig.savefig("plots/certification_boundary.png", bbox_inches="tight")
    plt.close(fig)