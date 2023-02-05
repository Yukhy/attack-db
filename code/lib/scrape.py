import requests
import pandas as pd

class Scrape:
    def __init__(self, url: str):
        self.content = requests.get(url).content
    
    # 指定したURL先のコンテンツのTableをDFに変換して返す
    def get_table_by_df(self):
        return pd.read_html(self.content)[0]