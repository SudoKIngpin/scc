from flask import render_template, Flask , request
from ytdl import yt

app=Flask(__name__)

@app.route("/",methods=["GET"])
def home():
    return render_template("form.html")

@app.route("/download",methods=["POST"])
def download():
    url=request.form['url']

    ytdict=yt(url) # Dictionary / JSON data containing URL Object 
    return render_template("download.html",yt=ytdict)

app.run(host='0.0.0.0',debug=True,port=80)