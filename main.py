import requests
import json
import time

Author : list[dict] = [
    {"work" : True,
     "name" : 'junyue-server MToxODU2NjpkMzgzNTE5ZWMwOWQ3ZDdlNzZhYWE4OTAyNTkwYWE3Mw==',
     "resourceId" : 760,
     "deviceMac" : "70B3D5058005005E",
     "id" : 0}
]

headers = {
    'Authorization': "",
}

json_data = {"use":{
                    'resourceId': 0,
                    'startTime': 0,
                    'endTime': 0,
                    },
             "device":{
                    "deviceMac" : ""
                    }
}

USE = "use"
FINISH = lambda id : "finish/" + str(id)
CURRENT = "current"
DEVICE = "devices/socket/on"
WEB_URL = lambda fun : "http://202.203.134.159:10009/v1/reservation/" + fun
ENDTIME = 0

def get_current():
    for auth in Author:
        headers["Authorization"] = auth["name"] 
        response = requests.get(WEB_URL(CURRENT), headers=headers)
        if response.content.decode() != '':
            auth["id"] = json.loads(response.content.decode())["id"]
            fin_seat() 
            
def occ_seat():
    global ENDTIME
    for auth in Author:
        headers["Authorization"] = auth["name"]
        json_data["use"]["resourceId"] = auth["resourceId"]
        json_data["device"]["deviceMac"] = auth["deviceMac"]
        response = requests.post(WEB_URL(USE), headers=headers, json=json_data["use"])
        content = json.loads(response.content.decode())
        requests.post(WEB_URL(DEVICE),headers=headers, json=json_data["device"])
        auth["id"] = content["id"]
        ENDTIME = content["endTime"]

def fin_seat():
    global ENDTIME
    for auth in Author:
        headers["Authorization"] = auth["name"]
        requests.post(WEB_URL(FINISH(auth["id"])), headers=headers)
        ENDTIME = 0

if "__main__" == __name__:
    get_current()
    while True:
        if ENDTIME == 0 and 22 >= time.localtime().tm_hour >= 8:
            occ_seat()
        elif ENDTIME <= time.time()*1000-1000:
            fin_seat()
        elif time.localtime().tm_hour > 22:
            fin_seat()
