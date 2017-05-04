import os
import requests
import mylib
keyPath = os.path.join(os.getcwd(), 'src', 'key.properties')
key = mylib.getKey(keyPath)
_url = 'http://openAPI.seoul.go.kr:8088'
_key = str(key['dataseoul '])
_type = 'xml'
_service = 'CardSubwayStatisticsService'
_start_index = 1
_end_index = 5
_use_mon = 201500
for mon in range(12):
    _use_mon += 1
    _api = _url + "/" + _key + "/" + _type + "/" + _service + "/" + str(_start_index) + "/" + str(_end_index) + "/" + str(_use_mon)
    response = requests.get(_api).text
    print response