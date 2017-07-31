import itchat
import  requests

TULING_KEY = '33d276e93843c8385e94a08c6c7ec878'

def get_reply(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key' : TULING_KEY,
        'info' : msg,
#        'loc' : '广东省惠州市',
        'userid' : '大神彭',
    }
    try:
        r = requests.post(apiUrl,data=data).json()
        return r.get("text")
    except:
        return None

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = '呵'
    reply = get_reply(msg['Text'])
    return reply or defaultReply


itchat.auto_login(hotReload=True,enableCmdQR=2)
itchat.run()
