import requests
import  json
URL="http://127.0.0.1:8000/aicreate/"
#create python data
data={
    'id' : 7,
}
#convert json data
json_data=json.dumps(data)

r=requests.delete(url=URL,data=json_data)
data=r.json()
print(data)