
Files from USha
Lakara-Dhatu-Arrangement.xlsx
Lakara-Vakyas-New.xlsx
Vibhaktis- Dev Scr.xlsx

# tsv conversion by Google Drive
Lakara_Sheet1.tsv
Vibhaktis_Sheet1.tsv  # from Lakara-Vakyas-New.xlsx

# unix line-endings
python ../unixify.py Lakara_Sheet1.tsv lakara_deva.tsv
python ../unixify.py Vibhaktis_Sheet1.tsv vibhakti_deva.tsv

# manually change '/' to '-' (the / is problematic for transcoder)
# convert to slp1
python ../convert.py deva slp1 lakara_deva.tsv lakara_slp1.tsv
# check round-trip
python ../convert.py slp1 deva Lakara_slp1.tsv temp.tsv
echo "check round-trip"
diff lakara_deva.tsv temp.tsv | wc -l
------
python ../convert.py deva slp1 vibhakti_deva.tsv vibhakti_slp1.tsv
# check round-trip
python ../convert.py slp1 deva Vibhakti_slp1.tsv temp.tsv  
diff vibhakti_deva.tsv temp.tsv | wc -l

# =====================================================
gaRa  DAtu law low ...
BvAdigaRaH paW praTamapuruzaH paW

python extract1.py lakara_slp1.tsv lakara1_slp1.tsv
901 lines written to lakara1_slp1.tsv
# 900 forms, 1 title line

python ../convert.py slp1 deva lakara1_slp1.tsv lakara1_deva.tsv

TODO 1
old header
gaRa : lakAra : puruza : vacanam : rUpam

new header 
DAtu : gaRa : upagraha : lakAra : puruza : vacanam : rUpam

TODO 2
old:
BvAdi : law : praTama : eka : paWati
new:
BU : BvAdi : parasmEpada : law : praTama : eka : paWati

    11:BU BvAdi : law : praTama : eka : paWati
    101: ad adAdi : law : praTama : eka : yAti
    191:hu : juhotyAdi : law : praTama : eka : jahAti
    281:kzip divAdi : law : praTama : eka : kzipyati
    371:Ap : svAdi : law : praTama : eka : Apnoti
    461:liK : tudAdi : law : praTama : eka : liKati
    551:yuj : ruDAdi : law : praTama : eka : yunakti
    641:kf : tanAdi : law : praTama : eka : karoti
    731:krI : kryAdi : law : praTama : eka : krIRAti

# =====================================================

python extract2.py vibhakti_slp1.tsv vibhakti1_slp1.tsv

181 lines read from vibhakti_slp1.tsv
line 1 has 27 fields
All lines have 27 fields

# nAmaviDA -> nAmapada  
18 groups
