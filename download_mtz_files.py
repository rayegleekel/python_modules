#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 20:12:22 2020

@author: vivekmodi
"""
#Usage python download_mtz_files.py 1gag

import subprocess, os, sys
import pandas as pd

def download_phases(df):
    print('Downloading phase files from PDB...')

    for i in df.index:
        pdb=df.at[i,'PDBid'][0:4].lower()
        if not os.path.isfile(f'{pdb}.mtz'):
            cmd=(f'wget  http://edmaps.rcsb.org/coefficients/{pdb}.mtz')      #Use wget -P path to specify a directory
            subprocess.call(cmd,shell=True)


if __name__=='__main__':
    df=pd.DataFrame()
    df.at[0,'PDBid']=sys.argv[1]
    download_phases(df)
