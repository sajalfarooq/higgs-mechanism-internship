# The Higgs Mechanism and Higgsstrahlung

Sajal Farooq's internship project explores how elementary particles acquire mass and applies the electroweak Standard Model to Higgs production in electron–positron collisions.

- **Part I** develops spontaneous symmetry breaking and the Higgs mechanism. The Python script visualizes the potential and fluctuations around a chosen vacuum.
- **Part II** computes the tree-level cross section for Higgsstrahlung, e⁺e⁻ → ZH, using Mathematica and FeynCalc.

![Total Higgsstrahlung cross section versus center-of-mass energy](total_cross_section.png)

## Project files

| File | Contents |
| --- | --- |
| [Internship report](Higgs_Internship_Report.pdf) | Theory, derivations, and numerical results. |
| [Mathematica notebook](higgsstrahlung.nb) | Amplitude, spin and polarization sums, cross sections, and saved plots. |
| [Python script](make_figures.py) | Generates the Higgs potential and symmetry-breaking plots. |

## Figures

| Part | Figures |
| --- | --- |
| I | [Potential slices](potential_slices.png), [symmetry-breaking transition](symmetry_breaking_transition.png), [Mexican hat potential](mexican_hat.png), [vacuum fluctuations](vacuum_fluctuations.png) |
| II | [Tree-level diagram](higgsstrahlung_tree_diagram.png), [total cross section](total_cross_section.png), [threshold detail](threshold_cross_section.png), [angular distribution](angular_distribution.png) |

## Reproduce the plots

- **Part I** — Install the Python dependencies with `python -m pip install -r requirements.txt`, then run `python python/make_figures.py` from the repository root.
- **Part II** — Open `notebooks/higgsstrahlung.nb` in Wolfram Mathematica with FeynCalc available and choose **Evaluation → Evaluate Notebook**.

## References

- F. Englert and R. Brout, [“Broken Symmetry and the Mass of Gauge Vector Mesons”](https://doi.org/10.1103/PhysRevLett.13.321), *Physical Review Letters* **13**, 321–323 (1964).
- A. Djouadi, [“The Anatomy of Electro-Weak Symmetry Breaking. I: The Higgs Boson in the Standard Model”](https://arxiv.org/abs/hep-ph/0503172), a review covering Higgs production, including Higgsstrahlung.
- [FeynCalc](https://feyncalc.github.io/), the Mathematica package used for the symbolic calculation.nment. Open [the notebook](notebooks/higgsstrahlung.nb) and choose **Evaluation → Evaluate Notebook**. The notebook was saved with Mathematica 14.2.

Export the plotted outputs from Mathematica as needed. The notebook contains the total cross-section, angular distribution, and a log–log comparison.
