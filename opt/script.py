import requests
from bs4 import BeautifulSoup

# 取得するサイトのURL
url = 'https://qiita.com/'
# requests.get(url)で指定されたwebの情報を色する
res = requests.get(url)

# res.textで内容を確認することができる
# print(res.text)

# 情報を解析する
soup = BeautifulSoup(res.text, "html.parser")

# クラス名item_nameがつく要素を取ってくる(タイトル)
title = soup.find_all(class_="css-1t4fpk1")
for titles in title:
  print(titles.text)
