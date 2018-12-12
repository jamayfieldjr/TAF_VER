
# https://www.wrh.noaa.gov/mesowest/timeseries.php?sid=KMEM&wfo=wrh&num=1&banner=NONE&hfmetars=1&rawobs=1
#https://stackoverflow.com/questions/43375884/how-to-print-dictionary-values-line-by-line-in-python
#https://www.codecademy.com/en/forum_questions/535b88039c4e9dd3cd001003

import pytaf
import re 

#taf = pytaf.TAF("TAF KIAH 090530Z 0906/1012 02006KT 3SM BR OVC004 FM090700 02008KT 4SM SHRA BR VCSH OVC007 TEMPO 0909/0913 2SM -TSRA BKN007 OVC040CB FM091300 01014G21KT 4SM -RA BR OVC006 FM091800 01017G25KT 6SM -DZ BR BKN012 OVC040 FM092200 01014G23KT P6SM BKN035 OVC090 FM100000 02013KT P6SM SCT120 SCT250 FM100700 03008KT P6SM BKN100 ")


taf = pytaf.TAF("TAF AMD CYMX 090209Z 0902/0924 VRB03KT P6SM BKN010 OVC020 TEMPO 0902/0904 3SM SHRA BR OVC004 PROB40 0902/0904 VRB15G25KT 11/2SM TSRA BR OVC003CB FM090400 VRB03KT P6SM OVC010 TEMPO 0904/0905 VRB15G25KT 11/2SM TSRA BR OVC003CB FM090500 VRB03KT 3/4SM BR OVC002 TEMPO 0905/0911 2SM -SHRA BR OVC003 PROB30 0905/0911 1/4SM FG VV001 FM091100 VRB03KT WS010/24030KT 3/4SM -SHRA BR OVC002 PROB30 0911/0914 VRB15G30KT 2SM TSRA BR OVC004CB FM091400 24010G20KT 4SM -SHRA BR OVC005 FM091600 24010G20KT P6SM SCT008 OVC015 BECMG 0922/0924 23008KT")

#taf = pytaf.TAF("TAF EIDW 120505Z 1206/1306 VRB03KT 9999 FEW007 BKN020 TEMPO 1206/1209 VRB03KT TEMPO 1206/1212 4000 -RADZ BR BKN007 PROB40 TEMPO 1208/1211 2000 BKN003 PROB30 TEMPO 1208/1211 0800 FG BKN001 BECMG 1209/1211 14006KT BECMG 1211/1213 13011KT TEMPO 1212/1223 -RA BKN012 BECMG 1215/1217 15018G30KT PROB30 TEMPO 1216/1220 5000 -RA BKN010 BECMG 1217/1219 15020G35KT BECMG 1219/1221 14025G41KT")

# correct way 
# 06,07,09,13,18,22,00,07
# 07,13,13,18,22,00,07,12

#TAF KIAH 090530Z 0906/1012 02006KT 3SM BR OVC004 OVC010
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

#print(weather_groups[2]["wind"])
#print(weather_groups[8]["windshear"])
#print(weather_groups[1]["visibility"])
print(weather_groups[0]["clouds"])
#print(weather_groups[0]["vertical_visibility"])
#print(weather_groups[0]["weather"])

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

""" For Loop For Wind Group """

for i in range(0,len(weather_groups)):
  #print(i)
  res1=[]
  res2=[]
  res3=[]
  res4=[]
  res5=[]
  res6=[]
  windtf = weather_groups[i]["wind"]
  #print(windtf)
  if not windtf:
    #print("A")
    res1 = "-9999"
    res2 = "-9999"
    res3 = "-9999"
    res4 = "-9999"
    res5 = "-9999"
    res6 = "-9999"
    results1.append(res1)
    results2.append(res2)
    results3.append(res3)
    results4.append(res4)
    results5.append(res5)
    results6.append(res6)
  else:
   res1 = weather_groups[i]["wind"]
   #print(weather_groups[i]["wind"]["direction"])
   res2 = (weather_groups[i]["wind"]["direction"])
   res3 = weather_groups[i]["wind"]["speed"]
   res5 = weather_groups[i]["wind"]["unit"]
   results1.append(res1)
   results2.append(res2)
   results3.append(res3)
   results5.append(res5)
   if not weather_groups[i]["wind"]["gust"]:
    res4 = "-9999" 
   else:
    res4 = weather_groups[i]["wind"]["gust"]
  results4.append(res4)
  windtf = []

wind_group = results1
wind_group_dd = results2 
wind_group_ff = results3 
wind_group_gg = results4
wind_group_units = results5

#print(wind_group_dd)
#print(wind_group_ff)
#print(wind_group_gg)

""" For Loop For Wind Shear Group """

# windshear None 
# {'altitude': '010', 'direction': '240', 'speed': '30', 'unit': 'KT'}

for i in range(0,len(weather_groups)):
  #print(i)
  res1=[]
  res2=[]
  res3=[]
  res4=[]
  windsheartf = weather_groups[i]["windshear"]
  #print(windtf)
  if not windtf:
    #print("A")
    res1 = "-9999"
    res2 = "-9999"
    res3 = "-9999"
    res4 = "-9999"
    res5 = "-9999"
    res6 = "-9999"
    results1.append(res1)
    results2.append(res2)
    results3.append(res3)
    results4.append(res4)
    results5.append(res5)
    results6.append(res6)
  else:
   res1 = weather_groups[i]["windshear"]["altitude"]
   #print(weather_groups[i]["wind"]["direction"])
   res2 = (weather_groups[i]["windshear"]["direction"])
   res3 = weather_groups[i]["windshear"]["speed"]
   res5 = weather_groups[i]["windshear"]["unit"]
   results1.append(res1)
   results2.append(res2)
   results3.append(res3)
   results4.append(res4)
  windsheartf = []

windshear_group_altitude = results1
windshear_group_dd = results2 
windshear_group_ff = results3 
windshear_group_units = results4


""" For Loop For Visibility Group """

#  None 
#or
# {'more': None, 'range': '3', 'unit': 'SM'}

for i in range(0,len(weather_groups)):
  #print(i)
  res1=[]
  res2=[]
  res3=[]
  visibilitytf = weather_groups[i]["visibility"]
  #print(windtf)
  if not visibilitytf:
    #print("A")
    res1 = "-9999"
    res2 = "-9999"
    res3 = "-9999"
    res4 = "-9999"
    res5 = "-9999"
    res6 = "-9999"
    results1.append(res1)
    results2.append(res2)
    results3.append(res3)
  else:
   res1 = weather_groups[i]["visibility"]["more"]
   #print(weather_groups[i]["wind"]["direction"])
   res2 = weather_groups[i]["visibility"]["range"]
   res5 = weather_groups[i]["visibility"]["unit"]
   results1.append(res1)
   results2.append(res2)
   results3.append(res3)
  visibilitytf = []

visibility_group_more= results1
visibility_group_range = results2 
visibility_group_units = results3 



