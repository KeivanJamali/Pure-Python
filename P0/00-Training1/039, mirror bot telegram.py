# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 18:25:57 2021

@author: KPS
"""

from urllib.request import urlopen
from urllib.parse import quote
import json, time


def decode(resp):
    decoded = ''
    for line in resp:
        decoded += line.decode('utf-8')
    return decoded
        
        
Token = '1619994074:AAFyW3rHYZShaTziTcTvNTvNPwAIbsan0no'
URL = f'https://api.telegram.org/bot{Token}/'
cmd = 'getme'
resp = urlopen(URL + cmd)
de_resp = decode(resp)
dic_resp = json.loads(de_resp)


while True:
    cmd = 'getUpdates'
    upd = urlopen(URL + cmd)
    de_upd = decode(upd)
    dic_upd = json.loads(de_upd)
    
    if len(dic_upd['result']) == 0:
        print('wait')
        time.sleep(3)
    else:
        msg = dic_upd['result'][0]['message']
        msg_Id = msg['chat']['id']
        if 'text' in msg:
            msg_text = quote(msg['text'].encode('utf-8'))
            
            cmd = 'sendMessage'
            smsg = urlopen(URL + cmd + f'?chat_id={msg_Id}&text={ msg_text}')
            de_smsg = decode(smsg)
            dic_smsg = json.loads(de_smsg)
            
            if dic_smsg['ok']:
                update_Id = dic_upd['result'][0]['update_id']
                cmd = 'getUpdates'
                urlopen(URL + cmd + f'?offset={update_Id+1}')
        else:
            update_Id = dic_upd['result'][0]['update_id']
            cmd = 'getUpdates'
            urlopen(URL + cmd + f'?offset={update_Id+1}')
        
        
        
        
        