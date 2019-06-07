import os
from dataTraffic import dataTraffic

telnum = os.environ.get('telnum')
password = os.environ.get('password')
line_access_token = os.environ.get('line_access_token')

dt = dataTraffic(telnum=telnum, password=password, line_access_token=line_access_token)
dt.send_data()