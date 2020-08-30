#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 15:01:50 2020

@author: vivekmodi
"""

#Usage from commandline python download_sifts.py /download/sifts 1xyz
#Usage from another script download_sifts(downld_dir, pdbid)

import os, subprocess, sys

def download_sifts(downld_dir, pdbid):
    print('Downloading files from Sifts...')
    if not os.path.isfile(downld_dir+"/"+str(pdbid).lower()+".xml.gz"):
                print("Downloading Sifts "+pdbid+"...")
                cmd=("wget ftp://ftp.ebi.ac.uk/pub/databases/msd/sifts/xml/"+str(pdbid).lower()+".xml.gz -P "+downld_dir)
                subprocess.call(cmd,shell=True)


if __name__ == '__main__':
    downld_dir=sys.argv[1]
    pdbid=sys.argv[2]
    download_sifts(downld_dir, pdbid)
