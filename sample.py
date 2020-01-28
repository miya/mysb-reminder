import MySBdt

telnum = 'your_phone_number'
password = 'your_mysoftbank_password'
line_access_token = 'your_line_notify_token'
current_month_data = 5.0

# インスタンスの作成
api = MySBdt.API(telnum=telnum, password=password, line_access_token=line_access_token, current_month_data=current_month_data)

# データ（使用量、残量、繰越残量、追加量、追加使用量、追加繰越量、追加繰越使用量）の取得
api.get_data()

# lineに通知する
api.send_message()
