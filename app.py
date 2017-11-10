from flask import Flask, session, render_template, request, redirect, flash,  url_for
import urllib2
import json
app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def root():
    u = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=RvEhHA59fuin9WI0oK3RxK7Te31EcneKjEvC0VAp")

    dict = json.loads(u.read())
    url = dict['url']
    exp = dict['explanation']
    return render_template("index.html", link=url, desc=exp)
    


if __name__ == "__main__":
    app.debug = True
    app.run()
