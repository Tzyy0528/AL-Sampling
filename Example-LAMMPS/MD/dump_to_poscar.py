#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ase.io import read, write
import os

dump_file = "dump.lammpstrj"

# 读取所有帧
frames = read(dump_file, index=":")

# 输出目录
output_dir = "POSCARs"
os.makedirs(output_dir, exist_ok=True)

for i, atoms in enumerate(frames):

    output_path = os.path.join(
        output_dir,
        f"POSCAR-{i+1:03d}"
    )

    write(
        output_path,
        atoms,
        format="vasp"
    )

    print(f"Written: {output_path}")