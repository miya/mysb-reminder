import re
import requests
from bs4 import BeautifulSoup

def login():
    session = requests.Session()
    req = session.get('https://my.softbank.jp/msb/d/webLink/doSend/MSB020063')
    soup = BeautifulSoup(req.text, 'html.parser')
    ticket = soup.find('input', type='hidden').get('value')
    payload = {
        'telnum': telnum,
        'password': password,
        'ticket': ticket
    }
    session.post('https://id.my.softbank.jp/sbid_auth/type1/2.0/login.php', data=payload)
    return session

def get_data(session):
    req = session.get('https://my.softbank.jp/msb/d/webLink/doSend/MRERE0000')
    soup = BeautifulSoup(req.text, 'html.parser')
    auth_token = soup.find_all('input')
    payload = {
        'mfiv': auth_token[0].get('value'),
        'mfsb': auth_token[1].get('value'),
    }
    res = session.post('https://re11.my.softbank.jp/resfe/top/', data=payload)
    m = re.findall('<span>(.+?)</span>GB', res.text)
    used = float(m[0])
    total = float(m[1])
    remain = float(m[2])
    rate = round(remain / total * 100, 1)
    return used, total, remain, rate

def line(message):
    line_notify_token = access_token
    line_notify_api = 'https://notify-api.line.me/api/notify'
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    line_notify = requests.post(line_notify_api, data=payload, headers=headers)

if __name__ == '__main__':
    telnum = 'your_phone_number'
    password = 'your_mysoftbank_password'
    access_token = 'your_line_notify_token'

    data = get_data(session=login())
    text =  '\n{}GB / {}GB ({}%)'.format(data[2], data[1], data[3])
    line(message=text)
