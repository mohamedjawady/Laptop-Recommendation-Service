import requests
from bs4 import BeautifulSoup
import pandas as pd

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
headers = {'User-Agent': user_agent}

def get_ebay_image(query):
    search = "+".join(query.split())
    page = requests.get(f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={search}&_sacat=0")
    
    soup = BeautifulSoup(page.text, 'html.parser')

    try:
        el = soup.find_all("img")[12]["src"]
        print(el)
        return el
    except:
        return "#"



df = pd.read_csv("models/processed_dataset.csv", index_col=0)
for i, row in df.iterrows():
    url = get_ebay_image(row["Laptop"])
    print(f"{i}/{len(df)} - {url}")
    df.at[i, 'url'] = url
    df.to_csv('models/processed_dataset_urls.csv')