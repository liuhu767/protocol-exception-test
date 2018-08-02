#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import requests
import json
import time
import random

url = 'http://xxxxxx/api/message/sendClientMsg'
headers = {'Authorization':"eyJib3RfaWQiOiJ1cyIsInJlc3VsdF90b2tlbiI6ImY0NGQxMDIzLTIzMjMtNDM4My1hYTkzLWZjMGE4ZTg5YjAxYyIsImJvdF90b2tlbiI6Im51bGwifQ",'content-type': "application/json", 'saiyalogid': "awefwgwgrwgrwgr"}
multi_directs = open("directives_multi.txt")
normal_directs = open("directives.txt")


while 1:
    lines = multi_directs.readlines(100000)
    test_uid = "xxxxxx"
    if not lines:
        break
    for line in lines:
        if line == " ":
            continue
        if line.find("data") != -1:
            data = json.loads(line)['data']
        if data.has_key("uid"):
            before_userid = line[0:line.find("uid")]
        if line.find("name") != -1:
            after_name = line[line.find("name"):]
        line = before_userid + 'uid":"' + test_uid + '","' + after_name
        print line
        command = json.loads(line)['data']['data']['directive']['header']['name']
        print command
        response = requests.post(url, data = line, headers = headers)
            # 返回信息
        print response.text
            # 返回响应头
        print response.status_code
        time.sleep(3)
    
multi_directs.close()


