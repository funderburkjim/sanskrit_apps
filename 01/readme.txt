
* Files from USha
Lakara-Dhatu-Arrangement.xlsx
Lakara-Vakyas-New.xlsx
Vibhaktis- Dev Scr.xlsx

# 
Lakara_Sheet1.tsv
Vibhaktis_Sheet1.tsv  # from Lakara-Vakyas-New.xlsx

* lakara_deva.tsv and vibhakti_deva.tsv
# unix line-endings
python ../unixify.py Lakara_Sheet1.tsv lakara_deva.tsv
python ../unixify.py Vibhaktis_Sheet1.tsv vibhakti_deva.tsv

* lakara_slp1.tsv 
# manually change '/' to '-' (the / is problematic for transcoder)
# convert to slp1
python ../convert.py deva slp1 lakara_deva.tsv lakara_slp1.tsv
# check round-trip
python ../convert.py slp1 deva Lakara_slp1.tsv temp.tsv
echo "check round-trip"
diff lakara_deva.tsv temp.tsv | wc -l

* vibhakti_slp1.tsv
python ../convert.py deva slp1 vibhakti_deva.tsv vibhakti_slp1.tsv
# check round-trip
python ../convert.py slp1 deva Vibhakti_slp1.tsv temp.tsv  
diff vibhakti_deva.tsv temp.tsv | wc -l

* lakara1_slp1.tsv

python extract1.py lakara_slp1.tsv lakara1_slp1.tsv
901 lines written to lakara1_slp1.tsv
# 900 forms, 1 title line

* lakara1_deva.tsv
python ../convert.py slp1 deva lakara1_slp1.tsv lakara1_deva.tsv

* TODO copies to html_01
cp lakara1_deva.tsv ../html_01/data/lakara.tsv
cp vibhakti1b_deva.tsv ../html_01/data/vibhakti.tsv
cp subj_verb_deva.tsv ../html_01/data/subj_verb.tsv
cp sarvanAma_deva.tsv ../html_01/data/sarvanAma.tsv
cp antyavarRa_deva.tsv ../html_01/data/antyavarRa.tsv

* vibhakti1_slp1.tsv  (replaced by vibhakti1a_slp1.tsv below)
# 2353 lines written to vibhakti1_slp1.tsv
# Revision (skip declensions with prAtipadika == emptystring
2281 lines written to vibhakti1_slp1.tsv

python extract2.py vibhakti_slp1.tsv vibhakti1_slp1.tsv

181 lines read from vibhakti_slp1.tsv
line 1 has 27 fields
All lines have 27 fields
18 groups

* vibhakti1a_slp1.tsv
cp vibhakti1_slp1.tsv vibhakti1b_slp1.tsv
Edit vibhakti1a_slp1.tsv
1a.  eka prAvfz -> eka prAvfw  (cf. PWG)
1b. prAvfw (prAtipadika) -> prAvfz
  
* vibhakti1a_deva.tsv (see vibhakti1b_slp1.tsv)
python ../convert.py slp1 deva vibhakti1a_slp1.tsv vibhakti1a_deva.tsv  

* subj_verb_slp1.tsv
python subj_verb.py vibhakti1b_slp1.tsv lakara1_slp1.tsv subj_verb_slp1.tsv
2257 lines read from vibhakti1b_slp1.tsv
901 lines read from lakara1_slp1.tsv
100 verb keys
94 subject keys
27600 sentences
27601 lines written to subj_verb_slp1.tsv

* subj_verb_deva.tsv
python ../convert.py slp1 deva subj_verb_slp1.tsv subj_verb_deva.tsv
27601 lines converted
* sarvanAma_slp1.tsv
# extract sarvanAma lines from from vibhakti1a_slp1.tsv 
# keep: 
#  title line
#  lines with nAmapada == 'sarvanAma'
python make_sarvanAma.py vibhakti1b_slp1.tsv sarvanAma_slp1.tsv
2257 lines read from vibhakti1b_slp1.tsv
769 lines written to sarvanAma_slp1.tsv



* sarvanAma_deva.tsv
python ../convert.py slp1 deva sarvanAma_slp1.tsv sarvanAma_deva.tsv
769 lines converted

* antya_work_slp1.tsv (preparation for antyavarRa_slp1.tsv)
  from Google Sheets "Vibhaktis- Dev Scr"
python ../convert.py deva slp1 antya_work_deva.tsv antya_work_slp1.tsv

Edit antya_work_slp1.tsv
1. cakArAnta -> c
2. prAvfw -> prAvfz
3. some other unknown changes
mv antya_work_deva.tsv temp_unused_antya_work_deva.tsv

