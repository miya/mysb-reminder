from dataTraffic import dataTraffic

telnum = 'your_phone_number'
password = 'your_mysoftbank_password'
access_token = 'your_line_notify_token'

dt = dataTraffic(telnum=telnum, password=password, access_token=access_token)
data = dt.get_data()
text = '\n{}GB / {}GB ({}%)'.format(data[0], data[1], data[3])
dt.line(message=text)
dt.add_database(remain=data[0], total=data[1], used=data[2], rate=data[3])
