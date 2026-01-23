# coding=utf-8
""" subj_verb.py
"""
from __future__ import print_function
import sys, re, codecs

fieldsep = '\t'
vacanam_fields = ['eka','dvi','bahu']
sfields =  ['prAtipadika','nAmapada','liNgam',
            'viBakti','vacanam','rUpam']
vfields = ['DAtu','gaRa','upagraha',
           'lakAra','puruza','vacanam','rUpam']
verb_ekeys = ['DAtu','gaRa','upagraha','lakAra']
subj_ekeys = ['prAtipadika','liNgam']
viBakti_fields = ['praTamA','dvitIyA','tftIyA','caturTI','paYcamI','zazWI','saptamI','samboDana',]

sen_fields = ['prAtipadika','liNgam',
              'DAtu','gaRa','upagraha','lakAra',
              'puruza', # same as 'viBakti'
              'vacanam', # in both subj and verb
              'vAkyam',
              ]
puruza_fields = ['praTama', 'maDyama', 'uttama']     
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

def get_viBakti_vacanam_pairs():
 ans = cross_product(viBakti_fields,vacanam_fields)
 return ans
viBakti_vacanam_pairs = get_viBakti_vacanam_pairs()
           
def make_outarr(sentences):
 outarr = []
 # title line
 titles = ['prAti','liNg',
              'DAtu','gaRa','upag','lak',
              'puru', 
              'vac', 
              '__vAkyam__',
              ]
 title = fieldsep.join(titles)
 outarr.append(title)
 ikey = 0
 dbg = False
 for key in sentences:
  sentence = sentences[key]
  if dbg: print('sentence=',sentence)
  ikey = ikey + 1
  outparts = list(key)
  outparts[4] = outparts[4][0:4]
  outparts[6] = outparts[4][0:4]
  #outparts[1] = outparts[1].replace('napuMsaka','napuM')
  outparts[1] = outparts[1][0:4]
  outparts[5] = outparts[5][0:4]
  outparts[3] = outparts[3].replace('Adi','')
  #outparts.insert(0,sentence)
  
  outparts.append(sentence)
  if dbg: print('outparts=',outparts)
  if dbg and (ikey == 10):
   break
  out = fieldsep.join(outparts)
  outarr.append(out)
 return outarr

def dictrecs(lines,fields):
 # header_line
 attrs = lines[0].split(fieldsep) # returned
 assert attrs == fields
 nfields = len(fields)
 recs = []  # returned
 for line in lines[1:]:
  parts = line.split(fieldsep)
  assert len(parts) == nfields
  d = {}
  for i in range(nfields):
   fieldname = fields[i]
   fieldval = parts[i]
   d[fieldname] = fieldval
  recs.append(d)
 return recs

def init_groups(recs,parms):
 d = {}
 for drec in recs:
  keyarr = []
  for parm in parms:
   # parm is an attribute name
   value = drec[parm]
   keyarr.append(value)
  key = tuple(keyarr) # python dict supports tuple keys
  if key not in d:
   d[key] = []
  d[key].append(drec)
 return d

def get_praTamA_vacanam(sdict,prAtipadika_in):
 ans = {}
 for skey in sdict:
  srecs = sdict[skey]
  (prAtipadika,liNgam) = skey
  if prAtipadika != prAtipadika_in:
   continue
  for sd in srecs:
   viBakti = sd['viBakti']
   if viBakti != 'praTamA':
    continue
   vacanam = sd['vacanam']
   rUpam = sd['rUpam']
   ans[vacanam] = rUpam
 return ans

def get_conjugations(vdict):
 conjdict = {}
 for vkey in vdict:
  DAtu,gaRa,upagraha,lakAra = vkey
  vrecs = vdict[vkey]
  conj = {}
  for vd in vrecs:
   puruza = vd['puruza']
   vacanam = vd['vacanam']
   conjkey = (puruza,vacanam)
   conj[conjkey] = vd['rUpam']
  conjdict[vkey] = conj
 return conjdict

def subj_verb_join(subj,verb):
 # subj, verb in slp1 transliteration
 # apply sandhi rules as needed
 vowels = 'aAiIuUfFxXeEoO'
 if subj.endswith('m'):
  if verb[0] not in vowels:
   # assume first character of verb is a constant
   # change last character of subj to M (anusvAra)
   subj = subj[0:-1] + 'M'
 ans = subj + ' ' + verb
 return ans
