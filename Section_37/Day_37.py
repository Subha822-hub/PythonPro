import requests
from datetime import date


X_USER_TOKEN = "abcdefghijklmnop"
USER_NAME="subha1"
GRAPH_ID="graphy1"

URL = "https://pixe.la/v1/users"

post_endpoint = {
    "token":X_USER_TOKEN,
    "username":USER_NAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
} 

# response = requests.post(url=URL,json=post_endpoint)
# print(response.text)

graph_url = f"{URL}/{USER_NAME}/graphs"

graph_post_endpoint = {
    "id":GRAPH_ID,
    "name":"walking",
    "unit":"Km",
    "type":"int",
    "color":"ajisai",

} 

headers = {
    "X-USER-TOKEN":X_USER_TOKEN
}

# response = requests.post(url=graph_url,json=graph_post_endpoint,headers=headers)
# print(response.text)

put_graph_url = f"{URL}/{USER_NAME}/graphs/{GRAPH_ID}"

today = date.today().strftime('%Y%m%d')

put_graph_post_endpoint = {
    "date":"20231030",
    "quantity":"7",
    
} 

put_headers = {
    "X-USER-TOKEN":X_USER_TOKEN
}

# response = requests.post(url=put_graph_url,json=put_graph_post_endpoint,headers=put_headers)
# print(response.text)

delete_graph_url = f"{URL}/{USER_NAME}/graphs/{GRAPH_ID}/20231030"
 

delete_headers = {
    "X-USER-TOKEN":X_USER_TOKEN
}

# response = requests.delete(url=delete_graph_url,headers=delete_headers)
# print(response.text)

# Ouput

# Sample_URL :: https://pixe.la/v1/users/subha1/graphs/graphy1.html

# UsefulSite

# * https://pixe.la *



