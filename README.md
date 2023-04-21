# ATOM_ReORDER_GROMOS

This Python script is designed to help with Molecular Dynamics (MD) simulations of protein-ligand complexes that require special topology preparation. It allows you to reorder your ligand.gro file to match the atom order specified in your ligand.itp file. To prepare your ligand.itp file, you can use the GROMOS forcefield available at https://atb.uq.edu.au/.  By using this script, you can ensure that your ligand atoms are correctly ordered, which is essential for performing accurate MD simulations. The script is easy to use and can save you time when preparing your system for simulations.


# GROMOS_AUTOMATIC_REORDER 
#### This script is part of the project "GROMOS_MD"
#### Copyright (c) 2023, Thanawat Thaingtamtanha
#### Theoretical chemistry group, University of Siegen, Germany
#### All rights reserved.
The program needs your 
- "lig.gro" : From yout protein-ligand complex file.
- "lig.itp" : From https://atb.uq.edu.au/, by upload SMILES or pdb of your ligand pdb.
It will read your "lig.itp" and rearrange the order of atom in "lig.gro" respect to the order of atom in "[ atoms ]" section in "lig.itp".
After use the python script, you will get new "lig_reordered.gro". Copy the new atom order in this file and paste in "solv.gro".

To run the code:

$ python reorder_lig_gro.py <lig.itp> <lig.gro> <out.gro>
