from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *

import random



   #Flex_Msg.py
def flex_example():
    list=[0,1,2,3,4,5,6,7,8,9]
    random.shuffle(list)

    
    #將JSON設定為變數content，並以FlexSendMessage()包成Flex Message
    content = {
    
    "type": "bubble",
    "size":"giga",
    
    "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "md",

        "contents": [
        {
            "type": "text",
            "text": "鍵盤",
            "size": "xl",
            "weight": "bold"
        },
        {
            "type": "box",
            "layout": "horizontal",
            "contents": [
            {
                "type": "button",
                "action": {
                "type": "postback",
                "label": "1",
                "data": "1",
                "displayText": "1"
                }
            },
            {
                "type": "button",
                "action": {
                "type": "postback",
                "label": "2",
                "data": "2"
                }
            },
            {
                "type": "button",
                "action": {
                "type": "postback",
                "label": "3",
                "data": "3"
                }
            }
            ]
            
        },
        {
            "type": "box",
            "layout": "horizontal",
            "contents": [
            {
                "type": "button",
                "action": {
                "type": "postback",
                "label": "4",
                "data": "4"
                }
            },
            {
                "type": "button",
                "action": {
                "type": "postback",
                "label": "5",
                "data": "5"
                }
            },
            {
                "type": "button",
                "action": {
                "type": "postback",
                "label": "6",
                "data": "6"
                }
            }
            ]
        },
        {
            "type": "box",
            "layout": "horizontal",
            "contents": [
            {
                "type": "button",
                "action": {
                "type": "postback",
                "label": "7",
                "data": "7"
                }
            },
            {
                "type": "button",
                "action": {
                "type": "postback",
                "label": "8",
                "data": "8"
                }
            },
            {
                "type": "button",
                "action": {
                "type": "postback",
                "label": "9",
                "data": "9"
                }
            }
            ]
        },
        {
            "type": "box",
            "layout": "horizontal",
            "contents": [
            {
                "type": "button",
                "action": {
                "type": "postback",
                "label": "0",
                "data": "0"
                }
            },
            {
                "type": "button",
                "action": {
                "type": "message",
                "label": "確認",
                "text": "確認"
                }
            },
            {
                "type": "button",
                "action": {
                "type": "postback",
                "label": "清除",
                "data": "清除",
                "displayText": "清除"
                }
            }
            ]
        }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": []
    },
    "styles": {
        "body": {
        
        "backgroundColor": "#FF79BC"
        },
        "footer": {
        "backgroundColor": "#FF79BC"
        }
    }
    }

    message=FlexSendMessage(alt_text='FlexMessage範例',contents=content)
    return message