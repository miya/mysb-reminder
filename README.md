# MySB_dataTraffic
[MySoftBank](https://www.softbank.jp/mysoftbank/)をスクレイピングしてデータ残量をLINEに通知するやつ
## Install
```
$ pip3 install MySB-datatraffic
```
## How to use
LINE通知には[LINE Notify](https://notify-bot.line.me/ja/)を使用するのでアクセストークンを取得しておく。

インポート
```Python
from MySBdT import dataTraffic
```
telnum、password、line_access_tokenを自分のものに置き換える。
```Python
telnum = 'your_phone_number'
password = 'your_mysoftbank_password'
line_access_token = 'your_line_access_token'
```
インスタンスを作成  
```Python
dt = dataTraffic(telnum=telnum, password=password, line_access_token=line_access_token)
```
データ（総量、残量、使用量、割合、前月繰越分）の取得
```Python
data = dt.get()
print(data)

# 実行結果
# ('5.00', '4.04', '0.96', '80.8', '0.00')
```
LINEに通知する
```Python
dt.line()
```
実行すると以下のような情報がLINEに通知される。戻り値はrequestsのHTTPステータスコードが返る。

![](https://user-images.githubusercontent.com/34241526/66271995-2170de80-e89f-11e9-9a66-a32cfef9747f.jpg)
