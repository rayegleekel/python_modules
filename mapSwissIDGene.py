#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 09:54:06 2020

@author: vivekmodi
"""
#This script extracts uniprotid, gene and protein name information from uniprot.fasta file.
#Biopython currently can not read Uniprot text file due to an error

import gzip, subprocess
from Bio import SeqIO

def download_swissprot():
    cmd='curl -O ftp://ftp.uniprot.org/pub/databases/uniprot/knowledgebase/uniprot_sprot.fasta.gz'
    process=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
    process.wait()
    
def download_trembl():
    cmd='curl -O ftp://ftp.uniprot.org/pub/databases/uniprot/knowledgebase/uniprot_trembl.fasta.gz'
    process=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
    process.wait()
    
def update_swissprot():
    print('Reading SwissProt fasta and printing in tab separated file...')    
    fhandleUni=gzip.open('uniprot_sprot.fasta.gz','rt')
    fhandleOutput=open('SwissProtIDGeneProteinMapping.csv','w')
    fhandleOutput.write('UniprotAcc\tUniprotID\tGene\tProtein\tOrganism\tSequence\n')
    for records in SeqIO.parse(fhandleUni,'fasta'):
        firstString=records.description.split()[0]     
        uniprotAcc=firstString.split('|')[1]
        uniprotID=firstString.split('|')[2]
        sequence=records.seq
        geneName='XXX';proteinName='YYY';organism='ZZZ'
        if 'GN=' in records.description:
            geneName=records.description.split('GN=')[1].split('PE=')[0]
        proteinName=' '.join(records.description.split('OS=')[0].split()[1:])
        if 'OS=' in records.description:
            organism=' '.join(records.description.split('OX=')[0].split('OS=')[1:])
        fhandleOutput.write(f'{uniprotAcc}\t{uniprotID}\t{geneName}\t{proteinName}\t{organism}\t{sequence}\n')
    fhandleUni.close()
    fhandleOutput.close()

def update_trembl():
    print('Reading Trembl fasta and printing in tab separated file...')
    fhandleUni=gzip.open('uniprot_trembl.fasta.gz','rt')
    fhandleOutput=open('TremblIDGeneProteinMapping.csv','w')
    fhandleOutput.write('UniprotAcc\tUniprotID\tGene\tProtein\tOrganism\tSequence\n')
    for records in SeqIO.parse(fhandleUni,'fasta'):
        firstString=records.description.split()[0]     
        uniprotAcc=firstString.split('|')[1]
        uniprotID=firstString.split('|')[2]
        sequence=records.seq
        geneName='XXX';proteinName='YYY';organism='ZZZ'
        if 'GN=' in records.description:
            geneName=records.description.split('GN=')[1].split('PE=')[0]
        proteinName=' '.join(records.description.split('OS=')[0].split()[1:])
        if 'OS=' in records.description:
            organism=' '.join(records.description.split('OX=')[0].split('OS=')[1:])
        fhandleOutput.write(f'{uniprotAcc}\t{uniprotID}\t{geneName}\t{proteinName}\t{organism}\t{sequence}\n')
    fhandleUni.close()
    fhandleOutput.close()
    

if __name__=='__main__':
    download_swissprot()
    download_trembl()
    update_swissprot()
    update_trembl()