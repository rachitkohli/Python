import requests

def getResponse():
    URL = "http://localhost:55847/api/teachers"
    location = "delhi technological university"
    # Params = {'address':location} 
    r = requests.get(url=URL) 
    data = r.json()
    print(data[0]['teacherName'])

getResponse()