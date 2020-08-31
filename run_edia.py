#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 13:34:31 2020

@author: vivekmodi
"""
# Usage $python run_edia.py 1gag

import os, subprocess, sys
import pandas as pd

def run_edia(df):
    print('Running EDIA...')
    for i in df.index:
        pdb=df.at[i,'PDBid'].lower()

        if not os.path.isfile(f'Edia_out/{pdb}atomscores.csv'):
            cmd=f'Ediascorer -t {pdb}.cif -d {pdb}_2mFo-DFc_map.ccp4 -o Edia_out/'
            subprocess.call(cmd,shell=True)

if __name__ == '__main__':
    df=pd.DataFrame()
    df.at[0,'PDBid']=sys.argv[1]
    run_edia(df)
