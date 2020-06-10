#現代俳句データベース(http://www.haiku-data.jp/index.php)のスクレイピングプログラム
#https://teratail.com/questions/152188 の内容をコピペしたものである。

import csv
import time
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
}


def get_data(url):
    r = requests.get(url, headers=headers)
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.content, 'html.parser')
    try:
        title = soup.select_one('div.title').get_text(strip=True)
    except:
        return False
    else:
        if len(title) == 0:
            return False
        info = [[
            tds.get_text(strip=True).replace('\u3000', '')
            for tds in trs.find_all('td')
        ] for trs in soup.find(
            'table',
            attrs={
                'align': 'center',
                'bgcolor': '#E7DDD4',
                'border': '0',
                'cellpadding': '6',
                'cellspacing': '1',
                'width': '85%'
            }).find_all('tr')]
        result = dict(info)
        result['俳句'] = title
        return result



data = []
MAX_ID = 41188  # 登録されているIDの最大値
Start_ID = 7958 #スクレイピングするページIDのスタート地点

#with open('outputHAIKU.csv', 'w', newline='', encoding='utf-8') as f:  #２つめの引数がwだと上書き、aだと追記
with open('outputHAIKU.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                '俳句', '作者', '季語', '季節', '出典',  '前書', '評言','評者', '備考'
            ])
        writer.writeheader()

        for i in range(Start_ID, MAX_ID): #

            url = 'http://www.haiku-data.jp/work_detail.php?cd={id}'.format(
                id=i)
            print('fetching data... ' + url, end=' ')

            data = get_data(url)

            if data:
                print('result: SUCCESS')
                writer.writerow(data)
            else:
                print('result: MISSING')

            time.sleep(1)  # アクセス間隔


