# coding=utf-8
""" make_antyavarRa.py
"""
from __future__ import print_function
import sys, re, codecs

fieldsep = '\t'
vacanam_fields = ['eka','dvi','bahu']
sfields =  ['prAtipadika','nAmapada','liNgam',
            'viBakti','vacanam','rUpam']
subj_ekeys = ['prAtipadika','liNgam']
viBakti_fields = ['praTamA','dvitIyA','tftIyA','caturTI','paYcamI','zazWI','saptamI','samboDana',]
   
def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 print(f'{len(lines)} lines read from {filein}')
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"lines written to",fileout)

def make_outarr_helper(parts):
 [prAtipadika,nAmapada,liNgam,
            viBakti,vacanam,rUpam] = parts
 prAtipadika = prAtipadika.strip() # 'Atman ' -> 'Atman'
 antyas = [ 'अ', 'इ', 'उ', 'ऋ', 'ऐ', 'ओ', 'औ',
            'च्', 'ज्',
            'त्', 'द्', 'ध्', 'न्',
            'श्', 'स्', 'ह्',
            'तृच्', 'अत्', 'इन्', 'वत्', 'मत्', 'वस्', 'ईयस्', 'आ', 'ई', 'ऊ',]

 c = prAtipadika[-1] # last character of prAtipadika
 antyavarRa = c
 newparts = [prAtipadika,nAmapada,antyavarRa, liNgam,
            viBakti,vacanam,rUpam]
 newline = fieldsep.join(newparts)
 return newline

def antya_endings(lines):
 d = {}
 for line in lines:
  parts = line.split(fieldsep)
  (ending,prAtipadika,liNgam_abbrv) = parts
  if liNgam_abbrv  == 'napuM':
   liNgam = 'napuMsaka'
  else:
   liNgam = liNgam_abbrv
  key = (prAtipadika,liNgam)
  d[key] = ending
 return d

def make_outarr(lines,antyad):
 antya_fieldnames = ['antya', 'prAtipadika','liNgam']
 viBakti_fieldnames =  ['prAtipadika','nAmapada','liNgam',
            'viBakti','vacanam','rUpam']
# add new field antya = antyavarRa
 merge_fieldnames = ['prAtipadika','antya','nAmapada','liNgam',
            'viBakti','vacanam','rUpam']
  
 outarr = []  # returned
 title = fieldsep.join(merge_fieldnames)
 outarr.append(title)
 for iline,line in enumerate(lines[1:]):
  [prAtipadika,nAmapada,liNgam,
            viBakti,vacanam,rUpam] = line.split(fieldsep) 
  if nAmapada != 'nAma':
   # no sarvanAmas 
   continue
  antya_key = (prAtipadika,liNgam)
  if antya_key not in antyad:
   print(f'antya_key ERROR. {antya_key} at line')
   print(line)
   exit(1)
  antya = antyad[antya_key] 
  merge_fields = [prAtipadika,antya,nAmapada,liNgam,
            viBakti,vacanam,rUpam]
  merge_line = fieldsep.join(merge_fields)
  outarr.append(merge_line)
 return outarr

if __name__ == "__main__":
 filein=sys.argv[1]  # vibhakti1_slp1.tsv
 filein1 = sys.argv[2] # antya_work1_slp1.tsv
 fileout = sys.argv[3]
 slines = read_lines(filein) 
 alines = read_lines(filein1)
 antya_d = antya_endings(alines)
 outarr = make_outarr(slines,antya_d)
 write_lines(fileout,outarr)

