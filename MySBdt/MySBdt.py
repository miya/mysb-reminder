import re
import ast
import requests
from bs4 import BeautifulSoup

class API:

    def __init__(self, telnum=None, password=None, line_access_token=None):
        self.telnum = telnum
        self.password = password
        self.line_access_token = line_access_token

    def _login(self):
        s = requests.Session()
        r = s.get('https://my.softbank.jp/msb/d/webLink/doSend/MRERE0000')
        soup = BeautifulSoup(r.text, 'lxml')
        ticket = soup.find('input', type='hidden').get('value')
        payload = {
            'telnum': self.telnum,
            'password': self.password,
            'ticket': ticket
        }
        s.post('https://id.my.softbank.jp/sbid_auth/type1/2.0/login.php', data=payload)
        return s

    def get_data(self):
        login = self._login()
        r = login.get('https://my.softbank.jp/msb/d/webLink/doSend/MRERE0000')
        soup = BeautifulSoup(r.text, 'lxml')
        auth_token = soup.find_all('input')
        payload = {
            'mfiv': auth_token[0].get('value'),
            'mfsb': auth_token[1].get('value'),
        }
        r2 = login.post('https://re11.my.softbank.jp/resfe/top/', data=payload)

        find_data = re.findall('chartType":  "pie",(.+),}]};', r2.text)[0]
        num_data_tmp = "{" + find_data + "}"
        data = ast.literal_eval(num_data_tmp)

        # 使用量
        used_data = "0" if data["usedGigaData"] == "" else data["usedGigaData"]

        # 残量
        remain_data = "0" if data["remainData"] == "" else data["remainData"]

        # 繰越データ残量
        step_remain_data = "0" if data["stepRemainData"] == "" else data["stepRemainData"]

        # 追加データ量
        additional_data = "0" if data["currentAdditionalData"] == "" else data["currentAdditionalData"]

        # 追加データ使用量
        additional_used_data = "0" if data["currentAdditionalUsedData"] == "" else data["currentAdditionalUsedData"]

        # 追加繰越データ量
        given_data = "0" if data["currentGivenData"] == "" else data["currentGivenData"]

        # 追加繰越使用量
        given_used_data = "0" if data["currentGivenUsedData"] == "" else data["currentGivenUsedData"]

        dic = {
            "used_data": float(used_data),
            "remain_data": float(remain_data),
            "step_remain_data": float(step_remain_data),
            "additional_data": float(additional_data),
            "additional_used_data": float(additional_used_data),
            "given_data": float(given_data),
            "given_used_data": float(given_used_data),
        }

        return dic

    def send_message(self):
        data = self.get_data()
        remain = data["remain_data"]
        total = 5.0 + data["step_remain_data"] + data["additional_data"] + data["given_data"]
        rate = round(remain / total * 100, 2)
        text = '\n{}GB / {}GB ({}%)'.format(remain, total, rate)
        line_notify_token = self.line_access_token
        line_notify_api = 'https://notify-api.line.me/api/notify'
        payload = {'message': text}
        headers = {'Authorization': 'Bearer ' + line_notify_token}
        line_notify = requests.post(line_notify_api, data=payload, headers=headers)
        return line_notify.status_code
