# coding=utf-8
""" extract2.py
"""
from __future__ import print_function
import sys, re, codecs

fieldsep = '\t'

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

def checkfields(lines,nfields):
 for iline,line in enumerate(lines):
  parts = line.split(fieldsep)
  nparts = len(parts)
  lnum = iline + 1
  if iline == 0:
   print(f'line {lnum} has {nparts} fields')
  if nparts != nfields:
   print(f'ERROR: line {lnum} has {nparts} fields')
   exit(1)
 print(f'All lines have {nfields} fields')
def cross_product(list1,list2):
 # list of all pairs (pair is a tuple)
 ans = []
 for a in list1:
  for b in list2:
   # tuple can be key to a dictionary; list cannot
   val = (a,b)  
   ans.append(val)
 return ans
viBaktis = ['praTamA','dvitIyA','tftIyA','caturTI','paYcamI','zazWI','saptamI','samboDana',]
vacanas = ['eka', 'dvi', 'bahu']

def get_viBakti_vacanam_pairs():
 ans = cross_product(viBaktis,vacanas)
 return ans
viBakti_vacanam_pairs = get_viBakti_vacanam_pairs()

if False:
 for p in viBakti_vacanam_pairs:
  print(p)
 exit(1)


class Declension:
 def __init__(self,prAtipadika,nAmapada,liNgam):
  self.prAtipadika = prAtipadika
  self.nAmapada = nAmapada
  self.liNgam = liNgam
  self.table = {}
  for viBakti_vacanam in viBakti_vacanam_pairs:
   self.table[viBakti_vacanam]  = '' # default value

def extract_lakaras(parts):
 lakaras_in = parts[1:]  # first field is blank
 lakaras = []
 for x in lakaras_in:
  assert x.endswith('lakAraH')
  y = x.replace('lakAraH','')
  lakaras.append(y)
 return lakaras

def update_declensions(d,parts,gaRa,lakaras,puruza,vacanam):
 for ipart,part in enumerate(parts[1:]):
  lakara = lakaras[ipart]
  part = part.strip()
  subparts = part.split(' ')
  verb = subparts[-1]  # verb at end of sentence
  d[(gaRa,lakara)].table[(puruza,vacanam)] = verb

def step1_helper1(group):
 # (nAmapada,liNgam,vacanam)
 firstline = group[0]
 fields = firstline.split(fieldsep)
 field0 = fields[0]
 data = field0.split(' - ')
 ndata = len(data)
 assert ndata in (2,3)
 if ndata == 2:
  nAmapada = 'nAma'
  data1 = data
 else:
  nAmapada = 'sarvanAma'
  assert data[0] == 'sarvanAmaSabdAH'
  data1 = data[1:]
 liNgam_in,vacanam_in = data1
 liNgam = liNgam_in.replace('liNgam','')
 liNgam = liNgam.strip()
 vacanam = vacanam_in.replace('vacanam','')
 if liNgam not in ('puM','strI','napuMsaka'):
  print(f'ERROR liNgam = "{liNgam}"')
  exit(1)
 assert vacanam in('eka','dvi','bahu')
 return (nAmapada,liNgam,vacanam)

def update_decls_nAma(decls,group,parms):
 (nAmapada,liNgam,vacanam) = parms
 temp = group[1].split(fieldsep)
 prAtipadikas = temp[1:]
 if False:
  for i,p in enumerate(prAtipadikas):
   print(i,p)
  exit(1)
 for prAtipadika in prAtipadikas:
  key = (prAtipadika,liNgam)
  if key not in decls:
   # initialize
   decl = Declension(prAtipadika,nAmapada,liNgam)
   decls[key] = decl
 
 for iviBakti,line in enumerate(group[2:]):
  parts = line.split(fieldsep)
  viBakti0 = parts[0] 
  if viBakti0.startswith('samboDana'):
   viBakti= 'samboDana'
  else:
   viBakti = viBakti0.replace('viBaktiH','')
  viBakti1 = viBaktis[iviBakti]
  if viBakti != viBakti1:
   print(f'viBakti error: {viBakti} != {viBakti1}')
   print(f'line = {line}')
   exit(1)
  assert len(parts[1:]) == len(prAtipadikas)
  for i,rUpam in enumerate(parts[1:]):
   prAtipadika = prAtipadikas[i]
   key = (prAtipadika,liNgam)
   decl = decls[key]
   viBakti_vacanam = (viBakti,vacanam)
   decl.table[viBakti_vacanam] = rUpam
              
