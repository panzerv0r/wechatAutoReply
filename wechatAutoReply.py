# _*_ coding:utf-8 _*_
# __author__='Shiqing Xu'
import re
import time
import itchat
from itchat.content import *


@itchat.msg_register([TEXT])
def text_reply(msg):
    friend = itchat.search_friends(userName=msg['FromUserName'])
    replycontent = "收到您于%s发送的【%s】" % (time.strftime('%m-%d %H:%M', time.localtime()), msg['Type'])
    if msg['Type'] == 'Text':
        if re.search(r"新年快乐", msg['Content']):
            replycontent += "新年快乐！"
    itchat.send("好友:【%s（昵称：%s）】于：【%s】发来消息: 【%s】" % (
        friend['NickName'], friend['RemarkName'], time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), msg['Text']),
                toUserName='filehelper')
    itchat.send(replycontent, toUserName=msg['FromUserName'])
    print("于【%s】收到好友【%s（昵称：%s）】发来的【%s】: 【%s】" % (
            time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), friend['NickName'], friend['RemarkName'], msg['Type'],
            msg['Content']))
    print("于【%s】回复：%s" % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), replycontent) + '\n')


itchat.auto_login(hotReload=True)
itchat.run()
