# MySB_dataTraffic
データ残量をLINEに通知するスクリプト(ソフトバンクユーザー限定)
## Install
```
$ pip3 install MySB-datatraffic
```
## How to use
インポート
```Python
from MySBdT import dataTraffic
```
telnum、password、line_access_tokenを自分のものに置き換える  
```Python
telnum = 'your_phone_number'
password = 'your_mysoftbank_password'
line_access_token = 'your_line_access_token'
```
インスタンスを作成  
```Python
dt = dataTraffic(telnum=telnum, password=password, access_token=access_token)
```
データの取得  
```Python
data = dt.get_data()
```
LINE
```Python
dt.send_data()
```
