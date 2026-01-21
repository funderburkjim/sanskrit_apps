"""convert.py
  Python example of transcoding
"""
from __future__ import print_function
import sys,codecs,re
sys.path.append('../')
import transcoder
transcoder.transcoder_set_dir('../transcoder')

def convert(filein,fileout,tranin,tranout):
 fp = codecs.open(filein,"r",'utf-8')
 fpout = codecs.open(fileout,"w",'utf-8')
 n=0;
 for x in fp:
  x = x.rstrip('\r\n')
  n=n+1
  y = transcoder.transcoder_processString(x,tranin,tranout)
  fpout.write("%s\n" % y)
 fp.close()
 fpout.close()
 print(n,"lines converted\n")
#
def test():
 x =  " देवाः "
 tranin = 'deva'
 tranout = 'slp1'
 y = transcoder.transcoder_processString(x,tranin,tranout)
 print(x,y)
 exit(1)

#-----------------------------------------------------
if __name__=="__main__":
 filein = sys.argv[3]
 fileout = sys.argv[4]
 tranin = sys.argv[1]
 tranout = sys.argv[2]
 convert(filein,fileout,tranin,tranout)