* antya_work1_slp1.tsv (preparation for antyavarRa_slp1.tsv)
python antya_work1.py antya_work_slp1.tsv antya_work1_slp1.tsv
27 lines read from antya_work_slp1.tsv
9 groups
62 cases

3 fields : (ending,prAtipadika,liNgam)

# python ../convert.py slp1 deva antya_work1_slp1.tsv antya_work1_deva.tsv

----------------------------------
* missing values in vibhakti1a_slp1.tsv

** Sreyas in vibhakti1a_slp1.tsv

Sreyas puM is missing bahu 
Sreyas	nAma	puM	praTamA	eka	SreyAn
Sreyas	nAma	puM	praTamA	dvi	SreyAMsO
Sreyas	nAma	puM	praTamA	bahu	
Sreyas	nAma	puM	dvitIyA	eka	SreyAMsam
Sreyas	nAma	puM	dvitIyA	dvi	SreyAMsO
Sreyas	nAma	puM	dvitIyA	bahu	
Sreyas	nAma	puM	tftIyA	eka	SreyasA
Sreyas	nAma	puM	tftIyA	dvi	SreyoByAm
Sreyas	nAma	puM	tftIyA	bahu	
Sreyas	nAma	puM	caturTI	eka	Sreyase
Sreyas	nAma	puM	caturTI	dvi	SreyoByAm
Sreyas	nAma	puM	caturTI	bahu	
Sreyas	nAma	puM	paYcamI	eka	SreyasaH
Sreyas	nAma	puM	paYcamI	dvi	SreyoByAm
Sreyas	nAma	puM	paYcamI	bahu	
Sreyas	nAma	puM	zazWI	eka	SreyasaH
Sreyas	nAma	puM	zazWI	dvi	SreyasoH
Sreyas	nAma	puM	zazWI	bahu	
Sreyas	nAma	puM	saptamI	eka	Sreyasi
Sreyas	nAma	puM	saptamI	dvi	SreyasoH
Sreyas	nAma	puM	saptamI	bahu	
Sreyas	nAma	puM	samboDana	eka	Sreyan
Sreyas	nAma	puM	samboDana	dvi	SreyAMsO
Sreyas	nAma	puM	samboDana	bahu	
** Iyas in vibhakti1a_slp1.tsv
Iyas	nAma	puM	praTamA	eka	
Iyas	nAma	puM	praTamA	dvi	
Iyas	nAma	puM	praTamA	bahu	SreyAMsaH
Iyas	nAma	puM	dvitIyA	eka	
Iyas	nAma	puM	dvitIyA	dvi	
Iyas	nAma	puM	dvitIyA	bahu	SreyasaH
Iyas	nAma	puM	tftIyA	eka	
Iyas	nAma	puM	tftIyA	dvi	
Iyas	nAma	puM	tftIyA	bahu	SreyoBiH
Iyas	nAma	puM	caturTI	eka	
Iyas	nAma	puM	caturTI	dvi	
Iyas	nAma	puM	caturTI	bahu	SreyoByaH
Iyas	nAma	puM	paYcamI	eka	
Iyas	nAma	puM	paYcamI	dvi	
Iyas	nAma	puM	paYcamI	bahu	SreyoByaH
Iyas	nAma	puM	zazWI	eka	
Iyas	nAma	puM	zazWI	dvi	
Iyas	nAma	puM	zazWI	bahu	SreyasAm
Iyas	nAma	puM	saptamI	eka	
Iyas	nAma	puM	saptamI	dvi	
Iyas	nAma	puM	saptamI	bahu	Sreyassu
Iyas	nAma	puM	samboDana	eka	
Iyas	nAma	puM	samboDana	dvi	
Iyas	nAma	puM	samboDana	bahu	SreyAMsaH

**
** ap in vibhakti1a_slp1.tsv  This agrees with Huet (except for ,, in praTamA eka)
ap	nAma	strI	praTamA	eka	,,
ap	nAma	strI	praTamA	dvi	
ap	nAma	strI	praTamA	bahu	ApaH
ap	nAma	strI	dvitIyA	eka	
ap	nAma	strI	dvitIyA	dvi	
ap	nAma	strI	dvitIyA	bahu	apaH
ap	nAma	strI	tftIyA	eka	
ap	nAma	strI	tftIyA	dvi	
ap	nAma	strI	tftIyA	bahu	adBiH
ap	nAma	strI	caturTI	eka	
ap	nAma	strI	caturTI	dvi	
ap	nAma	strI	caturTI	bahu	adByaH
ap	nAma	strI	paYcamI	eka	
ap	nAma	strI	paYcamI	dvi	
ap	nAma	strI	paYcamI	bahu	adByaH
ap	nAma	strI	zazWI	eka	
ap	nAma	strI	zazWI	dvi	
ap	nAma	strI	zazWI	bahu	apAm
ap	nAma	strI	saptamI	eka	
ap	nAma	strI	saptamI	dvi	
ap	nAma	strI	saptamI	bahu	apsu
ap	nAma	strI	samboDana	eka	
ap	nAma	strI	samboDana	dvi	
ap	nAma	strI	samboDana	bahu	ApaH

