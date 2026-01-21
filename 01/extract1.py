# coding=utf-8
""" extract1.py
"""
from __future__ import print_function
import sys, re, codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"lines written to",fileout)

def checkfields(lines,nfields):
 for iline,line in enumerate(lines):
  parts = line.split('\t')
  nparts = len(parts)
  lnum = iline + 1
  if iline == 0:
   print(f'line {lnum} has {nparts} fields')
  if nparts != nfields:
   print(f'ERROR: line {lnum} has {nparts} fields')
   exit(1)

def cross_product(list1,list2):
 # list of all pairs (pair is a tuple)
 ans = []
 for a in list1:
  for b in list2:
   # tuple can be key to a dictionary; list cannot
   val = (a,b)  
   ans.append(val)
 return ans
puruzas = ['praTama', 'maDyama', 'uttama']
vacanas = ['eka', 'dvi', 'bahu']

def get_puruza_vacana_pairs():
 ans = cross_product(puruzas,vacanas)
 return ans
puruza_vacanan_pairs = get_puruza_vacana_pairs()
#print(puruza_vacanan_pairs)
if False:
 for p in puruza_vacanan_pairs:
  print(p)
 exit(1)
 
class Conjugation:
 def __init__(self,gaRa,lakara):
  self.gaRa = gaRa
  self.lakara = lakara
  self.table = {}
  for puruza_vacanam in puruza_vacanan_pairs:
   self.table[puruza_vacanam]  = None

def extract_lakaras(parts):
 lakaras_in = parts[1:]  # first field is blank
 lakaras = []
 for x in lakaras_in:
  assert x.endswith('lakAraH')
  y = x.replace('lakAraH','')
  lakaras.append(y)
 return lakaras

def init_conjugations(conjugations,gaRa,lakaras):
 # initialize conjugation table for (gaRa, lakara)
 # conjugations is a dict
 for lakara in lakaras:
  conjugations[(gaRa,lakara)] = Conjugation(gaRa,lakara)
def get_vacanam_from_lnum(lnum):
 lnum1 = lnum % 13 
 if lnum1 in (3,7,11):
  vacanam = 'eka'
 elif lnum1 in (4,8,12):
  vacanam = 'dvi'
 elif lnum1 in (5,9,0):
  vacanam = 'bahu'
 else:
  vacanam = None
 return vacanam
def update_conjugations(d,parts,gaRa,lakaras,puruza,vacanam):
 for ipart,part in enumerate(parts[1:]):
  lakara = lakaras[ipart]
  part = part.strip()
  subparts = part.split(' ')
  verb = subparts[-1]  # verb at end of sentence
  d[(gaRa,lakara)].table[(puruza,vacanam)] = verb
 
def step1(lines,nfields):
 conjugations = {} # keys are tuples (gaRa, lakara)
 for iline,line in enumerate(lines):
  parts = line.split('\t')
  nparts = len(parts)
  if iline == 0:  # names of lakaras
   lakaras = extract_lakaras(parts)
   continue
  lnum = iline + 1
  if lnum == 15:
   pass
   #print(f'breaking at lnum={lnum}')
   #break
  if lnum % 13 == 2:  # gaRa
   gaRa_in = parts[0]
   gaRa = gaRa_in.replace('gaRaH','')
   init_conjugations(conjugations,gaRa,lakaras)
  if lnum % 13 in (3,7,11): # puruza
   puruza_in = parts[0]
   puruza = puruza_in.replace('puruzaH','')
  # get vacanam
  vacanam = get_vacanam_from_lnum(lnum)
  # print(f'chk: lnum={lnum}, vacanam={vacanam}')
  if vacanam != None:
   update_conjugations(
    conjugations,parts,gaRa,lakaras,puruza,vacanam)
 return conjugations

def make_outarr(conjugations):
 outarr = []
 # title line
 fieldsep = '\t'
 titles = ['gaRa','lakAra','puruza','vacanam','rUpam']
 title = fieldsep.join(titles)
 outarr.append(title)
 for gaRa,lakAra in conjugations:
  conjugation = conjugations[(gaRa,lakAra)]
  table = conjugation.table
  for tabkey in table: # (puruza,vacanam)
   verb = table[tabkey]
   (puruza,vacanam) = tabkey
   outparts = [gaRa,lakAra,puruza,vacanam,str(verb)]
   out = fieldsep.join(outparts)
   outarr.append(out)
 return outarr

def make_outarr1(lines):
 outarr = []
 fieldsep = '\t'
 titles = ['DAtu','gaRa','upagraha',
           'lakAra','puruza','vacanam','rUpam']
 title = fieldsep.join(titles)
 outarr.append(title)
 gaRa_to_DAtu = {
"BvAdi":"paW",
 "adAdi":"yA",
 "juhotyAdi":"hu",
 "divAdi":"kzip",
 "svAdi":"Ap",
 "tudAdi":"liK",
 "ruDAdi":"yuj",
 "tanAdi":"kf",
 "kryAdi":"krI",
 "curAdi":"kaT",
}
 
 for line in lines[1:]:
  parts = line.split(fieldsep)
  newparts = []
  gaRa = parts[0]
  DAtu = gaRa_to_DAtu[gaRa]
  upagraha = 'parasmEpada'
  newparts.append(DAtu)
  newparts.append(gaRa)
  newparts.append(upagraha)
  for part in parts[1:]:
   newparts.append(part)
  newline = fieldsep.join(newparts)
  outarr.append(newline)
 return outarr

if __name__ == "__main__":
 filein=sys.argv[1]  # tab-delimited index file
 fileout = sys.argv[2]
 lines = read_lines(filein)
 nfields = 11
 checkfields(lines,nfields)
 conjugations = step1(lines,nfields)
 outarr = make_outarr(conjugations)
 outarr1 = make_outarr1(outarr)
 write_lines(fileout,outarr1)

 
 