while 1:
    lines = normal_directs.readlines(100000)
    test_uid = "a7lvsrpt0q7ex4pzxr4ogxva0dt2udlw|ff31f02122d428e2335e0261"
    if not lines:
        break
    for line in lines:
        if line == " ":
            continue
        if line.find("data") != -1:
            data = json.loads(line)['data']
        if data.has_key("uid"):
            before_userid = line[0:line.find("uid")]
        if line.find("name") != -1:
            after_name = line[line.find("name"):]
        line = before_userid + 'uid":"' + test_uid + '","' + after_name


        #随机删除header里的一个key
        if line.find("header") != -1:
            directive_from = line[0:line.find("header")]
            if line.find("directive") != -1:
                directive_json = json.loads(line)['data']['data']['directive']
                if directive_json.has_key("header"):    
                    directive_header = json.loads(line)['data']['data']['directive']['header']
           
                    #随机删除header里的key
                    if len(directive_header) != 0:
                        keys_number = len(directive_header)
                        delete_number = random.randrange(0,keys_number,1)
                    if delete_number is None or delete_number == 0:    
                        if directive_header.has_key("dialogRequestId"):    
                            del directive_header['dialogRequestId']
                    elif delete_number == 1:
                        del directive_header['namespace']
                    elif delete_number == 2:
                        del directive_header['name']
                    elif delete_number == 3:
                        del directive_header['messageId']
                    print "header:" + str(directive_header)   
                    print "---------------------------------"    
     
        #随机删除payload里的一个key
        if line.find("payload") != -1:
            directive_payload = json.loads(line)['data']['data']['directive']['payload']
            if len(directive_payload) != 0:
                keys_number = len(directive_payload)
                delete_number =  random.randrange(0,keys_number,1)
                #处理payload里有一个key的情况
                if keys_number == 1 :
                    if delete_number is None or delete_number == 0:
                        if directive_payload.has_key("volume"):
                            del directive_payload['volume']
                        if directive_payload.has_key("mute"):
                            del directive_payload['mute']
                        if directive_payload.has_key("endpoint"):
                            del directive_payload['endpoint']
                        if directive_payload.has_key("timeoutInMilliseconds"):
                            del directive_payload['timeoutInMilliseconds']
                #处理payload里有2个key的情况，并且payload里包含url
                elif keys_number == 2 and directive_payload.has_key("url"):
                    if delete_number is None or delete_number == 0:
                        if directive_payload.has_key("url"):
                            del directive_payload['url']
                    elif delete_number == 1:
                        del directive_payload['token']    
                #处理payload里有2个key的情况，并且payload里包含playBehavior
                elif keys_number == 2 and directive_payload.has_key("playBehavior"):
                    if delete_number is None or delete_number == 0:
                        if directive_payload.has_key("playBehavior"):
                            del directive_payload['playBehavior']
                    elif delete_number == 1:
                        del directive_payload['audioItem']
                #处理payload里有3个key的情况,并且payload里包scheduledTime
                elif keys_number == 3 and directive_payload.has_key("scheduledTime"):
                    if delete_number is None or delete_number == 0:
                        if directive_payload.has_key("type"):
                            del directive_payload['type']
                    elif delete_number == 1:
                        del directive_payload['token']
                    elif delete_number == 2:
                        del directive_payload['scheduledTime']
                #处理payload里有3个key的情况,并且payload里包format
                elif keys_number == 3 and directive_payload.has_key("format"):
                      if delete_number is None or delete_number == 0:
                          if directive_payload.has_key("url"):
                              del directive_payload['url']
                      elif delete_number == 1:
                          del directive_payload['token']
                      elif delete_number == 2:
                          del directive_payload['format']
 
          
            #随机删除Play指令中audioItem里的一个key
            if line.find("audioItem") != -1 and json.loads(line)['data']['data']['directive']['header']['name'] == 'Play':
                directive_Play_payload_audioItem = json.loads(line)['data']['data']['directive']['payload']['audioItem']
                if len(directive_Play_payload_audioItem) != 0:
                    keys_number = len(directive_Play_payload_audioItem)
                    delete_number =  random.randrange(0,keys_number,1)
                    #处理payload里有2个key的情况
                    if keys_number == 2:
                        if delete_number is None or delete_number == 0:
                            if directive_Play_payload_audioItem.has_key("audioItemId"):
                                del directive_Play_payload_audioItem['audioItemId']
                        if delete_number is None or delete_number == 1:
                            if directive_Play_payload_audioItem.has_key("stream"):
                                del directive_Play_payload_audioItem['stream']

                #随机删除stream里的一个key---expectedPreviousToken不一定存在
                if line.find("stream") != -1:
                    directive_Play_payload_audioItem_stream = json.loads(line)['data']['data']['directive']['payload']['audioItem']['stream']
                if line.find("progressReport") != -1:
                    directive_Play_payload_audioItem_stream_progressReport = json.loads(line)['data']['data']['directive']['payload']['audioItem']['stream']['progressReport']
           
                    if len(directive_Play_payload_audioItem_stream) != 0:
                        keys_number = len(directive_Play_payload_audioItem_stream)
                        delete_number =  random.randrange(0,keys_number,1)
                        if delete_number is None or delete_number == 0:
                            if directive_Play_payload_audioItem_stream.has_key("url"):
                                del directive_Play_payload_audioItem_stream['url']
                        elif delete_number == 1:
                            if directive_Play_payload_audioItem_stream.has_key("streamFormat"):
                                del directive_Play_payload_audioItem_stream['streamFormat']
                        elif delete_number == 2:
                            if directive_Play_payload_audioItem_stream.has_key("offsetInMilliseconds"):
                                del directive_Play_payload_audioItem_stream['offsetInMilliseconds']
                        elif delete_number == 3:
                            if directive_Play_payload_audioItem_stream.has_key("expiryTime"):
                                del directive_Play_payload_audioItem_stream['expiryTime']
                        elif delete_number == 4:
                            if directive_Play_payload_audioItem_stream.has_key("progressReport"):
                                if directive_Play_payload_audioItem_stream_progressReport.has_key("progressReportDelayInMilliseconds"):
                                    del directive_Play_payload_audioItem_stream_progressReport['progressReportDelayInMilliseconds']
                                if directive_Play_payload_audioItem_stream_progressReport.has_key("progressReportIntervalInMilliseconds"):
                                    del directive_Play_payload_audioItem_stream_progressReport['progressReportIntervalInMilliseconds']
                        elif delete_number == 5:
                            if directive_Play_payload_audioItem_stream.has_key("token"):
                                del directive_Play_payload_audioItem_stream['token']
                        elif delete_number == 6:
                            if directive_Play_payload_audioItem_stream.has_key("expectedPreviousToken"):
                                del directive_Play_payload_audioItem_stream['expectedPreviousToken']

            print "payload:" + str(directive_payload)
            print "---------------------------------"
            body = directive_from + str(directive_header) + ',' + str(directive_payload) + '},"timeout":50000}}}'    
