from flask import Flask, session, render_template, request, redirect, flash,  url_for
import urllib2
import json
import requests

HEADERS = {"X-API-Key":'72504fb40d484be59b89d903b9d4ed08'}
app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def root():
    u = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=RvEhHA59fuin9WI0oK3RxK7Te31EcneKjEvC0VAp")

    dict = json.loads(u.read())
    url = dict['url']
    exp = dict['explanation']
    return render_template("index.html", link=url, desc=exp)

@app.route('/armory', methods = ['GET','POST'])
def armory():
    r=requests.get("http://www.bungie.net/Platform/Destiny2/Armory/Search/DestinyInventoryItemDefinition/hive/", headers=HEADERS);
    dict=r.json()

    return render_template("armory.html", info=dict)

if __name__ == "__main__":
    app.debug = True
    app.run()
