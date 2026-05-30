#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from ase import Atoms
from ase.io import write
from ase.io.lammpsdata import write_lammps_data

# ======================
# Parameters
# ======================

natoms = 30
atomic_volume = 12.0
disturb = 0.5

# ======================
# Random triclinic box
# ======================

box = np.eye(3)

box += (np.random.rand(3, 3) - 0.5) * disturb

# Scale box volume
target_volume = natoms * atomic_volume

current_volume = abs(np.linalg.det(box))

scale = (target_volume / current_volume) ** (1 / 3)

box *= scale

# ======================
# Random atomic positions
# ======================

scaled_positions = np.random.rand(natoms, 3)

positions = scaled_positions @ box

atoms = Atoms(
    symbols=["Au"] * natoms,
    positions=positions,
    cell=box,
    pbc=True
)

# ======================
# Write LAMMPS data
# ======================

write_lammps_data(
    "structure.data",
    atoms)

print("Generated: structure.data")