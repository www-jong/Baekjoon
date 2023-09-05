from flask import Flask, render_template, request, redirect
from threading import Thread
import random
import requests

app = Flask(__name__, template_folder='templates', static_folder='static')

.com/lol/summoner/v4/summoners/by-name/" + '구형깔깔이' + '?api_key=' + RIOT_API
r = requests.get(get_data)


@app.route('/')
def home():
  return render_template('main.html')


@app.route("/user", methods=['GET', 'POST'])
def user_search():
  if request.method == "POST":
    username = request.form['username']
    get_data = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + username + '?api_key=' + RIOT_API
    r = requests.get(get_data)
    r = r.json()
    if 'status' in r:
      data={'name':'없는소환사입니다.'}
      return render_template('show_user_data.html', data=data)
    
    data = {}
    if 'summonerLevel' in r:
      data['level'] = r['summonerLevel']
    if 'name' in r:
      data['name'] = request.form['username']
    tier_url = "https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/"+ r['id'] +'?api_key=' + RIOT_API
    r2  = requests.get(tier_url)
    r2=r2.json()
    data['tear']=r2['tear']+' '+str(r2['rank'])
    return render_template('show_user_data.html', data=data)
  else:
    #data=request.args
    return render_template('show_result.html', data=request.args)


if __name__ == "__main__":  # Makes sure this is the main process
  app.run(host='0.0.0.0', port=random.randint(2000, 9000))
