import requests
import json
import sys
def qiwi():
    api_access_token = "126c962c6eaf147aae085d416ae44366"
    my_login ="+79828379093"

    struct = {}

    s = requests.Session()
    s.headers['authorization'] = 'Bearer ' + api_access_token
    parameters = {'rows': '50' , 'operation' : 'IN'}
    h = s.get('https://edge.qiwi.com/payment-history/v1/persons/'+my_login+'/payments', params = parameters)
    p = json.loads(h.text)

    new_line = str(p["data"])
    line = new_line.replace("[", " ")
    line_1 = line.replace("]"," ")
    end_line = line_1.replace("'", "")
    end_line_1 = end_line.replace(":",",")
    end_line_2 = end_line_1.split(',')
    summa = []
    for i in range(len(end_line_2)):
        if end_line_2[i] ==' sum':
            summa.append(float(end_line_2[i+2]))
    return summa
