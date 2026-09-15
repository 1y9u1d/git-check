import pandas as pd
import base64

df = pd.read_csv("scores.csv")

df['姓名']= df['姓名'].apply(lambda x: base64.b64decode(x.encode('utf-8')).decode('utf-8'))
df['学校']= df['学校'].apply(lambda x: base64.b64decode(x.encode('utf-8')).decode('utf-8'))


df = df[df['成绩是否有效']=='成绩有效']
sumdf = pd.DataFrame({'平均有效成绩':df.groupby(by=['学校'])['得分'].mean(),
                      '有效成绩中位数':df.groupby(by=['学校'])['得分'].median(),
                      '最高有效成绩':df.groupby(by=['学校'])['得分'].max()})
sumdf.sort_values(by=['有效成绩中位数'], ascending=False, inplace=True)
print(sumdf)