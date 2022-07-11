import requests#pip install requests

character=input('Please enter the character for see the data: ')
url="https://rickandmortyapi.com/api/character/?name={}".format(character)
response=requests.get(url)
data=response.json()

info_character=data["results"]#Print all info

name=data["results"][0]["name"]
status=data["results"][0]["status"]
species=data["results"][0]["species"]
gender=data["results"][0]["gender"]
origen=data["results"][0]["origin"]["name"]

print('The name is: {}\nThe status: {}\nThe specie is: {}\nThe gender is: {}\nThe origen is: {}'.format(name,status,species,gender,origen))