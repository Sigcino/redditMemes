from flask import Flask, render_template
import requests
import json
import logging

logging.basicConfig(filename='meme.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', encoding='utf-8', level=logging.DEBUG)


app = Flask(__name__)

def get_meme():
    url = 'https://meme-api.com/gimme/3'
    response = json.loads(requests.request("GET", url).text)
    memes = response["memes"]
    # Extract the meme data for each meme in the response
    # and store them in a list of dictionaries
    meme_list = []
    for meme in memes:
        meme_large = meme["preview"][-2]
        subreddit = meme["subreddit"]
        title = meme["title"]
        postLink = meme["postLink"]
        meme_dict = {"meme_pic": meme_large, "subreddit": subreddit, "title": title, "postLink": postLink}
        meme_list.append(meme_dict)
    return meme_list

@app.route("/")
def index():
    memes = get_meme()
    return render_template("home.html", memes=memes)


app.run(host="0.0.0.0", port=8089)
