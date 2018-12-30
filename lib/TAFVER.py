#import libraries
import pytaf
import re 

# Defining TAF_VER Object 

class TAFVER(object):

   """ TAFVER parser """
    def __init__(self,string):
     taf = pytaf.TAF(taf_input)
     weather_groups=taf._weather_groups
     taf_header = taf._taf_header

    def time_vector_function(self,string):
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
     """Creation of variables """
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
         res1 = weather_groups[i]["header"]["from_hours"]
         res2 = weather_groups[i]["header"]["from_date"]
         res3 = weather_groups[i]["header"]["till_hours"]
         res4 = weather_groups[i]["header"]["till_date"]
         results5.append(res1)
         results6.append(res2)
         results7.append(res3)
         results8.append(res4)
        elif re.search(regex,fmtype):
         res1 = weather_groups[i]["header"]["from_hours"]
         res2 = weather_groups[i]["header"]["from_date"]
         res3 = weather_groups[i]["header"]["till_hours"]
         res4 = weather_groups[i]["header"]["till_date"]
         results5.append(res1)
         results6.append(res2)
         results7.append(res3)
         results8.append(res4)
        elif fmtype =="BECMG":
         res1 = weather_groups[i]["header"]["from_hours"]
         res2 = weather_groups[i]["header"]["from_date"]
         res3 = weather_groups[i]["header"]["till_hours"]
         res4 = weather_groups[i]["header"]["till_date"]
         results5.append(res1)
         results6.append(res2)
         results7.append(res3)
         results8.append(res4)
         fmtype=[] 

         """FROM results into list1 and changing it into integars"""
         list1 = results1 
         list1 = [int(x) for x in list1]
         list1.insert(0,int(vfhrs))
         
         """ resutls1 is the from hours
             results2 is the from date   
             results3 repativate 
             results4 repativate 
             resutls5 is the start tempo,prob,becoming hours 
             results6 is the start tempo,prob,becoming date  
             resutls7 is the end tempo,prob,becoming hours 
             results8 is the end tempo,prob,becoming date"""  
         
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
         
         """For loop results7 i.e. till time changing it into integars"""
         res=[]
         resb=[]
         
         for i in results7:
          res = int(i)
          resb.append(res)
         
         """Indexing resutls5 results7 i.e. start,till time"""
         
         idxb=[index for index,value in enumerate(resb) if value > -9]
         list4 = [i for i in resb if i > -9]
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

       def wind_group_function(self,string):
        """Creation of Variables"""
        results1 = list()
        results2 = list()
        results3 = list()
        results4 = list()
        results5 = list()
        results6 = list()

        """ For Loop For Wind Group """

        for i in range(0,len(weather_groups)):
         res1=[]
         res2=[]
         res3=[]
         res4=[]
         res5=[]
         res6=[]
         windtf = weather_groups[i]["wind"]
         if not windtf:
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
    
         """ For Loop For Wind Shear Group """
         # windshear None 
         # {'altitude': '010', 'direction': '240', 'speed': '30', 'unit': 'KT'}

         for i in range(0,len(weather_groups)):
          res1=[]
          res2=[]
          res3=[]
          res4=[]
          windsheartf = weather_groups[i]["windshear"]

         def vertical_visibility_group_function(self,string):
         """Creation of varaibiles """
         results1 = list()
         """ For Loop For Vertical Visibility"""
         
         for i in range(0,len(weather_groups)):
          res1=[]
          res2=[]
          results3 =[]
          results4 =[]
          vvtf = weather_groups[i]["vertical_visibility"]
         
           if not vvtf:
            res1 = ["-9999"]
            results1.append(res1)
           else:
            res1 = weather_groups[i]["vertical_visibility"]
            results1.append([res1])
            vvtf = []
            vertical_visibility_group = results1
            print(vertical_visibility_group)
            
           if not windtf:
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

         def visibility_group_function(self,string):
         """ For Loop For Visibility Group """
         #  None 
         #or
         # {'more': None, 'range': '3', 'unit': 'SM'}
          for i in range(0,len(weather_groups)):
           res1=[]
           res2=[]
           res3=[]
           visibilitytf = weather_groups[i]["visibility"]
            
           if not visibilitytf:
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
            res2 = weather_groups[i]["visibility"]["range"]
            res5 = weather_groups[i]["visibility"]["unit"]
            results1.append(res1)
            results2.append(res2)
            results3.append(res3)
            visibilitytf = []
            visibility_group_more= results1
            visibility_group_range = results2 
            visibility_group_units = results3 

             def vertical_visibility_group_function(self,string):
              """Creation of varaibiles """
              
              results1 = list()
              results2 = list()
              print(weather_groups[0]["clouds"][0]["layer"])
              print(len(weather_groups[0]["clouds"]))
              
              """ For Loop For Clouds """
               
               for i in range(0,len(weather_groups)):
                res1=[]
                res2=[]
                results3 =[]
                results4 =[]
                cloudstf = weather_groups[i]["clouds"]
                
               if not cloudstf:
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