#            print "body:" + str(body)
#            print "---------------------------------"
#        command = json.loads(line)['data']['data']['directive']['header']['name']
#        print command
            response = requests.post(url, data = line, headers = headers)
            # 返回信息
            print response.text
            # 返回响应头
            print response.status_code
            time.sleep(3)
    

    #随机将header里的一个key置空
        if line.find("header") != -1:
            directive_from = line[0:line.find("header")]
            if line.find("directive") != -1:
                directive_json = json.loads(line)['data']['data']['directive']
                if directive_json.has_key("header"):    
                    directive_header = json.loads(line)['data']['data']['directive']['header']
           
                    #随机删除header里的key
                    if len(directive_header) != 0:
                        keys_number = len(directive_header)
                        delete_number = random.randrange(0,keys_number,1)
                    if delete_number is None or delete_number == 0:    
                        if directive_header.has_key("dialogRequestId"):    
                            directive_header['dialogRequestId'] = ""
                    elif delete_number == 1:
                        directive_header['namespace'] = ""
                    elif delete_number == 2:
                        directive_header['name'] = ""
                    elif delete_number == 3:
                        directive_header['messageId'] = ""
                    print "header:" + str(directive_header)   
                    print "---------------------------------"    
     
        #随机将payload里的一个key置空
        if line.find("payload") != -1:
            directive_payload = json.loads(line)['data']['data']['directive']['payload']
            if len(directive_payload) != 0:
                keys_number = len(directive_payload)
                delete_number =  random.randrange(0,keys_number,1)
                #处理payload里有一个key的情况
                if keys_number == 1 :
                    if delete_number is None or delete_number == 0:
                        if directive_payload.has_key("volume"):
                            directive_payload['volume'] = ""
                        if directive_payload.has_key("mute"):
                            directive_payload['mute'] = ""
                        if directive_payload.has_key("endpoint"):
                            directive_payload['endpoint'] = ""
                        if directive_payload.has_key("timeoutInMilliseconds"):
                            directive_payload['timeoutInMilliseconds'] = ""
                #处理payload里有2个key的情况，并且payload里包含url
                elif keys_number == 2 and directive_payload.has_key("url"):
                    if delete_number is None or delete_number == 0:
                        if directive_payload.has_key("url"):
                            directive_payload['url'] = ""
                    elif delete_number == 1:
                        directive_payload['token'] = ""
                #处理payload里有2个key的情况，并且payload里包含playBehavior
                elif keys_number == 2 and directive_payload.has_key("playBehavior"):
                    if delete_number is None or delete_number == 0:
                        if directive_payload.has_key("playBehavior"):
                            directive_payload['playBehavior'] = ""
                    elif delete_number == 1:
                        directive_payload['audioItem'] = ""
                #处理payload里有3个key的情况,并且payload里包scheduledTime
                elif keys_number == 3 and directive_payload.has_key("scheduledTime"):
                    if delete_number is None or delete_number == 0:
                        if directive_payload.has_key("type"):
                            directive_payload['type'] = ""
                    elif delete_number == 1:
                        directive_payload['token'] = ""
                    elif delete_number == 2:
                        directive_payload['scheduledTime'] = ""
                #处理payload里有3个key的情况,并且payload里包format
                elif keys_number == 3 and directive_payload.has_key("format"):
                      if delete_number is None or delete_number == 0:
                          if directive_payload.has_key("url"):
                              directive_payload['url'] = ""
                      elif delete_number == 1:
                          directive_payload['token'] = ""
                      elif delete_number == 2:
                          directive_payload['format'] = ""
 
          
            #随机将Play指令中audioItem里的key置空
            if line.find("audioItem") != -1 and json.loads(line)['data']['data']['directive']['header']['name'] == 'Play':
                directive_Play_payload_audioItem = json.loads(line)['data']['data']['directive']['payload']['audioItem']
                if len(directive_Play_payload_audioItem) != 0:
                    keys_number = len(directive_Play_payload_audioItem)
                    delete_number =  random.randrange(0,keys_number,1)
                    #处理payload里有2个key的情况
                    if keys_number == 2:
                        if delete_number is None or delete_number == 0:
                            if directive_Play_payload_audioItem.has_key("audioItemId"):
                                directive_Play_payload_audioItem['audioItemId'] = ""
                        if delete_number is None or delete_number == 1:
                            if directive_Play_payload_audioItem.has_key("stream"):
                                directive_Play_payload_audioItem['stream'] = ""

                #随机将stream里的key置空---expectedPreviousToken不一定存在
                if line.find("stream") != -1:
                    directive_Play_payload_audioItem_stream = json.loads(line)['data']['data']['directive']['payload']['audioItem']['stream']
                if line.find("progressReport") != -1:
                    directive_Play_payload_audioItem_stream_progressReport = json.loads(line)['data']['data']['directive']['payload']['audioItem']['stream']['progressReport']
           
                    if len(directive_Play_payload_audioItem_stream) != 0:
                        keys_number = len(directive_Play_payload_audioItem_stream)
                        delete_number =  random.randrange(0,keys_number,1)
                        if delete_number is None or delete_number == 0:
                            if directive_Play_payload_audioItem_stream.has_key("url"):
                                directive_Play_payload_audioItem_stream['url'] = ""
                        elif delete_number == 1:
                            if directive_Play_payload_audioItem_stream.has_key("streamFormat"):
                                directive_Play_payload_audioItem_stream['streamFormat'] = ""
                        elif delete_number == 2:
                            if directive_Play_payload_audioItem_stream.has_key("offsetInMilliseconds"):
                                directive_Play_payload_audioItem_stream['offsetInMilliseconds'] = ""
                        elif delete_number == 3:
                            if directive_Play_payload_audioItem_stream.has_key("expiryTime"):
                                directive_Play_payload_audioItem_stream['expiryTime'] = ""
                        elif delete_number == 4:
                            if directive_Play_payload_audioItem_stream.has_key("progressReport"):
                                if directive_Play_payload_audioItem_stream_progressReport.has_key("progressReportDelayInMilliseconds"):
                                    directive_Play_payload_audioItem_stream_progressReport['progressReportDelayInMilliseconds'] = ""
                                if directive_Play_payload_audioItem_stream_progressReport.has_key("progressReportIntervalInMilliseconds"):
                                    directive_Play_payload_audioItem_stream_progressReport['progressReportIntervalInMilliseconds'] = ""
                        elif delete_number == 5:
                            if directive_Play_payload_audioItem_stream.has_key("token"):
                                directive_Play_payload_audioItem_stream['token'] = ""
                        elif delete_number == 6:
                            if directive_Play_payload_audioItem_stream.has_key("expectedPreviousToken"):
                                directive_Play_payload_audioItem_stream['expectedPreviousToken'] = ""

            print "payload:" + str(directive_payload)
            print "---------------------------------"
            body = directive_from + str(directive_header) + ',' + str(directive_payload) + '},"timeout":50000}}}'    
