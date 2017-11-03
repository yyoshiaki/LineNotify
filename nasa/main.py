import datetime
import requests

from nasa import apod


# やること
# https://api.nasa.gov/index.html#getting-startedでNASAのAPI keyを取得
# pip install nasa-api-wraper

# Linux
# echo export NASA_API_KEY='所得したAPI key' >> ~/.bashrc && source ~/.bashrc

# Mac
# echo export NASA_API_KEY='所得したAPI key' >> ~/.bash_profile && source ~/.bash_profile


# python main.pyで動作確認。
# pip install schedule
# python ex_everyday.py &で定時実行
# ctrl+z, kill %num_jobで止める。


def GetImageAst(date, image_name):
    pic = apod.apod('{y}-{m}-{d}'.format(y=date.year, m=date.month, d=date.day))
    # NASAのAPIから取得した画像をダウンロード。
    res = requests.get(pic.url)
    if res.status_code == 200:
        with open(image_name, 'wb') as file:
            file.write(res.content)
            
            
def SendImage(image_name, line_notify_token):
    # ダウンロードした画像をLINEで送信。
    line_notify_api = 'https://notify-api.line.me/api/notify'
    message = '今日の宇宙。　#NASA'
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}  # 発行したトークン
    files = {"imageFile": open(image_name, "rb")}
    line_notify = requests.post(line_notify_api, data=payload, files=files, headers=headers)
    

def main(line_notify_token='aJnuEOsetjSgZR6GwqCAVOT2bUKSA0bSpf8N0f75TAw',
         date=datetime.date.today(),
         image_name = 'data/Ast_{y}_{m}_{d}.jpg'.format(y=datetime.date.today().year, m=datetime.date.today().month,
                                                        d=datetime.date.today().day)):
    GetImageAst(date, image_name)
    SendImage(image_name, line_notify_token)
    
    
if __name__ == '__main__':
    main()