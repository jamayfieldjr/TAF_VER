import pytaf

taf = pytaf.TAF("TAF KIAH 090530Z 0906/1012 02006KT 3SM BR OVC004 FM090700 02008KT 4SM SHRA BR VCSH OVC007 TEMPO 0909/0913 2SM -TSRA BKN007 OVC040CB FM091300 01014G21KT 4SM -RA BR OVC006 FM091800 01017G25KT 6SM -DZ BR BKN012 OVC040 FM092200 01014G23KT P6SM BKN035 OVC090 FM100000 02013KT P6SM SCT120 SCT250 FM100700 03008KT P6SM BKN100 =")

weather_groups=(taf._weather_groups)

#print(list(text[1]))
#decoder = pytaf.Decoder(taf)
#text.get('header')

res =[]
results=[] 

#def taftime(results):
# for values in text: 
#   res=(weather_groups[values]['header'])
#   results = res
#   return results



print(weather_groups[2]['header'])
if (weather_groups[6]['header']['type']))=='FM'
fromhrs=((weather_groups[6]['header']['from_hours']))
fromday=((weather_groups[6]['header']['from_date']))
tillhrs=((weather_groups[6]['header']['from_hours']))
tillday=((weather_groups[6]['header']['from_date']))
#print(type(text))
#next(item for item in text if item["name"] == "header")
# Print the contents of the dictionary
#print(d) 

# Get the entry from a dictionary using the key
#print(d['cat']



#attrs = dir(taf)
#all_examples = [attrs]
#print(all_examples)

