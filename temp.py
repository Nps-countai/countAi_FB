# import required modules
import firebase_admin
from firebase_admin import db, credentials
import json
from datetime import datetime
import re

# Define regular expression patterns for the two timestamp formats
timestamp_pattern1 = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\+\d{2}:\d{2}"
timestamp_pattern2 = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{6}\+\d{2}:\d{2}"
timestamp_pattern3 = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}" 
timestamp_pattern4 = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}"

# authenticate to firebase
cred = credentials.Certificate("credential.json")
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
        "databaseURL": "https://coneui-default-rtdb.asia-southeast1.firebasedatabase.app/"
    })

ref = db.reference("/")


# retrieving data from root node
fbData = ref.get()

# with open("fbDat.json", "w+") as f:
# 	file_contents = json.dump(fbData,f, indent=2)

mill_list = []
for i in fbData:
    mill_list.append(i)
    
for i in mill_list:
    total_uv_Nondefect = 0
    total_uv_Defect = 0
    total_conetip_Nondefect = 0
    total_conetip_Defect = 0
    lastDay_uv_Defect = 0
    lastDay_uv_Nondefect = 0
    lastDay_conetip_Nondefect = 0
    lastDay_conetip_Defect = 0
    uv_date_dict = {}
    conetip_date_dict = {}
    
    # ConeTIP
    for c in fbData[i]['conetip']:
        date_obj = (datetime.strptime(c['timestamp'], "%Y-%m-%d %H:%M:%S%z") if re.match(timestamp_pattern1, c['timestamp']) else datetime.strptime(c['timestamp'], "%Y-%m-%d %H:%M:%S.%f%z"))
        # counting date
        if date_obj.date() in conetip_date_dict.keys():
            conetip_date_dict[date_obj.date()] += 1
        else:
            conetip_date_dict[date_obj.date()] =1
        # finding defects
        if c['selectedconetype'] == c['detectedconetype']:
            total_conetip_Nondefect += 1
        else:
            total_conetip_Defect += 1   
        
        
    # UV   
    for c in fbData[i]['uv']:
        # print(c['timestamp'])
        date_obj = (datetime.strptime(c['timestamp'], "%Y-%m-%d %H:%M:%S.%f") if re.match(timestamp_pattern4, c['timestamp']) else datetime.strptime(c['timestamp'], "%Y-%m-%d %H:%M:%S") )
        
        # counting date
        if date_obj.date() in uv_date_dict.keys():
            uv_date_dict[date_obj.date()] += 1
        else:
            uv_date_dict[date_obj.date()] =1
        
        # finding defects        
        if c['detecteduv'] == "False":
            total_uv_Nondefect += 1
        else:
            total_uv_Defect += 1
            
            
            
    recentdayUV = list(uv_date_dict.keys())[-1]
    recentdayUV
    print('UV last day : ',list(uv_date_dict.keys())[-1])    
    print('ConeTip last day : ',list(conetip_date_dict.keys())[-1])   
    
    for c in fbData[i]['conetip']:
        date_obj = (datetime.strptime(c['timestamp'], "%Y-%m-%d %H:%M:%S%z") if re.match(timestamp_pattern1, c['timestamp']) else datetime.strptime(c['timestamp'], "%Y-%m-%d %H:%M:%S.%f%z"))
        
        # finding defects
        if c['selectedconetype'] == c['detectedconetype']:
            total_conetip_Nondefect += 1
        else:
            total_conetip_Defect += 1    
       
    print("conetip_date_dict : ",conetip_date_dict)
    print("uv_date_dict:",uv_date_dict)
    
    
    print('total_uv_Nondefect : ' ,total_uv_Nondefect,    'total_uv_Defect : ',total_uv_Defect,   'total_conetip_Nondefect : ', total_conetip_Nondefect, 'total_conetip_Defect : ',total_conetip_Defect)
    print("__________________________________________________")
    
     
    print("conetip Count of ",i," : \t",len(fbData[i]['conetip']))
    print("conetip last run on ",i," : \t",fbData[i]['conetip'][-1]['timestamp'])
    print("UV Count of ",i," : \t\t",len(fbData[i]['uv']))
    print("UV last run on ",i," : \t",(fbData[i]['uv'][-1]['timestamp']))
    print("Today Cone Tip Defect Count :")
    print("Today UV Defect Count :")
    
    print("__________________________________________________")

print("Working")