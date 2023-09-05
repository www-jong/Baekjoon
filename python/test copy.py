
from threading import Thread
import random
import requests



username = '구형깔깔이'
get_data = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + username + '?api_key=' + RIOT_API
r = requests.get(get_data)
r = r.json()
if 'status' in r:
    data={'name':'없는소환사입니다.'}

data = {}
if 'summonerLevel' in r:
    data['level'] = r['summonerLevel']
if 'name' in r:
    data['name'] = '구형깔깔이'
print(r)
tier_url = "https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/"+ r['id'] +'?api_key=' + RIOT_API
r2  = requests.get(tier_url)
r2=r2.json()[0]
print('___')
print(r2)
print(r2['tier'],r2['rank'])
print(str((r2['wins']/(r2['losses']+r2['wins']))*100)+"%")
