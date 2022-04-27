import requests


url='https://jsonplaceholder.typicode.com/'


def getApi(param):
    url='https://jsonplaceholder.typicode.com/'
    reponse=requests.get(url+param)
    print(reponse.content)
    


getApi('users')
