import os
import MySBdt

telnum = os.environ.get("telnum")
password = os.environ.get("password")
line_access_token = os.environ.get("line_access_token")

# インスタンスの作成
api = MySBdt.API(telnum=telnum, password=password, line_access_token=line_access_token)

# データ（使用量、残量、繰越残量、追加量、追加使用量、追加繰越量、追加繰越使用量）の取得
api.get_data()

# lineに通知する
api.send_message()
