# MySB_dataTraffic
[MySoftBank](https://www.softbank.jp/mysoftbank/)をスクレイピングしてデータ残量をLINEに通知するやつ
## Install
pipでインストールします
```
$ pip3 install MySB-datatraffic
```
## How to use
ライブラリのインポート
```Python
import MySBdt
```
LINE通知には[LINE Notify](https://notify-bot.line.me/ja/)を使用するのでアクセストークンを取得しておく必要があります。telnum、password、line_access_tokenを自分のものに置き変えます。
```Python
telnum = "電話番号"
password = "MySoftbankのパスワード"
line_access_token = "LineNotifyのアクセストークン"
```
インスタンスを作成  
```Python
api = MySBdt.API(telnum=telnum, password=password, line_access_token=line_access_token)
```
データ（使用量、残量、繰越残量、追加量、追加使用量、追加繰越量、追加繰越使用量）の取得ができます。
```Python
data = api.get_data()
print(data)

# 実行結果
# {'used_data': 6.34, 'remain_data': 0.02, 'step_remain_data': 0.0, 'additional_data': 1.0, 'additional_used_data': 0.98, 'given_data': 0.36, 'given_used_data': 0.36}
```
LINEに通知します。
```Python
status = api.send_message()
print(status)

# 実行結果
# 200
```
実行すると以下のような情報がLINEに通知されます。戻り値はrequestsのHTTPステータスコードが返ります。

![](https://user-images.githubusercontent.com/34241526/66271995-2170de80-e89f-11e9-9a66-a32cfef9747f.jpg)

## Author
@qxi_(https://twitter.com/qxi_)
