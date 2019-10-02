import re
import sqlite3
import requests
import datetime
from bs4 import BeautifulSoup

class dataTraffic:

    def __init__(self, telnum, password, line_access_token):
        self.telnum = telnum
        self.password = password
        self.line_access_token = line_access_token

    def login(self):
        session = requests.Session()
        req = session.get('https://my.softbank.jp/msb/d/webLink/doSend/MSB020063')
        soup = BeautifulSoup(req.text, 'lxml')
        ticket = soup.find('input', type='hidden').get('value')
        payload = {
            'telnum': self.telnum,
            'password': self.password,
            'ticket': ticket
        }
        session.post('https://id.my.softbank.jp/sbid_auth/type1/2.0/login.php', data=payload)
        return session

    def get(self):
        session = self.login()
        req = session.get('https://my.softbank.jp/msb/d/webLink/doSend/MRERE0000')
        soup = BeautifulSoup(req.text, 'lxml')
        auth_token = soup.find_all('input')
        payload = {
            'mfiv': auth_token[0].get('value'),
            'mfsb': auth_token[1].get('value'),
        }
        req2 = session.post('https://re11.my.softbank.jp/resfe/top/', data=payload)
        soup2 = BeautifulSoup(req2.text, 'lxml')
        num = [float(re.findall('\d+[.]+\d\d', str(i))[0]) for i in soup2.find_all(class_='p-left-10')]
        total = num[1]
        remain = num[1] - num[0]
        used = num[0]
        rate = round(remain / total * 100, 1)
        return total, remain, used, rate

    def line(self):
        data = self.get()
        text = '{}GB / {}GB ({}%)'.format(data[1], data[0], data[3])
        print(text)
        line_notify_token = self.line_access_token
        line_notify_api = 'https://notify-api.line.me/api/notify'
        payload = {'message': text}
        headers = {'Authorization': 'Bearer ' + line_notify_token}
        line_notify = requests.post(line_notify_api, data=payload, headers=headers)