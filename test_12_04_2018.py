# https://www.wrh.noaa.gov/mesowest/timeseries.php?sid=KMEM&wfo=wrh&num=1&banner=NONE&hfmetars=1&rawobs=1
#https://stackoverflow.com/questions/43375884/how-to-print-dictionary-values-line-by-line-in-python
#https://www.codecademy.com/en/forum_questions/535b88039c4e9dd3cd001003

import pytaf

#taf = pytaf.TAF("TAF KIAH 090530Z 0906/1012 02006KT 3SM BR OVC004 FM090700 02008KT 4SM SHRA BR VCSH OVC007 TEMPO 0909/0913 2SM -TSRA BKN007 OVC040CB FM091300 01014G21KT 4SM -RA BR OVC006 FM091800 01017G25KT 6SM -DZ BR BKN012 OVC040 FM092200 01014G23KT P6SM BKN035 OVC090 FM100000 02013KT P6SM SCT120 SCT250 FM100700 03008KT P6SM BKN100 =")


taf = pytaf.TAF("TAF AMD CYMX 090209Z 0902/0924 VRB03KT P6SM OVC010 TEMPO 0902/0904 3SM SHRA BR OVC004 PROB40 0902/0904 VRB15G25KT 11/2SM TSRA BR OVC003CB FM090400 VRB03KT P6SM OVC010 TEMPO 0904/0905 VRB15G25KT 11/2SM TSRA BR OVC003CB FM090500 VRB03KT 3/4SM BR OVC002 TEMPO 0905/0911 2SM -SHRA BR OVC003 PROB30 0905/0911 1/4SM FG VV001 FM091100 VRB03KT WS010/24030KT 3/4SM -SHRA BR OVC002 PROB30 0911/0914 VRB15G30KT 2SM TSRA BR OVC004CB FM091400 24010G20KT 4SM -SHRA BR OVC005 FM091600 24010G20KT P6SM SCT008 OVC015 BECMG 0922/0924 23008KT RMK NXT FCST BY 090600Z =")
decoder = pytaf.Decoder(taf)
print(decoder.decode_taf())


#TAF KIAH 090530Z 0906/1012 02006KT 3SM BR OVC004 
0#FM090700 02008KT 4SM SHRA BR VCSH OVC007 
1#TEMPO 0909/0913 2SM -TSRA BKN007 OVC040CB 
2#FM091300 01014G21KT 4SM -RA BR OVC006 
3#FM091800 01017G25KT 6SM -DZ BR BKN012 OVC040 
4#FM092200 01014G23KT P6SM BKN035 OVC090 
5#FM100000 02013KT P6SM SCT120 SCT250 
6#FM100700 03008KT P6SM BKN100 =

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

for i in range(len(weather_group)):
 print(weather_groups[i]["header"])

#res1 : fromhrs
#res2 : fromday
#res3 : tillhrs
#res4 : tillday

results1 = list()
results2 = list()
results3 = list()
results4 = list()

#print(len(weather_groups))

#print(weather_groups)

for i in range(1,7):
  res1=[]
  res2=[]
  res3=[]
  res4=[] 
  fmtype=[]
  fmtype = str(weather_groups[i]["header"]["type"])
  print(fmtype)
  if fmtype == "FM":
   #print("A")
   res1 = weather_groups[i]["header"]["from_hours"]
   res2 = weather_groups[i]["header"]["from_date"]
   res3 = "NaN"
   res4 = "NaN"
   results1.append(res1)
   results2.append(res2)
   results3.append(res3)
   results4.append(res4)
  elif fmtype == "TEMPO":
   #print("B")
   res1 = weather_groups[i]["header"]["from_hours"]
   res2 = weather_groups[i]["header"]["from_date"]
   res3 = weather_groups[i]["header"]["till_hours"]
   res4 = weather_groups[i]["header"]["till_date"]
   results1.append(res1)
   results2.append(res2)
   results3.append(res3)
   results4.append(res4)
  elif fmtype =="PROB":
   res1 = weather_groups[i]["header"]["from_hours"]
   res2 = weather_groups[i]["header"]["from_date"]
   res3 = weather_groups[i]["header"]["till_hours"]
   res4 = weather_groups[i]["header"]["till_date"]
   results1.append(res1)
   results2.append(res2)
   results3.append(res3)
   results4.append(res4)
  elif fmtype =="BECMNG":
   res1 = weather_groups[i]["header"]["from_hours"]
   res2 = weather_groups[i]["header"]["from_date"]
   res3 = weather_groups[i]["header"]["till_hours"]
   res4 = weather_groups[i]["header"]["till_date"]
   results1.append(res1)
   results2.append(res2)
   results3.append(res3)
   results4.append(res4)
  fmtype=[] 

print(results1)
endtime = (results1[1:len(results1)])
endtime.append(vthrs)
print(endtime)
#print(results2)
#print(results3)
#print(results4)
