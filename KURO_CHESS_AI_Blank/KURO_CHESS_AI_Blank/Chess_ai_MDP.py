import numpy as np
import pandas as pd
import json
import random
def make_dic(words,dic):
    tmp=["@"]
    for word in words:
        tmp.append(word)

        if len(tmp) < 3:continue
        if len(tmp) > 3: tmp=tmp[1:]

        set_word3(dic,tmp)

    return dic

def set_word3(dic,s3):
    w1,w2,w3=s3

    if not w1 in dic:
        dic[w1]={}
    if not w2 in dic[w1]:
        dic[w1][w2]={}
    if not w3 in dic[w1][w2]:
        dic[w1][w2][w3]=0
    dic[w1][w2][w3]=dic[w1][w2][w3]+1
    
def predict_next(data,dic):
    if len(data)>=2:
        s=data[len(data)-2:len(data)]
    elif len(data)==1:
        s=data[0]
        keys=dic[s].keys()
        return random.choice(list(keys))
    else:
        keys=dic['@'].keys()
        return random.choice(list(keys))
    w1,w2=s
    return random.choice(list(dic[w1][w2].keys()))
def predict_next(data,dic):
    if len(data)>=2:
        s=data[len(data)-2:len(data)]
    elif len(data)==1:
        s=data[0]
        keys=dic[s].keys()
        return random.choice(list(keys))
    else:
        keys=dic['@'].keys()
        return random.choice(list(keys))
    w1,w2=s
    return random.choice(list(dic[w1][w2].keys()))
"""
data=pd.read_csv('data.csv')
chess_datas=[]
for x in range(0,len(data['PGN'])):
    tmp=data['PGN'][x].split()
    tmp2=[]
    for y in range(0,len(tmp)):
        if y%3!=0:
            tmp2.append(tmp[y])
    chess_datas.append(tmp2)
dic={}
for x in chess_datas:
    make_dic(x,dic)
print('complete!')
print(predict_next([],dic))
with open("./chess_data.json", 'w') as outfile:
    json.dump(dic,outfile)
"""