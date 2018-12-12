
# https://www.wrh.noaa.gov/mesowest/timeseries.php?sid=KMEM&wfo=wrh&num=1&banner=NONE&hfmetars=1&rawobs=1
#https://stackoverflow.com/questions/43375884/how-to-print-dictionary-values-line-by-line-in-python
#https://www.codecademy.com/en/forum_questions/535b88039c4e9dd3cd001003

import pytaf
import re 

#taf = pytaf.TAF("TAF KIAH 090530Z 0906/1012 02006KT 3SM BR OVC004 FM090700 02008KT 4SM SHRA BR VCSH OVC007 TEMPO 0909/0913 2SM -TSRA BKN007 OVC040CB FM091300 01014G21KT 4SM -RA BR OVC006 FM091800 01017G25KT 6SM -DZ BR BKN012 OVC040 FM092200 01014G23KT P6SM BKN035 OVC090 FM100000 02013KT P6SM SCT120 SCT250 FM100700 03008KT P6SM BKN100 ")


taf = pytaf.TAF("TAF AMD CYMX 090209Z 0902/0924 VRB03KT P6SM OVC010 TEMPO 0902/0904 3SM SHRA BR OVC004 PROB40 0902/0904 VRB15G25KT 11/2SM TSRA BR OVC003CB FM090400 VRB03KT P6SM OVC010 TEMPO 0904/0905 VRB15G25KT 11/2SM TSRA BR OVC003CB FM090500 VRB03KT 3/4SM BR OVC002 TEMPO 0905/0911 2SM -SHRA BR OVC003 PROB30 0905/0911 1/4SM FG VV001 FM091100 VRB03KT WS010/24030KT 3/4SM -SHRA BR OVC002 PROB30 0911/0914 VRB15G30KT 2SM TSRA BR OVC004CB FM091400 24010G20KT 4SM -SHRA BR OVC005 FM091600 24010G20KT P6SM SCT008 OVC015 BECMG 0922/0924 23008KT")

# correct way 
# 06,07,09,13,18,22,00,07
# 07,13,13,18,22,00,07,12

#TAF KIAH 090530Z 0906/1012 02006KT 3SM BR OVC004 
#0#FM090700 02008KT 4SM SHRA BR VCSH OVC007 
#1#TEMPO 0909/0913 2SM -TSRA BKN007 OVC040CB 
#2#FM091300 01014G21KT 4SM -RA BR OVC006 
#3#FM091800 01017G25KT 6SM -DZ BR BKN012 OVC040 
#4#FM092200 01014G23KT P6SM BKN035 OVC090 
#5#FM100000 02013KT P6SM SCT120 SCT250 
#6#FM100700 03008KT P6SM BKN100 =

# 02 02 02 04 04 05 05 05 11 11 14 16 22
# 04 04 04 05 05 11 11 11 14 14 16 22 24

#TAF EIDW 120505Z 1206/1306 VRB03KT 9999 FEW007 BKN020
#TEMPO 1206/1209 VRB03KT
#TEMPO 1206/1212 4000 -RADZ BR BKN007
#PROB40 TEMPO 1208/1211 2000 BKN003
#PROB30 TEMPO 1208/1211 0800 FG BKN001
#BECMG 1209/1211 14006KT
#BECMG 1211/1213 13011KT
#TEMPO 1212/1223 -RA BKN012
#BECMG 1215/1217 15018G30KT
#PROB30 TEMPO 1216/1220 5000 -RA BKN010
#BECMG 1217/1219 15020G35KT
#BECMG 1219/1221 14025G41KT =


#TAF AMD CYMX 090209Z 0902/0924 VRB03KT P6SM OVC010 
#TEMPO 0902/0904 3SM SHRA BR OVC004 
#PROB40 0902/0904 VRB15G25KT 11/2SM TSRA BR OVC003CB 
#FM090400 VRB03KT P6SM OVC010 
#TEMPO 0904/0905 VRB15G25KT 11/2SM TSRA BR OVC003CB 
#FM090500 VRB03KT 3/4SM BR OVC002 
#TEMPO 0905/0911 2SM -SHRA BR OVC003 
#PROB30 0905/0911 1/4SM FG VV001 
#FM091100 VRB03KT WS010/24030KT 3/4SM -SHRA BR OVC002 
#PROB30 0911/0914 VRB15G30KT 2SM TSRA BR OVC004CB 
#FM091400 24010G20KT 4SM -SHRA BR OVC005 
#FM091600 24010G20KT P6SM SCT008 OVC015 
#BECMG 0922/0924 23008KT RMK NXT FCST BY 090600Z 

weather_groups=taf._weather_groups


taf_header = taf._taf_header

"""Origin Minutes, Hours, and Day within the taf_header(_taf_header attribute)"""

oringalmin=taf_header['origin_minutes']
orginalhrs=taf_header['origin_hours']
orginalday=taf_header['origin_date']

