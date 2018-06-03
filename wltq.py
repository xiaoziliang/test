# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import json
import urllib.request as r
url = 'http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric '

info = r.urlopen(url.format('leshan')).read().decode('utf-8','ignore')
data = json.loads(info)
print("[0-4]是2018/6/1")
print("[5-9]是2018/6/2")
print("[10-14]是2018/6/3")
print("[15-19]是2018/6/4")
print("[20-24]是2018/6/5")
i = input("请输入0-24的数字：")
tq = {'weather': data['list'][int(i)]['weather'][0]['description'],
      'temp' : data['list'][int(i)]['main']['temp'],
      'temp_min' : data['list'][int(i)]['main']['temp_min'],
      'temp_max' : data['list'][int(i)]['main']['temp_max'],
      'pressure' : data['list'][int(i)]['main']['pressure'],
      'day' : data['list'][int(i)]['dt_txt']
      }
print("{}的天气是{},最高温度是{},最低温度是{},气压是{}".format(tq['day'],tq['weather'],tq['temp_max'],tq['temp_min'],tq['pressure']))
