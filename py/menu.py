from flask import request
from monitor import API
import re
import requests
import json


def menu():
    data = request.get_json()
    message = data['message']

    if "menu" == message:
        a = "This is a clumsy menu：[CQ:face,id=101][CQ:face,id=101][CQ:shake]\n " \
            "1.Tell a joke (the joke may be repetitive, please understand)\n " \
            "2.What holiday is today\n " \
            "3.Song ordering rules\n " \
            "4.Query time (although it's not really useful)\n " \
            "5.What's the weather like today\n "  \
            "6.Licking Dog Diary\n " \
            "7.A word of the day\n " \
            "8.Random Music [NetEase Cloud Hot Song Chart Random Music]\n " \
            "9.Comfort copy\n " \
            "10.\n " \
            "Special menu：\n "\
            "About the author"
        API.send(a)

    elif "笨笨" == message:
        API.send("我在呀！" + '[CQ:face,id=20][CQ:face,id=20][CQ:face,id=20]')

    elif "笨笨，在吗" == message:
        API.send("笨笨一直在的哦！" + '[CQ:face,id=21][CQ:face,id=21]')

    elif "在吗" == message:
        API.send("笨笨一直在的哦！" + '[CQ:face,id=21][CQ:face,id=21]')

    elif "在干嘛" == message:
        API.send("[CQ:face,id=13][CQ:face,id=13][CQ:face,id=13]\n" + '每个人都是要学习的，就算是机器人也需要哦，快去忙你的叭~')

    elif "抱抱" == message:
        API.send("[CQ:face,id=49][CQ:face,id=49][CQ:face,id=49]")

    elif "关于作者" == message:
        API.send('作者当然是阿轩不会修电脑，善良勇敢聪明帅气集一身的A fierce man[猛男的意思]\n[笨笨都觉得不要脸,不知道他是怎么敢的]' +
                 '[CQ:face,id=0][CQ:face,id=0][CQ:face,id=0]\n'
                 '\n作者讲话：\nHello哇，这里是阿轩，目前我还是一个小白，第一次接触这个机器人框架，希望大家理解，不喜勿喷，感谢大家的支持和使用'
                 '\n小轩机器人是基于go-cqhttp开发的QQ机器人，部署在linux平台上面，目前还在开发中...'
                 '\n了解更多在我的Gitee主页：\nhttps://gitee.com/save-a-pocket-of-stars'
                 '\n这是机器人代码仓库：\nhttps://gitee.com/save-a-pocket-of-stars/qq-cqhttp\n内容仅供参考,仓库里面有开发帮助，可供使用')

    elif "小黑子" == message:
        API.send('小黑子，不要鸡叫了：'
                 +
                 "[CQ:image,file=https://image.yunyingpai.com/wp/2019/04/2J06j1jbmg2yDSQxlQgE.gif]"
                 +
                 "[CQ:face,id=178][CQ:face,id=178][CQ:face,id=178]")

    elif "点歌规则" == message:
        API.send("[格式为：点歌-歌的名字\n作者是废物，不会交互式点歌，所以目前点歌量比较少\n输入“点歌菜单”可以查看有哪些歌哦]"
                 +
                 "[CQ:face,id=179][CQ:face,id=179][CQ:face,id=179]")

    elif "点歌菜单" == message:
        a = '[《11》《再见》]\n' \
            '[《倒数》《寂寞烟火》]\n' \
            '[《特别的人》《意外》]\n' \
            '[《你不是真正的快乐》]\n' \
            '[《喜欢你》《光年之外》]\n' \
            '[《我们的歌》《我记得》]\n' \
            '[《哪里都是你》《我的秘密》]\n' \
            '[《山楂树之恋》《在你的身边》]\n' \
            '作者会持续更新，你们可以把自己喜欢的歌在我的Gitee主页加我QQ，给我留言即可(我是小白，不喜勿喷)\n' \
            'Gitee主页：\nhttps://gitee.com/save-a-pocket-of-stars'
        API.send(a)

    elif "点歌-哪里都是你" == message:
        API.send("[CQ:music,type=163,id=488249475]")

    elif "点歌-我的秘密" == message:
        API.send("[CQ:music,type=163,id=26117675]")

    elif "点歌-你不是真正的快乐" == message:
        API.send("[CQ:music,type=163,id=32924539]")

    elif "点歌-11" == message:
        API.send("[CQ:music,type=163,id=1907766514]")

    elif "点歌-再见" == message:
        API.send("[CQ:music,type=163,id=36024806]")

    elif "点歌-喜欢你" == message:
        API.send("[CQ:music,type=163,id=28949444]")

    elif "点歌-光年之外" == message:
        API.send("[CQ:music,type=163,id=449818741]")

    elif "点歌-倒数" == message:
        API.send("[CQ:music,type=163,id=1313107594]")

    elif "点歌-寂寞烟火" == message:
        API.send("[CQ:music,type=163,id=1984060648]")

    elif "点歌-我们的歌" == message:
        API.send("[CQ:music,type=163,id=2025533834]")

    elif "点歌-我记得" == message:
        API.send("[CQ:music,type=163,id=1974443814]")

    elif "点歌-山楂树之恋" == message:
        API.send("[CQ:music,type=163,id=1381755293]")

    elif "点歌-在你的身边" == message:
        API.send("[CQ:music,type=163,id=475479888]")

    elif "点歌-特别的人" == message:
        API.send("[CQ:music,type=163,id=28403111]")

    elif "点歌-意外" == message:
        API.send("[CQ:music,type=163,id=27890306]")

    elif "看小姐姐" == message:
        API.send("[CQ:image,file=,type=show,id=40004]")

    elif "讲一个笑话" == message:
        url = 'https://zj.v.api.aa1.cn/api/wenan-gaoxiao/?type=json'
        funny = requests.get(url)
        funny_text = json.loads(funny.text)
        joke = funny_text['msg']
        API.send('[' + joke + ']')

    elif "查询时间" == message:
        url = 'https://v.api.aa1.cn/api/time-tx/index.php'
        response = requests.get(url)
        time = json.loads(response.text)
        timee = time['nowtime']
        API.send('当前时间为：\n' + '[' + timee + ']' + '[CQ:face,id=176][CQ:face,id=176][CQ:face,id=176]')

    elif "今天天气如何" == message:
        url = 'https://v.api.aa1.cn/api/api-tianqi-4/?id=101271101'
        response = requests.get(url)
        weather = json.loads(response.text)
        city = weather['city']  # 查询地址
        temp = weather['temp']  # 温度
        wind_direction = weather['wd']  # 风向
        wdforce = weather['wdforce']  # 风力
        wdspd = weather['wdspd']  # 风速
        humidity = weather['humidity']  # 湿度
        stp = weather['stp']  # 压力
        wether = weather['wether']  # 天气情况
        today = weather['today']  # 日期
        API.send('今天天气如下：\n'
                 '查询地址：' + city + '\n'
                 '日期:' + today + '\n'
                 '天气情况:' + wether + '\n'
                 '温度:' + temp + ' ℃\n'
                 '风向:' + wind_direction + '\n'
                 '风力:' + wdforce + '\n'
                 '风速:' + wdspd + '\n'
                 '湿度:' + humidity + '\n'
                 '压力:' + stp + 'mm' + '\n'
                 )
        if wether == '晴':
            API.send('今天是晴天哦，出门做好防嗮哦！' + '[CQ:face,id=13][CQ:face,id=13]')
        elif wether == '多云':
            API.send('')
        elif wether == '少云':
            API.send('小雨，阵雨，中雨，大雨，暴雨，雷阵雨')
        elif wether == '阴':
            API.send('阴天，已经成为一种纪念，那个寂寞的好孩子，再也不会蹲在地上傻傻的看天了。' + '[CQ:face,id=179][CQ:face,id=179]')
        elif wether == '雾':
            API.send('今天是雾霾天气哦，请减少外出，乖乖待在家里。' + '[CQ:face,id=212][CQ:face,id=212]')
        elif wether == '小雨':
            API.send('出门记得带伞哦！' + '[CQ:face,id=176][CQ:face,id=176]')
    elif "舔狗日记" == message:
        url = 'https://v.api.aa1.cn/api/tiangou/index.php'
        response = requests.get(url)
        flatterer_text = response.text
        flatterer = re.findall('<p>(.*?)</p>', flatterer_text, re.S)[0]
        API.send('[' + flatterer + ']')

    elif "每日一言" == message:
        url = 'https://v.api.aa1.cn/api/yiyan/index.php'
        response = requests.get(url)
        everyday_text = response.text
        everyday = re.findall('<p>(.*?)</p>', everyday_text, re.S)[0]
        API.send('[' + everyday + ']' + '[CQ:face,id=176][CQ:face,id=176]')

    elif "随机音乐" == message:
        url = 'https://api.wqwlkj.cn/wqwlapi/wyy_random.php?type=json'
        netease = requests.get(url)
        netease_wyy = json.loads(netease.text)
        text = netease_wyy['data']
        netease_id = text['id']
        API.send(API.send('[CQ:music,type=163,id={}]'.format(netease_id)))

    elif "安慰文案" == message:
        url = 'https://v.api.aa1.cn/api/api-wenan-anwei/index.php?type=json'
        comfort = requests.get(url)
        comfort_text = json.loads(comfort.text)
        anwei = comfort_text['anwei']
        API.send('[' + anwei + ']')

    else:
        print('无关紧要的消息')
    return "OK"
