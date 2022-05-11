
import requests

import json
import sqlite3
url='https://animechan.vercel.app/api/available/anime'
req=requests.get(url)

print(f'API ლინკი {req.url}')
print(f'სტატუს კოდი {req.status_code}')
print(f'API შიგთვსი{req.content}')
print(f'REQUEST {req.request}')


req_json=req.text
res=json.loads(req_json)
stru=json.dumps(res,indent=4)
jres=(req.json())

with open('animes.json', 'w') as f:
    json.dump(stru, f)

"""ეს არის ცხრილი რომელიც გვიჩვენებს დღესდღეობით ხემისაწვდომ ანიმეებს."""
conn = sqlite3.connect('allanime.db')
c = conn.cursor()
c.execute("CREATE TABLE last_anime (data json)")

for list_anime in jres:


    c.execute("insert into last_anime values (?)",
      [json.dumps(list_anime,indent=4)])
    conn.commit()
conn.close()


