import requests
import json
URL="http://127.0.0.1:8000/aicreate/"
#create python data
data={
    'teacher_name':'Aksh',
    'course_name':'ML2',
    'course_duration':8,
    'seat':30,
}
#convert json data
json_data=json.dumps(data)

r=requests.post(url=URL,data=json_data)
data=r.json()
print(data)