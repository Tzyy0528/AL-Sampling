# AL-Sampling: Active Learning Sampling Strategies for Neural Network Atomic Potentials
<p align="center">
  <img src="TOC.png" width="800">
</p>
This repository provides the active-learning sampling strategies, representative datasets, example simulation workflows, and structural data associated with the global structure search of neutral Au clusters reported in this work.

The implemented workflow combines diversity-based sampling and uncertainty-based sampling to efficiently explore complex low-energy potential-energy surfaces using neural-network atomic potentials (NNAP) coupled with first-principles calculations.

---

# Repository Contents

This repository contains:

- `CUR.py`  
  Diversity-based active-learning query strategy based on CUR decomposition.

- `uncertainty.py`  
  Uncertainty-based query strategy for NNAP active learning.

- `Putative-lowest-energy-structures/`  
  Machine-readable POSCAR files and DFT energies for the putative lowest-energy Auₙ clusters (n = 30–45).

- `Low-lying-isomers/`  
  The five lowest-energy DFT-refined isomers for each cluster size (n = 30–45).

- `Dataset-and-potential/`  
  Example NNAP training dataset and trained neural-network potential used in this work.

- `Example-VASP/`  
  Example VASP input files for structural relaxation and static energy calculations.

- `Example-LAMMPS/`  
  Example LAMMPS input files and scripts used for RSS sampling, and molecular dynamics sampling.

- `README.md`  
  Documentation and workflow description.

---

# Dependencies

The Python scripts require the following packages:

```bash
pip install numpy scipy tqdm ase pandas
```

Some LAMMPS-based workflows additionally require:

- LAMMPS
- MPI
- ASE

---

# Important Note on `jse` / `jsex`

Loading and evaluating the NNAP model in the uncertainty-sampling workflow requires the `jse` / `jsex` package.

Please refer to the official repository for installation instructions:

https://github.com/liqa1024/jse

---

# Sampling Methods Overview

## 1. Diversity-based Sampling via CUR Decomposition (`CUR.py`)

This module calculates global rotationally invariant structural descriptors based on the spherical-Chebyshev basis and performs deterministic CUR matrix decomposition to select structurally diverse configurations from large candidate pools.

A prior-knowledge orthogonalization strategy is additionally employed to suppress configurations already well represented in the existing training database.

### Example Usage

```python
from CUR import cur_select_structures

cur_select_structures(
    db_in_path="raw_GA_candidates.db",
    db_out_path="sampled_for_DFT.db",
    n_select=200,
    db_based_path="training_base.db"
)
```

---

## 2. Uncertainty-based Sampling (`uncertainty.py`)

This module evaluates the prediction uncertainty of the current NNAP model and identifies structures with large energy prediction errors for subsequent DFT labeling and retraining.

### Example Usage

```python
from uncertainty import select_by_energy_uncertainty

select_by_energy_uncertainty(
    db_in_path="validation_set.db",
    db_out_path="high_error_sampled.db",
    top_k=50,
    jnn_path="path/to/your/nnap.jnn"
)
```

---

# Active Learning Workflow

The active-learning cycle used in this work consists of:

1. Generation of candidate cluster structures using global-search methods (e.g., GA or RSS).
2. Diversity-based down-sampling using CUR decomposition.
3. First-principles DFT calculations for selected configurations.
4. Uncertainty-based filtering using NNAP prediction errors.
5. Retraining of the NNAP model.
6. Iterative exploration of the low-energy configurational space.

---

# Structural Data

The repository provides machine-readable structural files for:

- Putative lowest-energy Auₙ clusters (n = 30–45)
- Low-lying DFT-refined isomers
- Relative DFT energies of low-energy isomers

All structures are provided in POSCAR format.

---

# Reproducibility Notes

This repository provides representative examples and machine-readable structural data associated with this work, including:

- Low-lying Au cluster isomers
- Example VASP calculations
- Example LAMMPS sampling workflows
- NNAP datasets
- Trained neural-network potentials

Due to the large computational cost and storage requirements of the full active-learning global-search workflow, the repository does not include all intermediate search trajectories, all DFT calculations, or a fully automated end-to-end reproduction package.

---

# Citation

If you use this repository or the associated workflow, please cite the corresponding publication.

---