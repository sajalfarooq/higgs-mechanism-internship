# The Higgs Mechanism and Higgsstrahlung

Sajal Farooq's internship project explores how elementary particles acquire mass and applies the electroweak Standard Model to Higgs production in electron–positron collisions.

- **Part I** develops spontaneous symmetry breaking and the Higgs mechanism. The Python script visualizes the potential and fluctuations around a chosen vacuum.
- **Part II** computes the tree-level cross section for Higgsstrahlung, e⁺e⁻ → ZH, using Mathematica and FeynCalc. The cross section turns on near 216 GeV and peaks at about 0.24 pb near 245 GeV.

![Total Higgsstrahlung cross section versus center-of-mass energy](figures/total_cross_section.png)

## Project files

| File | Contents |
| --- | --- |
| [Internship report](report/Higgs_Internship_Report.pdf) | Theory, derivations, numerical results, and Appendix A. The certificate page was removed, and the printed numbering and contents entry follow the original PDF. |
| [Mathematica notebook](notebooks/higgsstrahlung.nb) | Amplitude, spin and polarization sums, cross sections, and saved plots. |
| [Python script](python/make_figures.py) | Reconstructed from Appendix A and adapted to write PNGs to the figures directory. |

## Figures

| Part | Figures |
| --- | --- |
| I | [Potential slices](figures/potential_slices.png), [symmetry-breaking transition](figures/symmetry_breaking_transition.png), [Mexican hat potential](figures/mexican_hat.png), [vacuum fluctuations](figures/vacuum_fluctuations.png) |
| II | [Tree-level diagram](figures/higgsstrahlung_tree_diagram.png), [total cross section](figures/total_cross_section.png), [threshold detail](figures/threshold_cross_section.png), [angular distribution](figures/angular_distribution.png) |

The PNGs in the initial snapshot come from the report. The vector figures and diagram were rendered from the PDF, and the three cross-section plots were extracted from the embedded images.

## Reproduce the plots

### Part I · Python

From the repository root, run:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe python/make_figures.py
```

The script replaces the four Part I PNGs in `figures/`. Styling may vary with the Matplotlib version and installed fonts. The reconstructed script was checked with NumPy 2.5.3 and Matplotlib 3.11.2.

### Part II · Mathematica

Install FeynCalc in your Mathematica environment. Open [the notebook](notebooks/higgsstrahlung.nb) and choose **Evaluation → Evaluate Notebook**. The notebook was saved with Mathematica 14.2. Its saved outputs can be inspected before evaluation. A fresh Mathematica run was outside the verification of this repository package.

Export the plotted outputs from Mathematica as needed. The notebook contains the total cross-section, angular distribution, and a log–log comparison. The report PNGs provide the published versions, including the threshold detail.
