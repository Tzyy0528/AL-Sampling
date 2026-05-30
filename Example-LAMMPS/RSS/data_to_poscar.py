#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ase.io import read, write

atoms = read(
    "relaxed.data",
    format="lammps-data"
)

write(
    "POSCAR",
    atoms,
    format="vasp"
)

print("Generated: POSCAR")