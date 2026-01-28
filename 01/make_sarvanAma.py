# coding=utf-8
""" make_sarvanAma.py
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


def make_outarr(lines):
 fields =  ['prAtipadika','nAmapada','liNgam',
            'viBakti','vacanam','rUpam']

 attrs = lines[0].split(fieldsep) # returned
 if attrs != fields:
  print(f'make_outarr error')
  print(f'attrs = {attrs}')
  print(f'fields= {fields}')
  exit(1)
 nfields = len(fields)
 index_nAmapada = 1
 outarr = []  # returned
 outarr.append(lines[0])
 for iline,line in enumerate(lines[1:]):
  parts = line.split(fieldsep)
  # nAmapada field value index
  nAmapada = parts[index_nAmapada]
  if nAmapada != 'sarvanAma':
   continue
  outarr.append(line)
 return outarr
if __name__ == "__main__":
 filein=sys.argv[1]  # tab-delimited index file
 fileout = sys.argv[2]
 slines = read_lines(filein) #  vibhakti1
 outarr = make_outarr(slines)
 write_lines(fileout,outarr)

