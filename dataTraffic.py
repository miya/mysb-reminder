import requests,os,re
from bs4 import BeautifulSoup as bs


def login():
    s = requests.Session()
    r = s.get('https://my.softbank.jp/msb/d/webLink/doSend/MSB020063')
    soup = bs(r.text,'html.parser')
    auth_token = soup.find('input',type='hidden').get('value')
    payload = {
        'telnum': telnum,
        'password': password,
        'ticket':auth_token
    }
    s.post('https://id.my.softbank.jp/sbid_auth/type1/2.0/login.php', data=payload)
    return s


def get_data(s):
    r = s.get('https://my.softbank.jp/msb/d/webLink/doSend/MRERE0000')
    soup = bs(r.text,'html.parser')
    auth_token = soup.find_all('input')
    payload = {
        'mfiv': auth_token[0].get('value'),
        'mfsb': auth_token[1].get('value'),
    }
    req = s.post('https://re11.my.softbank.jp/resfe/top/', data=payload)
    data = bs(req.text,'html.parser')
    match = re.findall('<span>(.+)</span>GB',str(data))
    return match[0],match[1]


def line(message):
    line_notify_token = access_token
    line_notify_api = 'https://notify-api.line.me/api/notify'
    payload = {'message': '\n'+message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    line_notify = requests.post(line_notify_api, data=payload, headers=headers)


if __name__ == '__main__':
    telnum = 'telephone_number'
    password = 'mysoftbank_password'
    access_token = 'line_notify_access'

    data = get_data(login())
    text =  '{}GB / {}GB ({}%)'.format(data[0],data[1],int(float(data[0])/float(data[1])*100))
    line(text)
