#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 13:48:50 2020

@author: vivekmodi
"""


import os, subprocess, sys
from Bio import PDB

def download_cifs(downld_dir,pdbid):
    print('Downloading MMCIFs...')

    if not os.path.isfile(downld_dir+"/"+str(pdbid).lower()+".cif.gz"):           #Download if file does not exist
            pdb1=PDB.PDBList()
            pdb1.retrieve_pdb_file(pdbid,pdir=downld_dir)

    if os.path.isfile(downld_dir+"/"+str(pdbid).lower()+".cif"):     #gzip files
            cmd=("gzip -f "+downld_dir+"/"+str(pdbid).lower()+".cif")
            subprocess.call(cmd, shell=True)

if __name__ == '__main__':
    downld_dir=sys.argv[1]
    pdbid=sys.argv[2]
    download_cifs(downld_dir,pdbid)
