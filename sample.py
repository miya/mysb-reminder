from MySBdT import dataTraffic

telnum = 'your_phone_number'
password = 'your_mysoftbank_password'
line_access_token = 'your_line_notify_token'

dt = dataTraffic(telnum=telnum, password=password, line_access_token=line_access_token)

# データ（総量、残量、使用料、割合）の取得
dt.get()

# LINEに通知する
dt.line()