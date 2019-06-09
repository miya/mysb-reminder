from dataTraffic import dataTraffic

telnum = 'your_phone_number'
password = 'your_mysoftbank_password'
line_access_token = 'your_line_notify_token'

dt = dataTraffic(telnum=telnum, password=password, line_access_token=line_access_token)
dt.send_data()