def update_decls_sarvanAma(decls,group,parms):
 (nAmapada,liNgam,vacanam) = parms
 temp = group[0].split(fieldsep)
 prAtipadikas = temp[1:]
 if False:
  for i,p in enumerate(prAtipadikas):
   print(i,p)
  exit(1)
 for prAtipadika in prAtipadikas:
  key = (prAtipadika,liNgam)
  if key not in decls:
   # initialize
   decl = Declension(prAtipadika,nAmapada,liNgam)
   decls[key] = decl
 
 for iviBakti,line in enumerate(group[1:]):
  parts = line.split(fieldsep)
  viBakti0 = parts[0] 
  if viBakti0.startswith('samboDana'):
   viBakti= 'samboDana'
  else:
   viBakti = viBakti0.replace('viBaktiH','')
  viBakti1 = viBaktis[iviBakti]
  if viBakti != viBakti1:
   print(f'viBakti error: {viBakti} != {viBakti1}')
   print(f'liNgam = {liNgam}')
   print(f'line = {line}')
   exit(1)
  assert len(parts[1:]) == len(prAtipadikas)
  for i,rUpam in enumerate(parts[1:]):
   prAtipadika = prAtipadikas[i]
   key = (prAtipadika,liNgam)
   if key not in decls:
    print(f'{key} not in decls; the keys so far are')
    for key in decls:
     print(key)
    exit(1)
   decl = decls[key]
   viBakti_vacanam = (viBakti,vacanam)
   decl.table[viBakti_vacanam] = rUpam

def step1(groups,nfields):
 decls = {} # keys are prAtipadika
 for igroup,group in enumerate(groups):
  (nAmapada,liNgam,vacanam) = step1_helper1(group)
  parms = (nAmapada,liNgam,vacanam)
  if nAmapada == 'nAma':
   update_decls_nAma(decls,group,parms)
  elif nAmapada == 'sarvanAma':
   update_decls_sarvanAma(decls,group,parms)
  else:
   print(f'ERROR unknown nAmapada {nAmapada}')
   exit(1)
  #if igroup == 0:
  # print('quitting after group 0')
  # break
 return decls

def make_outarr(decls):
 outarr = []
 # title line
 titles = ['prAtipadika','nAmapada','liNgam','viBakti','vacanam','rUpam']
 title = fieldsep.join(titles)
 outarr.append(title)
 for key in declensions:
  (prAtipadika,liNgamkey) = key
  decl = decls[key]
  nAmapada = decl.nAmapada
  liNgam = decl.liNgam
  assert liNgam == liNgamkey
  table = decl.table
  for tabkey in table: # (viBakti,vacanam)
   rUpam = table[tabkey]
   rUpam = rUpam.strip()
   (viBakti,vacanam) = tabkey
   outparts = [prAtipadika,nAmapada,liNgam,viBakti,vacanam,str(rUpam)]
   out = fieldsep.join(outparts)
   outarr.append(out)
 return outarr

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
  groups.append(current)

 return groups

def check_groups_1(groups):
 for group in groups:
  firstline = group[0]
  firstparts = firstline.split(fieldsep)
  firstfield = firstparts[0]
  print(len(group),firstfield)
  
def init_groups(lines):
 emptyline = lines[11]
 lines1 = lines[1:] # skip first line
 groups = split_into_groups(lines1,emptyline)
 check_groups_1(groups)
 return groups
 
if __name__ == "__main__":
 filein=sys.argv[1]  # tab-delimited index file
 fileout = sys.argv[2]
 lines = read_lines(filein)
 nfields = 27
 checkfields(lines,nfields)
 groups = init_groups(lines)
 print(len(groups),'groups')
 
 declensions = step1(groups,nfields)
 outarr = make_outarr(declensions)
 write_lines(fileout,outarr)

 
 
