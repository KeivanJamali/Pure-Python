# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 22:05:02 2021

@author: KPS
"""

from urllib.request import urlopen
from urllib.parse import quote
import time, json


def decode(a):
    decoded = ''
    for line in a:
        decoded += line.decode('utf-8')
    return decoded


Token = '1619994074:AAFyW3rHYZShaTziTcTvNTvNPwAIbsan0no'
URL = f'https://api.telegram.org/bot{Token}/'
cmd = 'getme'

resp = urlopen(URL + cmd)
de_resp = decode(resp)
dic_resp = json.loads(de_resp)
Bool = 0

while True:
    
    
    cmd = 'getUpdates'
    upd = urlopen(URL + cmd)
    de_upd = decode(upd)
    dic_upd = json.loads(de_upd)
    
    if len(dic_upd['result']) == 0:
        print('waiting')
        time.sleep(1)

    for i in range(0, len(dic_upd['result'])):
        msg = dic_upd['result'][i]['message']
        upd_id = dic_upd['result'][i]['update_id']
        msg_id = msg['chat']['id']
            
        if 'text' in msg:
                
                
            if msg['text'] == '/command1':
                text = 'بوگو خب'
                text = quote(text.encode('utf-8'))
                cmd = 'sendMessage'
                smsg = urlopen(URL + cmd + f'?chat_id={msg_id}&text={text}')
                de_smsg = decode(smsg)
                dic_smsg = json.loads(de_smsg)
                if dic_smsg['ok']:
                    cmd = 'getUpdates'
                    urlopen(URL + cmd + f'?offset={upd_id+1}')
                Bool = 2
            elif type(msg['text']) == str and Bool == 2:
                text = 'حالا خیلی واجبه؟  عامو جون جدت حسش نی، بیخیال شو!'
                text = quote(text.encode('utf-8'))
                cmd = 'sendMessage'
                smsg = urlopen(URL + cmd + f'?chat_id={msg_id}&text={text}')
                de_smsg = decode(smsg)
                dic_smsg = json.loads(de_smsg)
                if dic_smsg['ok']:
                    cmd = 'getUpdates'
                    urlopen(URL + cmd + f'?offset={upd_id+1}')
                Bool = 0
                
                
            if msg['text'] == '/command2':
                    text = 'خو برو تو گوگل بزن، مگه من بیکارم'
                    text = quote(text.encode('utf-8'))
                    cmd = 'sendMessage'
                    smsg = urlopen(URL + cmd + f'?chat_id={msg_id}&text={text}')
                    de_smsg = decode(smsg)
                    dic_smsg = json.loads(de_smsg)
                    if dic_smsg['ok']:
                        cmd = 'getUpdates'
                        urlopen(URL + cmd + f'?offset={upd_id+1}')
                    ch = 1
                        
                        
            if msg['text'] == '/command3':
                    text = 'حالا کیو پیدا کنم؟'
                    text = quote(text.encode('utf-8'))
                    cmd = 'sendMessage'
                    smsg = urlopen(URL + cmd + f'?chat_id={msg_id}&text={text}')
                    de_smsg = decode(smsg)
                    dic_smsg = json.loads(de_smsg)
                    if dic_smsg['ok']:
                        cmd = 'getUpdates'
                        urlopen(URL + cmd + f'?offset={upd_id+1}')
                    Bool = 1
            elif type(msg['text']) == str and Bool == 1:
                    text = 'باید همین دور و برا باشه، حسش میکنم. خوب بگرد.'
                    text = quote(text.encode('utf-8'))
                    cmd = 'sendMessage'
                    smsg = urlopen(URL + cmd + f'?chat_id={msg_id}&text={text}')
                    de_smsg = decode(smsg)
                    dic_smsg = json.loads(de_smsg)
                    if dic_smsg['ok']:
                        cmd = 'getUpdates'
                        urlopen(URL + cmd + f'?offset={upd_id+1}')
                    Bool = 0
                        
                        
            if msg['text'] == '/command4':
                    text = 'دستته خب الاغ😑'
                    text = quote(text.encode('utf-8'))
                    cmd = 'sendMessage'
                    smsg = urlopen(URL + cmd + f'?chat_id={msg_id}&text={text}')
                    de_smsg = decode(smsg)
                    dic_smsg = json.loads(de_smsg)
                    if dic_smsg['ok']:
                        cmd = 'getUpdates'
                        urlopen(URL + cmd + f'?offset={upd_id+1}')
                        
                        
            if msg['text'] == '/command5':
                    text = 'not in range😂'
                    text = quote(text.encode('utf-8'))
                    cmd = 'sendMessage'
                    smsg = urlopen(URL + cmd + f'?chat_id={msg_id}&text={text}')
                    de_smsg = decode(smsg)
                    dic_smsg = json.loads(de_smsg)
                    if dic_smsg['ok']:
                        cmd = 'getUpdates'
                        urlopen(URL + cmd + f'?offset={upd_id+1}')
                    
                    
                # if ch == 0:
                #     text = 'من اگه چیزی گفتی یادم رفته، دوباره با command ها باهام ارتباط بگیر.'
                #     text = quote(text.encode('utf-8'))
                #     cmd = 'sendMessage'
                #     smsg = urlopen(URL + cmd + f'?chat_id={msg_id}&text={text}')
                #     de_smsg = decode(smsg)
                #     dic_smsg = json.loads(de_smsg)
                #     if dic_smsg['ok']:
                #         cmd = 'getUpdates'
                #         urlopen(URL + cmd + f'?offset={upd_id+1}')
            else:
                    cmd = 'getUpdates'
                    urlopen(URL + cmd + f'?offset={upd_id+1}')
                
                
                
                
                
                
                
                
            
            
        