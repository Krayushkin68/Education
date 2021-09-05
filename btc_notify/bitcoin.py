import requests
import win10toast
import os
from time import sleep
from datetime import datetime
from bs4 import BeautifulSoup as BS


def btc_checker():
    req = requests.get('https://www.google.com/search?q=%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD+%D0%BA+%D0%B4%D0%BE%D0%B'
                       'B%D0%BB%D0%B0%D1%80%D1%83&oq=%D0%B1%D0%B8%D1%82%D0%BA%D0%BE&aqs=chrome.0.69i59l2j69i57j0i20i131i263'
                       'i433j0i131i433j69i61l3.1007j1j7&sourceid=chrome&ie=UTF-8')
    html = BS(req.content, 'html.parser')
    tag = html.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'})
    btc = ''.join(tag.text.split()[:2])
    btc = btc.replace(',', '.')
    return float(btc)


def log(btc):
    time = datetime.now().time().strftime('%H:%M:%S')
    with open('btc_log.txt', 'at') as f:
        f.write(f"{time}:   BTC/USD: {btc}\n")
    print(f"{time}:   BTC/USD: {btc}")


slp_time = 20*60
toaster = win10toast.ToastNotifier()
prev_val = btc_checker()
while True:
    ico = os.path.join(os.getcwd(), 'btc.ico')
    cur_val = btc_checker()
    if cur_val > prev_val and cur_val > 40000:
        chn = cur_val-prev_val
        toaster.show_toast(f"Биточек подрос на {chn:.2f}", f"BTC/USD:  {cur_val}", icon_path=ico)
    elif cur_val < prev_val and cur_val > 40000:
        chn = prev_val-cur_val
        toaster.show_toast(f"Биточек упал на {chn:.2f}", f"BTC/USD:  {cur_val}", icon_path=ico)
    else:
        if cur_val > 40000:
            toaster.show_toast(f"Биточек все тот-же", f"BTC/USD:  {cur_val}", icon_path=ico)
    log(cur_val)
    prev_val = cur_val
    sleep(slp_time)
