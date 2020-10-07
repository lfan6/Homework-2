# Lucas Fan
# FE-595 Assignment 2
# Web Scraper

from bs4 import BeautifulSoup
import requests
import pandas as pd


def get_company():
    url = "http://3.95.249.159:8000/random_company"
    try:
        test = requests.get(url)
        test.raise_for_status()
    except requests.HTTPError as exception:
        print(exception)
        return

    co_name = []
    co_purpose = []
    for i in range(50):
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        for li in soup.find('ol').find_all('li'):
            if 'Name:' in str(li):
                co_name.append(li.text[6:])
            if 'Purpose:' in str(li):
                co_purpose.append(li.text[9:])
            continue
    data = pd.DataFrame({'Company Name': co_name, 'Company Purpose': co_purpose})
    data.to_csv("output.csv", index=False)


if __name__ == "__main__":
    get_company()