** complete Sreyas declension, using Iyas above 
 agrees with Huet except for saptamI bahu, where Huet has SreyaHsu
Sreyas	nAma	puM	praTamA	eka	SreyAn
Sreyas	nAma	puM	praTamA	dvi	SreyAMsO
Sreyas	nAma	puM	praTamA	bahu	SreyAMsaH
Sreyas	nAma	puM	dvitIyA	eka	SreyAMsam
Sreyas	nAma	puM	dvitIyA	dvi	SreyAMsO
Sreyas	nAma	puM	dvitIyA	bahu	SreyasaH
Sreyas	nAma	puM	tftIyA	eka	SreyasA
Sreyas	nAma	puM	tftIyA	dvi	SreyoByAm
Sreyas	nAma	puM	tftIyA	bahu	SreyoBiH
Sreyas	nAma	puM	caturTI	eka	Sreyase
Sreyas	nAma	puM	caturTI	dvi	SreyoByAm
Sreyas	nAma	puM	caturTI	bahu	SreyoByaH
Sreyas	nAma	puM	paYcamI	eka	SreyasaH
Sreyas	nAma	puM	paYcamI	dvi	SreyoByAm
Sreyas	nAma	puM	paYcamI	bahu	SreyoByaH
Sreyas	nAma	puM	zazWI	eka	SreyasaH
Sreyas	nAma	puM	zazWI	dvi	SreyasoH
Sreyas	nAma	puM	zazWI	bahu	SreyasAm
Sreyas	nAma	puM	saptamI	eka	Sreyasi
Sreyas	nAma	puM	saptamI	dvi	SreyasoH
Sreyas	nAma	puM	saptamI	bahu	Sreyassu
Sreyas	nAma	puM	samboDana	eka	Sreyan
Sreyas	nAma	puM	samboDana	dvi	SreyAMsO
Sreyas	nAma	puM	samboDana	bahu	SreyAMsaH

** Sreyas puM declension from Huet
pumAn : eka : dvi : bahu
praTamA : SreyAn : SreyAMsO : SreyAMsaH
samboDanam : Sreyan : SreyAMsO : SreyAMsaH
dvitIyA : SreyAMsam : SreyAMsO : SreyasaH
tftIyA : SreyasA : SreyoByAm : SreyoBiH
caturTI : Sreyase : SreyoByAm : SreyoByaH
paYcamI : SreyasaH : SreyoByAm : SreyoByaH
zazWI : SreyasaH : SreyasoH : SreyasAm
saptamI : Sreyasi : SreyasoH : SreyaHsu

** ap strI declension from Huet
strI : eka : dvi : bahu
praTamA :  :  : ApaH
samboDanam :  :  : ApaH
dvitIyA :  :  : apaH
tftIyA :  :  : adBiH
caturTI :  :  : adByaH
paYcamI :  :  : adByaH
zazWI :  :  : apAm
saptamI :  :  : apsu

* vibhakti1b_slp1.tsv
 cp vibhakti1a_slp1.tsv vibhakti1b_slp1.tsv
edit vibhakti1b_slp1.tsv
 1. add missing values to Sreyas puM (by using Iyas puM above)
 2. remove Iyas
 3. make ap praTamA eka  to empty string
* vibhakti1b_deva.tsv
python ../convert.py slp1 deva vibhakti1b_slp1.tsv vibhakti1b_deva.tsv  
also revise files that depend on vibhakti1b_slp1.tsv
 antyavarRa_slp1.tsv
 antyavarRa_deva.tsv
 sarvanAma_slp1.tsv
 sarvanAma_deva.tsv
 subj_verb_slp1.tsv
 subj_verb_deva.tsv
and copy files to html_01/data/
* antyavarRa_slp1.tsv
python make_antyavarRa.py vibhakti1b_slp1.tsv antya_work1_slp1.tsv antyavarRa_slp1.tsv
2257 lines read from vibhakti1b_slp1.tsv
62 lines read from antya_work1_slp1.tsv
1489 lines written to antyavarRa_slp1.tsv




*  antyavarRa_deva.tsv
python ../convert.py slp1 deva antyavarRa_slp1.tsv antyavarRa_deva.tsv


* THE END


