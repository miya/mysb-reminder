# dataTraffic
データ残量をLINEに通知するスクリプト(ソフトバンクユーザー限定)
## Setup
```git clone https://github.com/0x0u/dataTraffic```  

```cd dataTraffic```  

```pip3 install -r requiremenets.txt```  

sample.pyを開きtelnum（電話番号）、password、access_token（line notifyのアクセストークン）を自分のものに書き換える

```python3 sample.py```  
## qiita
qiita: https://qiita.com/0x0/items/b7c951988b5ea6c866d3

## How to use
外部ファイルから開く場合はインポートする　。
```Python
from dataTraffic import dataTraffic
```
telnum、password、access_tokenを自分のものに置き換える  
```Python
telnum = 'your_phone_number'
password = 'your_mysoftbank_password'
access_token = 'your_line_notify_token'
```
インスタンスを作成  
```Python
dt = dataTraffic(telnum=telnum, password=password, access_token=access_token)
```
データの取得  
```Python
data = dt.get_data()
```
取得したデータを加工してlineに通知、データベースに保存  
```Python
text = '\n{}GB / {}GB ({}%)'.format(data[0], data[1], data[3])
dt.line(message=text)
dt.add_database(remain=data[0], total=data[1], used=data[2], rate=data[3])
```
