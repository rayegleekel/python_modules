#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 21:25:46 2020

@author: vivekmodi
"""
#Usage $python run_phoenix.py 1gag

import subprocess,os,sys
import pandas as pd

def run_phoenix(df):
    print('Running Phoenix...')
    for i in df.index:
        pdb=df.at[i,'PDBid'][0:4].lower()

        if not os.path.isfile(f'{pdb}_2mFo-DFc_map.ccp4'):
            if not os.path.isfile(f'{pdb}_2mFo-DFc_map.ccp4.gz'):
                cmd=f'phenix.maps {pdb}.cif {pdb}.mtz'
                subprocess.call(cmd,shell=True)

if __name__ == '__main__':
    df=pd.DataFrame()
    df.at[0,'PDBid']=sys.argv[1]
    run_phoenix(df)
