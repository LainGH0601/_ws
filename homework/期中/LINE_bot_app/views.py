from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *

from LINE_bot_app.models import *
from LINE_bot_app.flex_M import *


import hashlib
import paho.mqtt.client as mqtt

import jieba

from django.shortcuts import render
from django.shortcuts import redirect


import string
import time
import base64
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage


line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


password=''

dict={}


@csrf_exempt
def callback(request):
    d_input={}

    global dict 
    global password
    if request.method == 'POST':
        message=[]
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
       
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                
                uid=event.source.user_id
                profile=line_bot_api.get_profile(uid)
                name=profile.display_name
                pic_url=profile.picture_url
                
                

                
                
                print(event.message.type)
                if event.message.type=='text':
                    mtext=event.message.text
                    if '登入' in mtext:
                        
                        message.append(TextSendMessage(text='輸入你的密碼'))
                        message.append(flex_example())

                       

                                        
                        
                        dict[uid]=''#程式更新後，如未按登入鍵直接開始輸入會有問題
                    elif '確認' in mtext:
                        if dict[uid]=='':
                            message.append(TextSendMessage(text='密碼不可為空!'))
                            user_info = User_Info.objects.filter(uid=uid)
                        else:
                            stringData =dict[uid]
                            utf8Data = stringData.encode('utf-8')
                            hashString = hashlib.sha256(utf8Data).hexdigest()
                            print(hashString)

                            if User_Info.objects.filter(uid=uid).exists()==False:
                                
                                User_Info.objects.create(uid=uid,name=name,pic_url=pic_url,mtext=mtext,password=hashString)
                                message.append(TextSendMessage(text='正在創建帳號...'))
                                user_info = User_Info.objects.filter(uid=uid)
                                for user in user_info:
                                    info = '註冊成功'+'UID=%s\nNAME=%s\n大頭貼=%s'%(user.uid,user.name,user.pic_url)
                                    message.append(TextSendMessage(text=info))
                                dict[uid]=''
                            elif User_Info.objects.filter(uid=uid).exists()==True:
                                
                                ma='正在登入帳號...密碼是'+dict[uid]
                                
                                message.append(TextSendMessage(text=ma))
                                if User_Info.objects.filter(uid=uid,password=hashString).exists()==False:
                                    
                                    message.append(TextSendMessage(text='密碼不正確'))
                                    # sticker_message = StickerMessage(
                                    #     package_Id= "11537",
                                    #     sticker_Id= "52002736"
                                    # )
                                    
                                elif User_Info.objects.filter(uid=uid,password=hashString).exists()==True:
                                    
                                    user_info = User_Info.objects.filter(uid=uid)
                                    for user in user_info:
                                        info = '登入成功'+'UID=%s\nNAME=%s\n大頭貼=%s'%(user.uid,user.name,user.pic_url)
                                        message.append(TextSendMessage(text=info))
                                dict[uid]=''
                    
   
                    else:
                        message.append(TextSendMessage(text='1'))
                        message=TextSendMessage(
                            text="文字訊息",
                            quick_reply=QuickReply(
                                items=[
                                    
                                    QuickReplyButton(
                                        action=MessageAction(label="登入",text="登入")
                                        ),
                                    QuickReplyButton(
                                        action=PostbackAction(label="Postback",data="回傳資料")
                                        ),
                                    QuickReplyButton(
                                        action=MessageAction(label="文字訊息",text="回傳文字")
                                        ),
                                    QuickReplyButton(
                                        action=DatetimePickerAction(label="時間選擇",data="時間選擇",mode='datetime')
                                        ),
                                    QuickReplyButton(
                                        action=CameraAction(label="拍照")
                                        ),
                                    QuickReplyButton(
                                        action=CameraRollAction(label="相簿")
                                        ),
                                    QuickReplyButton(
                                        action=LocationAction(label="傳送位置")
                                        )
                                    ]
                                )
                            )
                        # emoji = [
                        #     {
                        #         "index": 0,
                        #         "productId": "5ac1bfd5040ab15980c9b435",
                        #         "emojiId": "001"
                        #     },
                        #     {
                        #         "index": 13,
                        #         "productId": "5ac1bfd5040ab15980c9b435",
                        #         "emojiId": "002"
                        #     }
                        # ]
                        # message = TextSendMessage(text='$ LINE emoji $', emojis=emoji)
                        
                        # seg_list = jieba.lcut(mtext)
                        # print(seg_list)
                        # text=''
                        # for jword in range(0,len(seg_list)):
                            
                        #     text=text+"/"+seg_list[jword] 
                        
                            
            
                        # message = TextSendMessage(text)#=seg_list[0]+'/'+seg_list[1]+'/'+seg_list[2]+'/'+seg_list[3]+'/'+seg_list[4])
                        

                        # message = StickerSendMessage(package_id= "1",sticker_id= "3")

                        # message = LocationSendMessage(title= "1",address= "3",latitude=24.44907,longitude= 118.3206)

                        # message = VideoSendMessage(
                        #     original_content_url='https://i.imgur.com/WS3dQe3.mp4', # 影片的網址，可以參考圖片的上傳方式
                        #     preview_image_url='https://i.imgur.com/wpM584d.jpg' # 影片預覽的圖片
                        # )
                        # message=TextSendMessage(
                        #     text="文字訊息",
                        #     quick_reply=QuickReply(
                        #         items=[
                        #             QuickReplyButton(
                        #                 action=PostbackAction(label="Postback",data="回傳資料")
                        #                 ),
                        #             QuickReplyButton(
                        #                 action=MessageAction(label="文字訊息",text="回傳文字")
                        #                 ),
                        #             QuickReplyButton(
                        #                 action=DatetimePickerAction(label="時間選擇",data="時間選擇",mode='datetime')
                        #                 ),
                        #             QuickReplyButton(
                        #                 action=CameraAction(label="拍照")
                        #                 ),
                        #             QuickReplyButton(
                        #                 action=CameraRollAction(label="相簿")
                        #                 ),
                        #             QuickReplyButton(
                        #                 action=LocationAction(label="傳送位置")
                        #                 )
                        #             ]
                        #         )
                        #     )
                                                
               
                        
                        

                #     line_bot_api.reply_message(event.reply_token,message)
                # elif event.message.type=='image':  
                #     message.append(ImageSendMessage('https://en.wikipedia.org/wiki/Neko_Atsume#/media/File:Neko_atsume_logo.png'))
                    line_bot_api.reply_message(event.reply_token,message)

                elif event.message.type=='image':
                    message.append(TextSendMessage(text='圖片訊息'))
                    line_bot_api.reply_message(event.reply_token,message)

                elif event.message.type=='location':
                    message.append(TextSendMessage(text='位置訊息'))
                    line_bot_api.reply_message(event.reply_token,message)

                elif event.message.type=='video':
                    message.append(TextSendMessage(text='影片訊息'))
                    line_bot_api.reply_message(event.reply_token,message)


                elif event.message.type=='sticker':
                    message.append(TextSendMessage(text='貼圖訊息'))
                    line_bot_api.reply_message(event.reply_token,message)

                elif event.message.type=='audio':
                    message.append(TextSendMessage(text='聲音訊息'))
                    line_bot_api.reply_message(event.reply_token,message)

                elif event.message.type=='file':
                    message.append(TextSendMessage(text='檔案訊息'))
                    line_bot_api.reply_message(event.reply_token,message)

            elif isinstance(event, PostbackEvent):
                uid=event.source.user_id
                if '清除' in event.postback.data:
                        dict[uid]=''
                else:   
                      
                    print(event.postback.data)  
                    d_input[uid]=event.postback.data
                    dict[uid] = dict[uid]+d_input[uid]
                    #password=password+dict[uid]
                    
                    print(dict[uid])
                

        return HttpResponse()
    else:
        return HttpResponseBadRequest()




