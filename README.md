# ATOM_ReORDER_GROMOS

This Python script is designed to help with Molecular Dynamics (MD) simulations of protein-ligand complexes that require special topology preparation. It allows you to reorder your ligand.gro file to match the atom order specified in your ligand.itp file. To prepare your ligand.itp file, you can use the GROMOS forcefield available at https://atb.uq.edu.au/.  By using this script, you can ensure that your ligand atoms are correctly ordered, which is essential for performing accurate MD simulations. The script is easy to use and can save you time when preparing your system for simulations.

This script was developed and used for teaching in theoretical chemistry group, University of Siegen, Germany.

# GROMOS_AUTOMATIC_REORDER 
#### This script is part of the project "GROMOS_MD"
#### Copyright (c) 2023, Thanawat Thaingtamtanha
#### Theoretical chemistry group, University of Siegen, Germany
#### All rights reserved.
The program requires the following files:

"lig.gro": This is your protein-ligand complex file.
"lig.itp": This file can be obtained from https://atb.uq.edu.au/ by uploading the SMILES or PDB file of your ligand.
The program will read your "lig.itp" file and rearrange the order of atoms in "lig.gro" to match the order of atoms in the "[atoms]" section of "lig.itp". After running the Python script, you will obtain a new file called "lig_reordered.gro". Copy the new atom order from this file and paste it into "solv.gro".
To run the code, use the following command:

$ python reorder_lig_gro.py <lig.itp> <lig.gro> <out.gro>