#            print "body:" + str(body)
#            print "---------------------------------"
#        command = json.loads(line)['data']['data']['directive']['header']['name']
#        print command
            response = requests.post(url, data = line, headers = headers)
            # 返回信息
            print response.text
            # 返回响应头
            print response.status_code
            time.sleep(3)



        #随机将header里的一个key置为任意的字符
        if line.find("header") != -1:
            directive_from = line[0:line.find("header")]
            if line.find("directive") != -1:
                directive_json = json.loads(line)['data']['data']['directive']
                if directive_json.has_key("header"):    
                    directive_header = json.loads(line)['data']['data']['directive']['header']
                    #生成随机的字符串
                    random_str = ''
                    base_str = 'abcdefghigklmnopqrstuvwxyz0123456789'
                    length = len(base_str) - 1
                    for i in range(36):
                        random_str += base_str[random.randint(0, length)]
                    #随机置为任意字符
                    if len(directive_header) != 0:
                        keys_number = len(directive_header)
                        delete_number = random.randrange(0,keys_number,1)
                    if delete_number is None or delete_number == 0:    
                        if directive_header.has_key("dialogRequestId"):    
                            directive_header['dialogRequestId'] = random_str
                    elif delete_number == 1:
                        directive_header['namespace'] = random_str
                    elif delete_number == 2:
                        directive_header['name'] = random_str
                    elif delete_number == 3:
                        directive_header['messageId'] = random_str
                    print "header:" + str(directive_header)   
                    print "---------------------------------"    
     
        #随机将payload里的key置为任意的字符
        if line.find("payload") != -1:
            directive_payload = json.loads(line)['data']['data']['directive']['payload']
            if len(directive_payload) != 0:
                keys_number = len(directive_payload)
                delete_number =  random.randrange(0,keys_number,1)
                #生成随机的字符串
                random_str = ''
                base_str = 'abcdefghigklmnopqrstuvwxyz0123456789'
                length = len(base_str) - 1
                for i in range(36):
                    random_str += base_str[random.randint(0, length)]
                #处理payload里有一个key的情况
                if keys_number == 1 :
                    if delete_number is None or delete_number == 0:
                        if directive_payload.has_key("volume"):
                            directive_payload['volume'] = random_str
                        if directive_payload.has_key("mute"):
                            directive_payload['mute'] = random_str
                        if directive_payload.has_key("endpoint"):
                            directive_payload['endpoint'] = random_str
                        if directive_payload.has_key("timeoutInMilliseconds"):
                            directive_payload['timeoutInMilliseconds'] = random_str
                #处理payload里有2个key的情况，并且payload里包含url
                elif keys_number == 2 and directive_payload.has_key("url"):
                    if delete_number is None or delete_number == 0:
                        if directive_payload.has_key("url"):
                            directive_payload['url'] = random_str
                    elif delete_number == 1:
                        directive_payload['token'] = random_str
                #处理payload里有2个key的情况，并且payload里包含playBehavior
                elif keys_number == 2 and directive_payload.has_key("playBehavior"):
                    if delete_number is None or delete_number == 0:
                        if directive_payload.has_key("playBehavior"):
                            directive_payload['playBehavior'] = random_str
                    elif delete_number == 1:
                        directive_payload['audioItem'] = random_str
                #处理payload里有3个key的情况,并且payload里包scheduledTime
                elif keys_number == 3 and directive_payload.has_key("scheduledTime"):
                    if delete_number is None or delete_number == 0:
                        if directive_payload.has_key("type"):
                            directive_payload['type'] = random_str
                    elif delete_number == 1:
                        directive_payload['token'] = random_str
                    elif delete_number == 2:
                        directive_payload['scheduledTime'] = random_str
                #处理payload里有3个key的情况,并且payload里包format
                elif keys_number == 3 and directive_payload.has_key("format"):
                      if delete_number is None or delete_number == 0:
                          if directive_payload.has_key("url"):
                              directive_payload['url'] = random_str
                      elif delete_number == 1:
                          directive_payload['token'] = random_str
                      elif delete_number == 2:
                          directive_payload['format'] = random_str
 
          
            #随机将Play指令中audioItem里的key置为任意字符
            if line.find("audioItem") != -1 and json.loads(line)['data']['data']['directive']['header']['name'] == 'Play':
                directive_Play_payload_audioItem = json.loads(line)['data']['data']['directive']['payload']['audioItem']
                #生成随机的字符串
                random_str = ''
                base_str = 'abcdefghigklmnopqrstuvwxyz0123456789'
                length = len(base_str) - 1
                for i in range(36):
                    random_str += base_str[random.randint(0, length)]

                if len(directive_Play_payload_audioItem) != 0:
                    keys_number = len(directive_Play_payload_audioItem)
                    delete_number =  random.randrange(0,keys_number,1)
                    #处理payload里有2个key的情况
                    if keys_number == 2:
                        if delete_number is None or delete_number == 0:
                            if directive_Play_payload_audioItem.has_key("audioItemId"):
                                directive_Play_payload_audioItem['audioItemId'] = random_str
                        if delete_number is None or delete_number == 1:
                            if directive_Play_payload_audioItem.has_key("stream"):
                                directive_Play_payload_audioItem['stream'] = random_str

                #随机将stream里的key置为任意字符串---expectedPreviousToken不一定存在
                if line.find("stream") != -1:
                    directive_Play_payload_audioItem_stream = json.loads(line)['data']['data']['directive']['payload']['audioItem']['stream']
                if line.find("progressReport") != -1:
                    directive_Play_payload_audioItem_stream_progressReport = json.loads(line)['data']['data']['directive']['payload']['audioItem']['stream']['progressReport']
           
                    if len(directive_Play_payload_audioItem_stream) != 0:
                        keys_number = len(directive_Play_payload_audioItem_stream)
                        delete_number =  random.randrange(0,keys_number,1)
                        if delete_number is None or delete_number == 0:
                            if directive_Play_payload_audioItem_stream.has_key("url"):
                                directive_Play_payload_audioItem_stream['url'] = random_str
                        elif delete_number == 1:
                            if directive_Play_payload_audioItem_stream.has_key("streamFormat"):
                                directive_Play_payload_audioItem_stream['streamFormat'] = random_str
                        elif delete_number == 2:
                            if directive_Play_payload_audioItem_stream.has_key("offsetInMilliseconds"):
                                directive_Play_payload_audioItem_stream['offsetInMilliseconds'] = random_str
                        elif delete_number == 3:
                            if directive_Play_payload_audioItem_stream.has_key("expiryTime"):
                                directive_Play_payload_audioItem_stream['expiryTime'] = random_str
                        elif delete_number == 4:
                            if directive_Play_payload_audioItem_stream.has_key("progressReport"):
                                if directive_Play_payload_audioItem_stream_progressReport.has_key("progressReportDelayInMilliseconds"):
                                    directive_Play_payload_audioItem_stream_progressReport['progressReportDelayInMilliseconds'] = random_str
                                if directive_Play_payload_audioItem_stream_progressReport.has_key("progressReportIntervalInMilliseconds"):
                                    directive_Play_payload_audioItem_stream_progressReport['progressReportIntervalInMilliseconds'] = random_str
                        elif delete_number == 5:
                            if directive_Play_payload_audioItem_stream.has_key("token"):
                                directive_Play_payload_audioItem_stream['token'] = random_str
                        elif delete_number == 6:
                            if directive_Play_payload_audioItem_stream.has_key("expectedPreviousToken"):
                                directive_Play_payload_audioItem_stream['expectedPreviousToken'] = random_str

            print "payload:" + str(directive_payload)
            print "---------------------------------"
            body = directive_from + str(directive_header) + ',' + str(directive_payload) + '},"timeout":50000}}}'    
 #           print "body:" + str(body)
 #           print "---------------------------------"
