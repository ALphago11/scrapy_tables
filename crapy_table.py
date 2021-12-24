import requests
import pandas as pd
url="http://xxfb.mwr.cn/hydroSearch/greatRiver"
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
req=requests.get(url=url,headers=headers)
text=eval(req.text)['result']
date=text['date']
df=pd.DataFrame(text['data'])
df.to_csv(date+'_greatRiver.csv')