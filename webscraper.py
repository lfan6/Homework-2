# Lucas Fan
# FE-595 Assignment 2
# Web Scraper

import random

from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)


@app.route('/hw3', methods=['GET'])
def index():
    url = "http://3.95.249.159:8000/random_company"
    co_name = []
    co_purpose = []
    for i in range(50):
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        items = soup.find('ol').findChildren()
        co_name.append(items[0].text[6:])
        co_purpose.append(items[3].text[9:])
    return render_template('name_purpose.html', name=co_name, purpose=co_purpose)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)





