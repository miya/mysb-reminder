from MySBdT import dataTraffic

telnum = 'your_phone_number'
password = 'your_mysoftbank_password'
line_access_token = 'your_line_notify_token'

dt = dataTraffic(telnum=telnum, password=password, line_access_token=line_access_token)

# データ（データ残量、総量、使用量、割合）の取得
dt.get()

# LINEに通知する
dt.line() 