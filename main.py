import requests
import json
import time

# lst : list[dict]:

Author : list[dict] = [
    {"work" : True,
     "name" : 'junyue-server MToxODU2NjpkMzgzNTE5ZWMwOWQ3ZDdlNzZhYWE4OTAyNTkwYWE3Mw==',
     "resourceId" : 760,
     "deviceMac" : "70B3D5058005005E",
     "id" : 0}
]

headers = {
    'Host': '202.203.134.159:10009',
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
FINISH = lambda id : "finish/" + id
DEVICE = "device/socket/on"
WEB_URL = lambda fun : "http://202.203.134.159:10009/v1/reservation/" + fun

ENDTIME = 0

for auth in Author:
    headers["Authorization"] = auth["name"]
    json_data["use"]["resourceId"] = auth["resourceId"]
    json_data["device"]["deviceMac"] = auth["deviceMac"]
    response = requests.post(WEB_URL(USE), headers=headers, json=json_data["use"])
    content = json.loads(response.content.decode())
    auth["id"] = content["id"]
    ENDTIME = content["endTime"]

while True:
    pass

# response = requests.post('http://202.203.134.159:10009/v1/reservation/finish/52582', headers=headers)
