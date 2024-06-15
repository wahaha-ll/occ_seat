import requests

headers = {
    'Authorization': 'junyue-server MToxODU2NjpmY2VmM2MzMDM4ZmVkOGM3NjlkOTczMTE5NTM5MTdkMQ==',
}

json_data = {
    'deviceMac': '70B3D5058005005E',
}

response = requests.post('http://202.203.134.159:10009/v1/reservation/devices/socket/off', headers=headers, json=json_data)
