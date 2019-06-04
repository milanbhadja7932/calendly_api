import requests
headers={"Authorization": "token:NKNECNBKNOVDSF3RTAJJB3CEH6HK3KOL"}
data={'title':'Python Requests','body':'req are awesome'}

#get data
response=requests.get("https://calendly.com/milanbhadja7932/",headers=headers)
tor=(response.content)
print("status code",response.status_code)

#post data
response = requests.post('https://calendly.com/milanbhadja7932/',json=data,headers=headers)        # To execute get request 
print("status code",response.status_code)

#patch/update data
response = requests.patch('https://calendly.com/milanbhadja7932/',json=data,headers=headers)
print("status code",response.status_code)

#delete data
response = requests.delete('https://calendly.com/',headers=headers)
print("status code",response.status_code)

