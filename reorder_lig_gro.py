## GROMOS_AUTOMATIC_REORDER ##
# This script is part of the project "GROMOS_MD"
# Copyright (c) 2023, Thanawat Thaingtamtanha
# Theoretical chemistry group, University of Siegen, Germany
# All rights reserved.
#!/usr/bin/env python

import sys


def reorder_lig_gro(lig_itp_path, lig_gro_path, out_path):
    # Open the "lig.itp" file and extract the atom order
    with open(lig_itp_path, 'r') as f:
        lines = f.readlines()
        start = lines.index('[ atoms ]\n') + 1
        atom_order = []
        for line in lines[start:]:
            if line.startswith('[ bonds ]'):
                break  # Stop processing the file if [ bonds ] is reached
            if line.startswith(';'):
                continue
            atom_data = line.split()
            if len(atom_data) < 5:
                raise ValueError(f'Invalid format in "lig.itp" line: {line}')
            atom_order.append(atom_data[4])

    # Open the "lig.gro" file and reorder the atoms
    with open(lig_gro_path, 'r') as f:
        lines = f.readlines()
        natoms = int(lines[1])
        if natoms != len(atom_order):
            raise ValueError('Number of atoms in "lig.gro" does not match "lig.itp"')
        start = 2
        end = start + natoms
        atoms = lines[start:end]
        reordered_atoms = sorted(atoms, key=lambda x: atom_order.index(x.split()[1]))

    # Write the reordered atoms to a new file
    with open(out_path, 'w') as f:
        f.write(lines[0])  # Write the title line
        f.write(f'{natoms}\n')  # Write the number of atoms
        for atom in reordered_atoms:
            f.write(atom)  # Write each reordered atom


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(f'Usage: {sys.argv[0]} <lig.itp> <lig.gro> <out.gro>')
        sys.exit(1)

    lig_itp_path = sys.argv[1]
    lig_gro_path = sys.argv[2]
    out_path = sys.argv[3]

    try:
        reorder_lig_gro(lig_itp_path, lig_gro_path, out_path)
    except Exception as e:
        print(e)
        sys.exit(1)

    print(f'Reordered "lig.gro" written to "{out_path}"')
    print(f'This script was developed by Thanawat Thaingtamtanha')
    print(f'From Theoretical chemistry group, University of Siegen, Germany')
    print(f'Why dont joy us for Table tennis?')