def get_sentence_vacanams(sdict,viBakti_in):
 ans = {}
 for skey in sdict:
  srecs = sdict[skey]
  (prAtipadika,liNgam) = skey
  if prAtipadika in ('yuzmad','asmad'):
   continue
  vacanams = {}
  for sd in srecs:
   viBakti = sd['viBakti']
   if viBakti != 'praTamA':
    continue
   vacanam = sd['vacanam']
   rUpam = sd['rUpam']
   vacanams[vacanam] = rUpam
  ans[skey] = vacanams
 return ans
def make_sentences(sdict,vdict):
 # get the eka, dvi, bahu forms of 'yuzmad' and 'asmad'
 yuzmad_forms = get_praTamA_vacanam(sdict,'yuzmad')
 asmad_forms = get_praTamA_vacanam(sdict,'asmad')
 dbg = False
 if dbg: print(yuzmad_forms)
 if dbg: print(asmad_forms)
 conjs = get_conjugations(vdict)
 if dbg: print(f'{len(conjs)} conjugations')
 praTamA_vacanams = get_sentence_vacanams(sdict,'praTamA')
 if dbg: print(f'{len(praTamA_vacanams)} praTamA_vacanams')
 # xxxx
 sentences = {}
 for skey in praTamA_vacanams:
  (prAtipadika,liNgam) = skey
  vacanams = praTamA_vacanams[skey]
  if dbg: print(f'skey = {skey}')
  if dbg: print(f'vacanams = {vacanams}')
  for conjkey in conjs:
   DAtu, gaRa, upagraha, lakAra = conjkey
   conj = conjs[conjkey]
   if dbg: print(f'conjkey = {conjkey}')
   if dbg: print(f'conj = {conj}')
   """
skey=('rAma','puM')
vacanams={'eka':'rAmaH','dvi':'rAmO','bahu':'rAmAH'}
conjkey=('paW','BvAdi','parasmEpada','law')
conj={('praTama','eka'):'paWati',('praTama','dvi'):
'paWataH',('praTama','bahu'):'paWanti',('maDyama','ek
a'):'paWasi',('maDyama','dvi'):'paWaTaH',('maDyama',
'bahu'):'paWaTa',('uttama','eka'):'paWAmi',('uttama',
'dvi'):'paWAvaH',('uttama','bahu'):'paWAmaH'}
"""
   #print('just checking')
   # make a sentence for
   
   for puruza_field in puruza_fields:
    for vacanam_field in vacanam_fields:
     puruza_vacanam = (puruza_field,vacanam_field)
     if puruza_vacanam not in conj:
      # Does this happen?
      continue
     verb = conj[puruza_vacanam]
     if puruza_field == 'praTama':
      subj = vacanams[vacanam_field]
     elif puruza_field == 'maDyama':
      subj = yuzmad_forms[vacanam_field]
      continue
     elif puruza_field == 'uttama':
      subj = asmad_forms[vacanam_field]
      continue
     sentence_val = subj_verb_join(subj,verb)
     sentence_key = skey + conjkey + puruza_vacanam
     if dbg: print(f'sentence_key = {sentence_key}')
     if dbg: print(f'sentence_val = {sentence_val}')
     sentences[sentence_key] = sentence_val
  
 return sentences
if __name__ == "__main__":
 filein1=sys.argv[1]  # tab-delimited index file
 filein2=sys.argv[2]  # tab-delimited index file
 fileout = sys.argv[3]
 slines = read_lines(filein1) # subject - vibhakti1
 vlines = read_lines(filein2) # verb  lakara1
 # srecs is a list of dicts for each line of sline
 srecs = dictrecs(slines,sfields) 
 vrecs = dictrecs(vlines,vfields)
 vdict = init_groups(vrecs,verb_ekeys)
 vkeys = vdict.keys()
 print(len(vkeys),'verb keys')
 sdict = init_groups(srecs,subj_ekeys)
 skeys = sdict.keys()
 print(len(skeys),'subject keys')

 sentences = make_sentences(sdict,vdict)
 print(f'{len(sentences)} sentences')
 outarr = make_outarr(sentences)
 write_lines(fileout,outarr)

 
 
