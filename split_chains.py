#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 15:17:07 2020

@author: vivekmodi
"""

#Usage from commandline python split_chains.py file.cif/file.cif.gz    (prints the chain id provided in a separate file)

import os, gzip, subprocess, sys
from Bio import PDB

############# FIX (The files which have disordered atoms give an error while copying while printing separate chains. This block is a fix copied from https://github.com/biopython/biopython/issues/455)

def get_unpacked_list(self):
#     """
#     Returns all atoms from the residue,
#     in case of disordered, keep only first alt loc and remove the alt-loc tag
#     """
    atom_list = self.get_list()
    undisordered_atom_list = []
    for atom in atom_list:
        if atom.is_disordered():
            atom.altloc=" "
            undisordered_atom_list.append(atom)
        else:
            undisordered_atom_list.append(atom)
    return undisordered_atom_list

PDB.Residue.Residue.get_unpacked_list = get_unpacked_list

###########################


def split_chains(pdbid):

        if not os.path.isfile(pdbid):
            print("Error: Function split_chains: file does not exist:"+pdbid+"\n")
            return

        if '.gz' in pdbid:
            handle=gzip.open(pdbid,"rt")
            parser=PDB.MMCIFParser(QUIET=True)
            structure=parser.get_structure(pdbid[:-7],handle)
        else:
            handle=open(pdbid,"rt")
            parser=PDB.MMCIFParser(QUIET=True)
            structure=parser.get_structure(pdbid[:-4],handle)

        for model in structure:
            for chain in model:
                    #io=PDB.PDBIO()      Section to output .pdb format
                    #io.set_structure(chain)
                    #chain_filename=(structure.id+chain.id+".pdb")             #Output in PDB format
                    #io.save(chain_filename)
                    #cmd=('gzip -f '+chain_filename)
                    #subprocess.call(cmd, shell=True)

                    io=PDB.MMCIFIO()
                    io.set_structure(chain)
                    chain_filename=(structure.id+chain.id+".cif")             #Output in MMCIF format
                    io.save(chain_filename)
                    cmd=('gzip -f '+chain_filename)
                    subprocess.call(cmd, shell=True)

if __name__ == '__main__':
     pdbid=sys.argv[1]
     split_chains(pdbid)
