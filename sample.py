import MySBdt

telnum = 'your_phone_number'
password = 'your_mysoftbank_password'
line_access_token = 'your_line_notify_token'

# インスタンスの作成
api = MySBdt.API(telnum=telnum, password=password, line_access_token=line_access_token, current_month_data=5.0)

# データ（総量、残量、使用量、割合、前月繰越分）の取得
api.get_data()

# lineに通知する
api.send_message()
