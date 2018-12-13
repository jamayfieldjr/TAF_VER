
# https://www.wrh.noaa.gov/mesowest/timeseries.php?sid=KMEM&wfo=wrh&num=1&banner=NONE&hfmetars=1&rawobs=1
#https://stackoverflow.com/questions/43375884/how-to-print-dictionary-values-line-by-line-in-python
#https://www.codecademy.com/en/forum_questions/535b88039c4e9dd3cd001003

import pytaf
import re 

#taf = pytaf.TAF("TAF KIAH 090530Z 0906/1012 02006KT 3SM BR OVC004 FM090700 02008KT 4SM SHRA BR VCSH OVC007 TEMPO 0909/0913 2SM -TSRA BKN007 OVC040CB FM091300 01014G21KT 4SM -RA BR OVC006 FM091800 01017G25KT 6SM -DZ BR BKN012 OVC040 FM092200 01014G23KT P6SM BKN035 OVC090 FM100000 02013KT P6SM SCT120 SCT250 FM100700 03008KT P6SM BKN100 ")


taf = pytaf.TAF("TAF AMD CYMX 090209Z 0902/0924 VRB03KT P6SM BKN010 OVC020 TEMPO 0902/0904 3SM SHRA BR OVC004 PROB40 0902/0904 VRB15G25KT 11/2SM TSRA BR OVC003CB FM090400 VRB03KT P6SM OVC010 TEMPO 0904/0905 VRB15G25KT 11/2SM TSRA BR OVC003CB FM090500 VRB03KT 3/4SM BR OVC002 TEMPO 0905/0911 2SM -SHRA BR OVC003 PROB30 0905/0911 1/4SM FG VV001 FM091100 VRB03KT WS010/24030KT 3/4SM -SHRA BR OVC002 PROB30 0911/0914 VRB15G30KT 2SM TSRA BR OVC004CB FM091400 24010G20KT 4SM -SHRA BR OVC005 FM091600 24010G20KT P6SM SCT008 OVC015 BECMG 0922/0924 23008KT")

#taf = pytaf.TAF("TAF EIDW 120505Z 1206/1306 VRB03KT 9999 FEW007 BKN020 TEMPO 1206/1209 VRB03KT TEMPO 1206/1212 4000 -RADZ BR BKN007 PROB40 TEMPO 1208/1211 2000 BKN003 PROB30 TEMPO 1208/1211 0800 FG BKN001 BECMG 1209/1211 14006KT BECMG 1211/1213 13011KT TEMPO 1212/1223 -RA BKN012 BECMG 1215/1217 15018G30KT PROB30 TEMPO 1216/1220 5000 -RA BKN010 BECMG 1217/1219 15020G35KT BECMG 1219/1221 14025G41KT")


weather_groups=taf._weather_groups

"""Creation of varaibiles """

results1 = list()
results2 = list()

print(weather_groups[0]["clouds"][0]["layer"])
print(len(weather_groups[0]["clouds"]))
""" For Loop For Clouds """

for i in range(0,len(weather_groups)):
  #print(i)
  res1=[]
  res2=[]
  results3 =[]
  results4 =[]
  cloudstf = weather_groups[i]["clouds"]
  #print(windtf)
  if not cloudstf:
    #print("A")
    res1 = ["-9999"]
    res2 = ["-9999"]
    results1.append(res1)
    results2.append(res2)
  else:
    for k in range(0,len(weather_groups[i]["clouds"])):
     res1 = weather_groups[i]["clouds"][k]["layer"]
     res2 = weather_groups[i]["clouds"][k]["ceiling"]
     results3.append(res1)
     results4.append(res2)
    results1.append(results3)
    results2.append(results4)
  cloudtf = []

cloud_group_height = results1
cloud_group_layer = results2 
print(cloud_group_height)
print(cloud_group_layer)


