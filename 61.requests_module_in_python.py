#the requests module in is an http library that enables developer to send and makes it possible to interact with apis and web service
# import requests
# responce=requests("https://www.google.com")
# print(responce.text)
# #post request :-
import requests
url="https://WWW.google.com"
data={
    "title":"bhuyan",
    "body":"bhai",
    "user id":12}
headers={'content-type':'application/json;charset=0tf-8'}
responce=requests.post(url,headers=headers,json=data)