#        command = json.loads(line)['data']['data']['directive']['header']['name']
#        print command
            response = requests.post(url, data = line, headers = headers)
            # 返回信息
            print response.text
            # 返回响应头
            print response.status_code
            time.sleep(3)


        #在header里增加一个key
        if line.find("header") != -1:
            directive_from = line[0:line.find("header")]
            if line.find("directive") != -1:
                directive_json = json.loads(line)['data']['data']['directive']
                if directive_json.has_key("header"):    
                    directive_header = json.loads(line)['data']['data']['directive']['header']
                    directive_header['status'] = "fweffawef"
                    print "header:" + str(directive_header)   
                    print "---------------------------------"    
     
        #在payload里的增加一个key
        if line.find("payload") != -1:
            directive_payload = json.loads(line)['data']['data']['directive']['payload']
            directive_payload['status_code'] = "wefafwf"
          
            #在Play指令中audioItem里的一个key
            if line.find("audioItem") != -1 and json.loads(line)['data']['data']['directive']['header']['name'] == 'Play':
                directive_Play_payload_audioItem = json.loads(line)['data']['data']['directive']['payload']['audioItem']
                directive_Play_payload_audioItem['expect'] = "fwaegag"

                #随机删除stream里的一个key---expectedPreviousToken不一定存在
                if line.find("stream") != -1:
                    directive_Play_payload_audioItem_stream = json.loads(line)['data']['data']['directive']['payload']['audioItem']['stream']
                    directive_Play_payload_audioItem_stream['command'] = "wfoijke"
                if line.find("progressReport") != -1:
                    directive_Play_payload_audioItem_stream_progressReport = json.loads(line)['data']['data']['directive']['payload']['audioItem']['stream']['progressReport']
                    directive_Play_payload_audioItem_stream_progressReport['progress'] = "fpoikie"
                    
            print "payload:" + str(directive_payload)
            print "---------------------------------"
            body = directive_from + str(directive_header) + ',' + str(directive_payload) + '},"timeout":50000}}}'    
