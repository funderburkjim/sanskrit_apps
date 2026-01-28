# coding=utf-8
""" antya_work1.py
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

def split_into_groups(lines, sep):
 # courtesy Copilot
 groups = []
 current = []

 for line in lines:
  if line == sep:
   # End of current group
   if current:
    groups.append(current)
    current = []
  else:
   current.append(line)

 # Add the final group if it has content
 if current:
  print('split_into_groups finds a partial final group')
  groups.append(current)

 return groups


def align_groups(groups):
 d = {}
 recs = [] # returned
 for igroup,group in enumerate(groups):
  line1 = group[0]
  line2 = group[1]
  parts1 = line1.split(fieldsep)
  parts2 = line2.split(fieldsep)
  liNga_vac = parts1[0]
  assert liNga_vac == parts2[0]
  liNga,vac = liNga_vac.split('-')
  if vac != 'eka':
   continue
  endings = parts1[1:]
  prAtipadikas = parts2[1:]
  nprAtipadikas = len(prAtipadikas)
  for iending,ending in enumerate(endings):
   try:
    prAtipadika = prAtipadikas[iending]
   except:
    prAtipadika = None
    continue
   
   key = (ending,prAtipadika,liNga)  # return value
   if key in d:
    print(f'duplicate {key} ')
    exit(1)
   d[key] = liNga_vac
   recs.append(key)
 return recs
  
def make_outarr_helper(parts):
 [prAtipadika,nAmapada,liNgam,
            viBakti,vacanam,rUpam] = parts
 prAtipadika = prAtipadika.strip() # 'Atman ' -> 'Atman'
 c = prAtipadika[-1] # last character of prAtipadika
 antyavarRa = c
 newparts = [prAtipadika,nAmapada,antyavarRa, liNgam,
            viBakti,vacanam,rUpam]
 newline = fieldsep.join(newparts)
 return newline

def unused_make_outarr(lines):
 fields =  ['prAtipadika','nAmapada','liNgam',
            'viBakti','vacanam','rUpam']
 # add new field antyavarRa
 fields1 = ['prAtipadika','nAmapada', 'antyavarRa', 'liNgam',
            'viBakti','vacanam','rUpam']
 attrs = lines[0].split(fieldsep) # returned
 if attrs != fields:
  print(f'make_outarr error')
  print(f'attrs = {attrs}')
  print(f'fields= {fields}')
  exit(1)
 nfields = len(fields)
 nfields1 = len(fields1)
 index_nAmapada = 1
 outarr = []  # returned
 title = fieldsep.join(fields1)
 outarr.append(title)
 index_nAmapada = 1
 for iline,line in enumerate(lines[1:]):
  parts = line.split(fieldsep)
  # nAmapada field value index
  nAmapada = parts[index_nAmapada]
  if nAmapada != 'nAma':
   continue
  newline = make_outarr_helper(parts)
  outarr.append(newline)
 return outarr

def make_outarr(lines):
 fields =  ['prAtipadika','nAmapada','liNgam',
            'viBakti','vacanam','rUpam']
 # add new field antyavarRa
 fields1 = ['prAtipadika','nAmapada', 'antyavarRa', 'liNgam',
            'viBakti','vacanam','rUpam']
 # eka
 attrs = lines[0].split(fieldsep) # returned
 if attrs != fields:
  print(f'make_outarr error')
  print(f'attrs = {attrs}')
  print(f'fields= {fields}')
  exit(1)
 nfields = len(fields)
 nfields1 = len(fields1)
 index_nAmapada = 1
 outarr = []  # returned
 title = fieldsep.join(fields1)
 outarr.append(title)
 index_nAmapada = 1
 for iline,line in enumerate(lines[1:]):
  parts = line.split(fieldsep)
  # nAmapada field value index
  nAmapada = parts[index_nAmapada]
  if nAmapada != 'nAma':
   continue
  newline = make_outarr_helper(parts)
  outarr.append(newline)
 return outarr

if __name__ == "__main__":
 filein=sys.argv[1]  # antya_work.tsv
 fileout = sys.argv[2]
 slines = read_lines(filein) #
 # last line in group is empty in antya_work.tsv
 groups = split_into_groups(slines,'')
 print(len(groups),'groups')
 recs = align_groups(groups)

 #outarr = make_outarr(recs)
 outarr = []
 d = {}
 for rec in recs:
  (ending,prAtipadika,liNgam) = rec
  key = (prAtipadika,liNgam)
  if key not in d:
   d[key] = key
  else: 
   print('duplicate key:',key)
  out = fieldsep.join(rec)
  outarr.append(out)
 write_lines(fileout,outarr)