"""Valid From Minutes, Hours, and Day within the taf_header(_taf_header attribute)"""

vfhrs=taf_header['valid_from_hours']
vfday=taf_header['valid_from_date']

"""Valid Till  Minutes, Hours, and Day within the taf_header(_taf_header attribute)"""

vthrs=taf_header['valid_till_hours']
vtday=taf_header['valid_till_date']

"""Number of Lines (nof ) in Terminal Aerodrome Forecast"""

"""Creation of varaibiles """

#res1 : fromhrs
#res2 : fromday
#res3 : tillhrs
#res4 : tillday

results1 = list()
results2 = list()
results3 = list()
results4 = list()
results5 = list()
results6 = list()
results7 = list()
results8 = list()

"""For Loop with assoicated if and if else to  Pull Each Time (DD/HH:MM) in Each From Tempo Prob Becming Line in the Terminal Aerodrome Forecast"""
regex = r"PROB\d{0,2}"


for i in range(1,len(weather_groups)):
  res1=[]
  res2=[]
  res3=[]
  res4=[] 
  fmtype=[]
  fmtype = str(weather_groups[i]["header"]["type"])
  if fmtype == "FM":
   #print("A")
   res1 = weather_groups[i]["header"]["from_hours"]
   res2 = weather_groups[i]["header"]["from_date"]
   res3 = weather_groups[i]["header"]["from_hours"]
   res4 = weather_groups[i]["header"]["from_date"]
   results1.append(res1)
   results2.append(res2)
   results3.append(res3)
   results4.append(res4)
   results5.append("-9")
   results6.append("-9")
   results7.append("-9")
   results8.append("-9")
  elif fmtype == "TEMPO":
   #print("B")
   res1 = weather_groups[i]["header"]["from_hours"]
   res2 = weather_groups[i]["header"]["from_date"]
   res3 = weather_groups[i]["header"]["till_hours"]
   res4 = weather_groups[i]["header"]["till_date"]
   results5.append(res1)
   results6.append(res2)
   results7.append(res3)
   results8.append(res4)
  elif re.search(regex,fmtype):
   #print("C")
   res1 = weather_groups[i]["header"]["from_hours"]
   res2 = weather_groups[i]["header"]["from_date"]
   res3 = weather_groups[i]["header"]["till_hours"]
   res4 = weather_groups[i]["header"]["till_date"]
   results5.append(res1)
   results6.append(res2)
   results7.append(res3)
   results8.append(res4)
  elif fmtype =="BECMG":
   #print("D")
   res1 = weather_groups[i]["header"]["from_hours"]
   res2 = weather_groups[i]["header"]["from_date"]
   res3 = weather_groups[i]["header"]["till_hours"]
   res4 = weather_groups[i]["header"]["till_date"]
   results5.append(res1)
   results6.append(res2)
   results7.append(res3)
   results8.append(res4)
  fmtype=[] 

#print(results1)
#print(results5)
#print(results7)

#PROB\d{0,2}

"""FROM results into list1 and changing it into integars"""

list1 = results1 
list1 = [int(x) for x in list1]
list1.insert(0,int(vfhrs))
#print(list1)
# resutls1 is the from hours 
# results2 is the from date  
# results3 repativate 
# results4 repativate 

# resutls5 is the start tempo,prob,becoming hours 
# results6 is the start tempo,prob,becoming date  
# resutls7 is the end tempo,prob,becoming hours 
# results8 is the end tempo,prob,becoming date  

"""For loop results5 i.e. start time  changing it into integars"""

res=[]
resa=[]
for i in results5:
  res = int(i)
  resa.append(res)

"""Indexing resutls5 results7 i.e. start,till time"""

idxa=[index for index,value in enumerate(resa) if value > -9]

list2 = [i for i in resa if i > -9]

idx = [int(x) for x in idxa]
print(list1,list2,idx)
"""Building List of Starting Time of Each Line in the Terminal Aerodrome Forecast"""

additive = [1] * (len(idx))

for index in range(len(idx)):
 list1.insert(idx[index]+additive[index],list2[index]) 

begintime = list1

#print(begintime)

"""For loop results7 i.e. till time changing it into integars"""

res=[]
resb=[]
for i in results7:
  res = int(i)
  resb.append(res)

#print(resb)

"""Indexing resutls5 results7 i.e. start,till time"""

idxb=[index for index,value in enumerate(resb) if value > -9]

list4 = [i for i in resb if i > -9]
#print(list3)
idx = [int(x) for x in idxb]

"""Building List of End Time of Each Line in the Terminal Aerodrome Forecast"""

list3 = results1 
list3.insert(len(list3),(vthrs))
print(list3)
list3 = [int(x) for x in list3]
print(list3,list4,idx)
additive = [1] * (len(idx))

for index in range(len(idx)):
 list3.insert(idx[index]+additive[index],list4[index]) 
 
endtime = list3
print(begintime)
print(endtime)

alltime=(begintime,endtime)
print(alltime)

