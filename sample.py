import mysoftbank

# LINEに通知する場合は以下のURLからLINE Notifyのアクセストークンを取得する必要があります。
# https://notify-bot.line.me/ja/

telnum = "電話番号"
password = "MySoftbankのパスワード"
line_access_token = "LineNotifyのアクセストークン"

# インスタンスの作成
api = mysoftbank.API(telnum=telnum, password=password, line_access_token=line_access_token)

# データ（使用量、残量、繰越残量、追加量、追加使用量、追加繰越量、追加繰越使用量）の取得
api.get_data()

# lineに通知する
api.send_message()
