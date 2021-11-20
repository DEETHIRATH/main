
import requests
from bs4 import BeautifulSoup
from tkinter import messagebox

Address = "https://kabutan.jp/stock/?code="
url_list = ["9318", "2038"]
response = ""

#会社名と株価を取得
for url in url_list:
    res = requests.get(Address + url)
    soup = BeautifulSoup(res.text, "html.parser")
    elems_corp_name = soup.select('#kobetsu')
    elems_price = soup.select('#stockinfo_i1 > div.si_i1_2 > span.kabuka')
    corp_name = elems_corp_name[0].contents[0].split()[0]
    price = elems_price[0].contents[0]

    result = corp_name + " : " + price + "\n"
    response += result

messagebox.showinfo('メッセージ', response)



