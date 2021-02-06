from flask import Flask
from flask import jsonify
from requests import get
from bs4 import BeautifulSoup as bs
from tabulate import tabulate

a = Flask(__name__)

@a.route("/nba_stands")
def nba_stands():
	r = get("https://www.basketball-reference.com/")
	r = bs(r.text,'html.parser')
	tw = r.find("table",{"id":"confs_standings_W"})
	te = r.find("table",{"id":"confs_standings_E"})
	return str(tw) + "<br>" + str(te)
	
@a.route("/euroleage_stands")
def euro():
	r = get("https://www.euroleague.net/main/standings")
	r = bs(r.text,"html.parser")
	r = r.find("table")
	return str(r)
	

	
if "__main__" == __name__:
	a.run()