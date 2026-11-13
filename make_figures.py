"""Generate the four Part I figures from the report's Appendix A."""

from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt

FIGURES = Path(__file__).resolve().parents[1] / "figures"

plt.rcParams.update({
    "font.size": 11,
    "font.family": "serif",
    "mathtext.fontset": "cm",
    "axes.spines.top": False,
    "axes.spines.right": False,
})


def potential(radius, mu2):
    return mu2 * radius**2 + radius**4


def save(fig, name):
    fig.tight_layout()
    fig.savefig(FIGURES / f"{name}.png", dpi=300, bbox_inches="tight")
    plt.close(fig)


def main():
    FIGURES.mkdir(parents=True, exist_ok=True)
    phi = np.linspace(-1.6, 1.6, 400)
    v = np.sqrt(0.5)

    fig, (symmetric, broken) = plt.subplots(1, 2, figsize=(9, 3.6))
    symmetric.plot(phi, potential(phi, 1), color="tab:blue")
    symmetric.set_title(r"$\mu^2 > 0$: unique vacuum at $\phi = 0$")
    symmetric.plot(0, 0, "ko", ms=6)
    broken.plot(phi, potential(phi, -1), color="tab:red")
    broken.set_title(r"$\mu^2 < 0$: degenerate vacua at $|\phi| = v$")
    broken.plot([v, -v], [potential(v, -1)] * 2, "ko", ms=6)
    broken.annotate(r"$+v$", (v, potential(v, -1)), xytext=(6, -12),
                    textcoords="offset points")
    broken.annotate(r"$-v$", (-v, potential(v, -1)), xytext=(-22, -12),
                    textcoords="offset points")
    for ax in (symmetric, broken):
        ax.set(xlabel=r"$\phi$", ylabel=r"$V(\phi)$")
    save(fig, "potential_slices")

    fig, ax = plt.subplots(figsize=(6.2, 4))
    colors = plt.cm.coolwarm(np.linspace(0, 1, 5))
    for mu2, color in zip([1, 0.5, 0, -0.5, -1], colors):
        ax.plot(phi, potential(phi, mu2), color=color, label=rf"$\mu^2={mu2:+.1f}$")
    ax.set(xlabel=r"$\phi$", ylabel=r"$V(\phi)$", ylim=(-0.4, 1.5),
           title=r"Symmetry breaking as $\mu^2$ passes through zero")
    ax.legend(frameon=False)
    save(fig, "symmetry_breaking_transition")

    fig = plt.figure(figsize=(6.5, 5))
    ax = fig.add_subplot(projection="3d")
    theta = np.linspace(0, 2 * np.pi, 120)
    radius, angle = np.meshgrid(np.linspace(0, 1.35, 120), theta)
    ax.plot_surface(radius * np.cos(angle), radius * np.sin(angle),
                    potential(radius, -1), cmap="viridis", alpha=0.9,
                    linewidth=0, antialiased=True, rstride=2, cstride=2)
    ax.plot(v * np.cos(theta), v * np.sin(theta), potential(v, -1), "r-",
            lw=2.5, label=r"degenerate vacua $|\phi| = v$")
    ax.set(xlabel=r"$\mathrm{Re}\,\phi$", ylabel=r"$\mathrm{Im}\,\phi$",
           zlabel=r"$V(\phi)$", title=r"Mexican hat potential ($\mu^2 < 0$, $\lambda > 0$)")
    ax.legend(loc="upper right")
    ax.view_init(elev=28, azim=-60)
    save(fig, "mexican_hat")

    fig, ax = plt.subplots(figsize=(6.2, 5), subplot_kw={"aspect": "equal"})
    ax.add_patch(plt.Circle((0, 0), v, fill=False, color="tab:gray", ls="--", lw=1.5))
    ax.plot(v, 0, "ko", ms=8)
    ax.annotate(r"$\langle\phi\rangle = v$", (v, 0), xytext=(8, -14),
                textcoords="offset points")
    ax.annotate("", xytext=(v, 0), xy=(v + 0.28, 0),
                arrowprops={"arrowstyle": "->", "color": "tab:red", "lw": 2})
    ax.text(v + 0.30, 0.05, r"$h(x)$ radial: massive (Higgs)", color="tab:red")
    ax.annotate("", xytext=(v, 0), xy=(v, 0.30),
                arrowprops={"arrowstyle": "->", "color": "tab:blue", "lw": 2})
    ax.text(v + 0.03, 0.36, r"$\theta(x)$ angular: massless (Goldstone)", color="tab:blue")
    ax.set(xlim=(-1.2, 1.6), ylim=(-1.1, 1.1), xlabel=r"$\mathrm{Re}\,\phi$",
           ylabel=r"$\mathrm{Im}\,\phi$", title="Fluctuations around the chosen vacuum")
    ax.axhline(0, color="0.85", lw=0.8, zorder=0)
    ax.axvline(0, color="0.85", lw=0.8, zorder=0)
    save(fig, "vacuum_fluctuations")


if __name__ == "__main__":
    main()
