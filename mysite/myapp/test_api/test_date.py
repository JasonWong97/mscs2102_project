import datetime
import time

millis = int(round(time.time() * 1000))
print(millis)
print(millis-90*24*60*60*1000)
timeStamp=millis-90*24*60*60*1000
timeStamp=timeStamp/1000
import time

timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
print(otherStyleTime)
#
# import requests
# url = 'http://api.bitdataset.com/v1/symbols'
# headers = {'apikey' : 'a4c7f4f4-6506-451a-b35c-631e7a2949b9'}
# response = requests.get(url, headers=headers)
# print(response.text)



