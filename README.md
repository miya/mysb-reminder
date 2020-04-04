# MySB-datatraffic
[MySoftbank](https://www.softbank.jp/mysoftbank/)をスクレイピングして通信データ残量をLINE通知するやつ

## Install 
```python
$ pip3 install MySB-datatraffic
```

## Initialize
```python
import MySBdt

telnum = "your_phone_number"
password = "your_MySoftbank_password"
line_access_token = "your_line_notify_access_token"

api = MySBdt.API(telnum=telnum, password=password, line_access_token=line_access_token)
```

## Feature
```python
# データ（使用量、残量、繰越残量、追加量、追加使用量、追加繰越量、追加繰越使用量）の取得
data = api.get_data()
print(data)

# out
{
    'used_data': 6.34,
    'remain_data': 0.02, 
    'step_remain_data': 0.0,
    'additional_data': 1.0,
    'additional_used_data': 0.98,
    'given_data': 0.36, 
    'given_used_data': 0.36
}
```
```python
# lineに通知
status = api.send_message()
print(status)

# out
200
```

## Demo
[サンプルコード](https://github.com/miya/MySB_dataTraffic/blob/master/sample.py)を実行した！

![](https://user-images.githubusercontent.com/34241526/78420090-e3564b00-7686-11ea-92e6-77bbfdfe56f9.png)

