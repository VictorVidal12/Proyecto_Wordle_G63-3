import requests
import ast

"""
Con este código se hace el llamado a la API y se obtienen las palabras de allí 

"""
api_url = 'https://api.api-ninjas.com/v1/randomword'
n = 0
f = open("palabras", "w")
while n < 10000:
    response = requests.get(api_url, headers={'X-Api-Key': '74w5GflDZj4lbxnx3l7Lrg==129rRPt1vTEb5hdg'})
    plb = ast.literal_eval(response.text)
    if len(plb['word']) == 5:
        palabras_wordle: str = plb['word']
        f.write(palabras_wordle + '\n')
    n += 1

f.close()