#            print "body:" + str(body)
#            print "---------------------------------"
#        command = json.loads(line)['data']['data']['directive']['header']['name']
#        print command
            response = requests.post(url, data = line, headers = headers)
            # 返回信息
            print response.text
            # 返回响应头
            print response.status_code
            time.sleep(3)


        print "--------多个指令----------------------多个指令------------------------多个指令---------------"
        #在data里增加多个指令
        if line.find("directive") != -1:
            before_directive = line[0:line.find("directive")]
            directive_data = json.loads(line)['data']['data']['directive']
            timeout = line[0:line.find("timeout")]
            multi_number = random.randrange(0,5,1)
            if multi_number is None or multi_number == 0:        
                line = before_directive + "" + '"' + ',"' + timeout
            elif multi_number == 1:
                line = before_directive + 'directive":' + json.dumps(directive_data) + ',"timeout": 50000}}}'
            elif multi_number == 2:
                line = before_directive + 'directive":' + json.dumps(directive_data) + ',"' + 'directive":' + json.dumps(directive_data) + ',"timeout": 50000}}}'
            elif multi_number == 3:
                line = before_directive + 'directive":' + json.dumps(directive_data) + ',"' + 'directive":' + json.dumps(directive_data) + ',"' + 'directive":' + json.dumps(directive_data) + ',"timeout": 50000}}}'
            elif multi_number == 4:
                line = before_directive + 'directive":' + json.dumps(directive_data) + ',"' + 'directive":' + json.dumps(directive_data) + ',"' + 'directive":' + json.dumps(directive_data) + ',"' + 'directive":' + json.dumps(directive_data) +',"timeout": 50000}}}'    
    
            print line
            response = requests.post(url, data = line, headers = headers)
            # 返回信息
            print response.text
            # 返回响应头
            print response.status_code
            time.sleep(3)

normal_directs.close()
           
