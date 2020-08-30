#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 16:55:45 2020

@author: vivekmodi
"""
from Bio import SearchIO
import pandas as pd
from datetime import datetime
import sys

def read_psiblast(psiblast_result):
    df=pd.DataFrame()
    print("Reading psiblast output...")
    fhandle_psiblast=SearchIO.read(psiblast_result,"blast-xml")

    index=0
    hit_accession_list=list()
    specie_list=['HUMAN']       # All the species to be included in the output

    for hits in fhandle_psiblast:        #hits object does not have any evalue, only hsps have evalues

        for hsp in hits.hsps:
            if hsp.evalue<5.0 and hsp.aln_span>125:       # Above certain cutoff and length

                if hits.accession in hit_accession_list:    #to make sure that the sequences which are split into two hsps are not repeated in the output
                    continue
                hit_accession_list.append(hits.accession)

                if any(specie in hsp.hit_description.upper() for specie in specie_list):     #any in an inbuilt function

                    if hsp.hit_description.find('|')!=-1:       #Skip fusion proteins; returns position of substring, -1 means not found
                        continue

                    chain_length=hsp.hit_description.split()[1]
                    method=hsp.hit_description.split()[2]
                    reso=hsp.hit_description.split()[3]
                    rvalue=hsp.hit_description.split()[4]
                    free_rvalue=hsp.hit_description.split()[5]
                    protein=' '.join(hsp.hit_description.split('<')[0].split()[7:])
                    uniprot_name=str(hsp.hit_description.split('<')[1].split('>')[0].split('(')[0])
                    #sequence=''.join(str(hsp.hit.seq).split('-'))       #this prints incomplete sequence, only corressponding to the alignment
                    specie=str(hsp.hit_description.split('[')[1].split(']')[0])

                    if rvalue=='NA':
                        rvalue=999;
                    if free_rvalue=='NA':
                        free_rvalue=999;
                    if reso=='NA'    :
                        reso=999

                    try:
                        residue_range=(hsp.hit_description.split("<")[1].split(">")[0].split("(")[1]).split(")")[0]     #assign structure residue numbers to dictionary
                        res1=int(residue_range.split("-")[0])       #These residue numbers in pdbaa come from sifts database
                        res2=int(residue_range.split("-")[1])
                    except IndexError:
                        res1=0;res2=0
                        continue      #skip the structures which do not have residue information in pdbaa


                    df.at[index,'PDBid']=hsp.hit_id
                    df.at[index,'Protein']=protein
                    df.at[index,'UniprotID']=uniprot_name
                    df.at[index,'ChainLen']=int(chain_length)
                    df.at[index,'StrBegin']=int(res1)
                    df.at[index,'StrEnd']=int(res2)
                    df.at[index,'Specie']=specie
                    df.at[index,'Resolution']=round(float(reso),2)
                    df.at[index,'Method']=method
                    df.at[index,'Rvalue']=round(float(rvalue),2)
                    df.at[index,'FreeRvalue']=round(float(free_rvalue),2)
                    index=index+1

    return df

if __name__ == '__main__':
     psiblast_result=sys.argv[1]
     today=str(datetime.now())[0:10].strip()
     df=read_psiblast(psiblast_result)
     df.to_excel(f'df_psiblast_{today}.xlsx',index=False)   #Write excel and csv
     df.to_csv(f'df_psiblast_{today}.csv',sep='\t',index=False)
