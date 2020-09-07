#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 08:30:15 2020

@author: vivekmodi
"""

# This script outputs the frequency of each uniprot in PDB.
# Usage $python pdbaa-summary.py 

import subprocess, gzip

def download_pdbaa():
    print("Downloading pdbaa from dunbrack.fccc.edu...")
    cmd=("rm pdbaa.gz")
    subprocess.call(cmd, shell=True)
    cmd=("wget http://dunbrack.fccc.edu/Guoli/culledpdb_hh/pdbaa.gz")
    subprocess.call(cmd,shell=True)
    
def pdbaa_summary():
    print('Counting PDB structures for each uniprot...')
    fhandle_pdbaa=gzip.open('pdbaa.gz','rt')
    fhandle_summ=open('PDBAA-summary.tab','w')
    uniprot_count=dict()
    for lines in fhandle_pdbaa:
        lines=lines.strip()
        if '>' in lines:
            if '|' in lines:            #Ignore fusion proteins
                continue
            uniprot=lines.split('<')[1].split('>')[0].split('(')[0]
            uniprot_count[uniprot]=0
    
    fhandle_pdbaa.seek(0)
    for lines in fhandle_pdbaa:
        lines=lines.strip()
        if '>' in lines:
            if '|' in lines:            #Ignore fusion proteins
                continue
            uniprot=lines.split('<')[1].split('>')[0].split('(')[0]
            uniprot_count[uniprot]+=1
            
    for items in uniprot_count:
        fhandle_summ.write(f'{items} {uniprot_count[items]}\n')
        
    cmd=('sort -k2nr PDBAA-summary.tab > temp; column -t temp > PDBAA-summary.tab;')
    subprocess.call(cmd,shell=True)
    
    fhandle_pdbaa.close()
    
if __name__ == '__main__':
    download_pdbaa()
    pdbaa_summary()