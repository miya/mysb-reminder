# MySB_dataTraffic
[MySoftBank](https://www.softbank.jp/mysoftbank/)をスクレイピングして端末のデータ残量をLINEに通知するやつ
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
データ（総量、残量、使用料、割合）の取得
```Python
data = dt.get()
```
LINEに通知する
```Python
dt.line()
```
こんな感じ。 一日一回スケジューラーで実行したらデータマネジメントしやすそう。

![](https://user-images.githubusercontent.com/34241526/59161618-1fc92100-8b20-11e9-9394-b6cfb86a6914.png)
