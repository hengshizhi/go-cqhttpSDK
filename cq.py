import json
cq = '[CQ:at,qq=123,name=不在群的QQ]' #示例信息
class cqc:
    def CqToJson(self,cq):  #解析CQ码
        '''函数文档
        作用：将CQ码解析为python对象
        输入示例：'[CQ:at,qq=123,name=不在群的QQ]'
        输出示例：'{"type": "at", "data": {"qq": "123", "name": "\u4e0d\u5728\u7fa4\u7684QQ"}}'
        '''
        cq = cq.replace('[','').replace(']','')
        cq = cq.split(',')
        data = {}
        for i in range(len(cq)-1):
            data['lin'] = cq[i+1].split('=')
            data[data['lin'][0]] = data['lin'][1]
        del data['lin']
        cqs = {}
        cqs['type'] = cq[0].replace('CQ:','')
        cqs['data'] = data
        return json.dumps (cqs)
    def JsonToCq(self,Json): #将python对象或者json转换为CQ码
        dic = json.loads (Json)
        cqdata = 'CQ:'+dic['type']
        for k,v in dic['data'].items():
            cqdata += ','+k+'='+str(v)
        return '['+cqdata+']'
    def face(self,id):
        '''
{
    "type": "face",
    "data": {
        "id": "123"
    }
}
[CQ:face,id=123]
        '''
        dic = {}
        dic['data'] = {}
        dic['type'] = 'face'
        dic['data']['id'] = id
        print(json.dumps(dic))
        return self.JsonToCq(json.dumps(dic))
    def QQ表情(self,id=0):
        '''
{
    "type": "face",
    "data": {
        "id": "123"
    }
}
[CQ:face,id=123]

        '''
        dic = {}
        dic['data'] = {}
        dic['type'] = 'face'

        if(id == 0):
            pass
        else:
            dic['data']['id'] = id

        print(json.dumps(dic))
        return self.JsonToCq(json.dumps(dic))

    def 语音(self,file=0,magic=0,url=0,cache=0,proxy=0,timeout=0):       
        '''
{
    "type": "record",
    "data": {
        "file": "http://baidu.com/1.mp3"
    }
}
[CQ:record,file=http://baidu.com/1.mp3]

        '''
        dic = {}
        dic['data'] = {}
        dic['type'] = 'record'

        if(file == 0):
            pass
        else:
            dic['data']['file'] = file

        if(magic == 0):
            pass
        else:
            dic['data']['magic'] = magic

        if(url == 0):
            pass
        else:
            dic['data']['url'] = url

        if(cache == 0):
            pass
        else:
            dic['data']['cache'] = cache

        if(proxy == 0):
            pass
        else:
            dic['data']['proxy'] = proxy

        if(timeout == 0):
            pass
        else:
            dic['data']['timeout'] = timeout

        print(json.dumps(dic))
        return self.JsonToCq(json.dumps(dic))

    def 短视频(self,file=0,cover=0,c=0):
        '''
{
    "type": "video",
    "data": {
        "file": "http://baidu.com/1.mp4"
    }
}
[CQ:video,file=http://baidu.com/1.mp4]

        '''
        dic = {}
        dic['data'] = {}
        dic['type'] = 'video'

        if(file == 0):
            pass
        else:
            dic['data']['file'] = file

        if(cover == 0):
            pass
        else:
            dic['data']['cover'] = cover

        if(c == 0):
            pass
        else:
            dic['data']['c'] = c

        print(json.dumps(dic))
        return self.JsonToCq(json.dumps(dic))

    def 某人(self,qq=0,name=0):
        '''
{
    "type": "at",
    "data": {
        "qq": "10001000",
        "name": "此栏无效，此人在群里"
    }
}
[CQ:at,qq=10001000]
[CQ:at,qq=123,name=不在群的QQ]
[CQ:at,qq=all]

        '''
        dic = {}
        dic['data'] = {}
        dic['type'] = 'at'

        if(qq == 0):
            pass
        else:
            dic['data']['qq'] = qq

        if(name == 0):
            pass
        else:
            dic['data']['name'] = name

        print(json.dumps(dic))
        return self.JsonToCq(json.dumps(dic))

    def 猜拳魔法表情(self):
        '''
{
    "type": "rps",
    "data": {}
}
[CQ:rps]

        '''
        dic = {}
        dic['data'] = {}
        dic['type'] = 'rps'

        print(json.dumps(dic))
        return self.JsonToCq(json.dumps(dic))

    def 掷骰子魔法表情(self):
        '''
{
    "type": "dice",
    "data": {}
}
[CQ:dice]

        '''
        dic = {}
        dic['data'] = {}
        dic['type'] = 'dice'

        print(json.dumps(dic))
        return self.JsonToCq(json.dumps(dic))

    def 窗口抖动戳一戳发(self):
        '''
{
    "type": "shake",
    "data": {}
}
[CQ:shake]

        '''
        dic = {}
        dic['data'] = {}
        dic['type'] = 'shake'

        print(json.dumps(dic))
        return self.JsonToCq(json.dumps(dic))

    def 匿名发消息发(self,ignore=0):
        '''
{
    "type": "anonymous",
    "data": {}
}
[CQ:anonymous]

        '''
        dic = {}
        dic['data'] = {}
        dic['type'] = 'anonymous'

        if(ignore == 0):
            pass
        else:
            dic['data']['ignore'] = ignore

        print(json.dumps(dic))
        return self.JsonToCq(json.dumps(dic))

    def 链接分享(self,url=0,title=0,content=0,image=0):
        '''
{
    "type": "share",
    "data": {
        "url": "http://baidu.com",
        "title": "百度"
    }
}
[CQ:share,url=http://baidu.com,title=百度]

        '''
        dic = {}
        dic['data'] = {}
        dic['type'] = 'share'

        if(url == 0):
            pass
        else:
            dic['data']['url'] = url

        if(title == 0):
            pass
        else:
            dic['data']['title'] = title

        if(content == 0):
            pass
        else:
            dic['data']['content'] = content

        if(image == 0):
            pass
        else:
            dic['data']['image'] = image

        print(json.dumps(dic))
        return self.JsonToCq(json.dumps(dic))

    def 推荐好友群(self,type=0,id=0):
        '''
[CQ:contact,type=qq,id=10001000]
[CQ:contact,type=group,id=100100]

        '''
        dic = {}
        dic['data'] = {}
        dic['type'] = 'contact'

        if(type == 0):
            pass
        else:
            dic['data']['type'] = type

        if(id == 0):
            pass
        else:
            dic['data']['id'] = id

        print(json.dumps(dic))
        return self.JsonToCq(json.dumps(dic))

    def 位置(self,lat=0,lon=0,title=0,content=0):
        '''
{
    "type": "location",
    "data": {
        "lat": "39.8969426",
        "lon": "116.3109099"
    }
}
[CQ:location,lat=39.8969426,lon=116.3109099]

        '''
        dic = {}
        dic['data'] = {}
        dic['type'] = 'location'

        if(lat == 0):
            pass
        else:
            dic['data']['lat'] = lat

        if(lon == 0):
            pass
        else:
            dic['data']['lon'] = lon

        if(title == 0):
            pass
        else:
            dic['data']['title'] = title

        if(content == 0):
            pass
        else:
            dic['data']['content'] = content

        print(json.dumps(dic))
        return self.JsonToCq(json.dumps(dic))

    def 音乐分享发(self,type=0,id=0):
        '''
{
    "type": "music",
    "data": {
        "type": "163",
        "id": "28949129"
    }
}
[CQ:music,type=163,id=28949129]

        '''
        dic = {}
        dic['data'] = {}
        dic['type'] = 'music'

        if(type == 0):
            pass
        else:
            dic['data']['type'] = type

        if(id == 0):
            pass
        else:
            dic['data']['id'] = id

        print(json.dumps(dic))
        return self.JsonToCq(json.dumps(dic))

    def 音乐自定义分享发(self,type=0,url=0,audio=0,title=0,content=0,image=0):
        '''
{
    "type": "music",
    "data": {
        "type": "custom",
        "url": "http://baidu.com",
        "audio": "http://baidu.com/1.mp3",
        "title": "音乐标题"
    }
}
[CQ:music,type=custom,url=http://baidu.com,audio=http://baidu.com/1.mp3,title=音乐标题]

        '''
        dic = {}
        dic['data'] = {}
        dic['type'] = 'music'

        if(type == 0):
            pass
        else:
            dic['data']['type'] = type

        if(url == 0):
            pass
        else:
            dic['data']['url'] = url

        if(audio == 0):
            pass
        else:
            dic['data']['audio'] = audio

        if(title == 0):
            pass
        else:
            dic['data']['title'] = title

        if(content == 0):
            pass
        else:
            dic['data']['content'] = content

        if(image == 0):
            pass
        else:
            dic['data']['image'] = image

        print(json.dumps(dic))
        return self.JsonToCq(json.dumps(dic))

    def 图片(self,file=0,type=0,subType=0,url=0,cache=0,id=0,c=0):       
        '''

        '''
        dic = {}
        dic['data'] = {}
        dic['type'] = 'image'

        if(file == 0):
            pass
        else:
            dic['data']['file'] = file

        if(type == 0):
            pass
        else:
            dic['data']['type'] = type

        if(subType == 0):
            pass
        else:
            dic['data']['subType'] = subType

        if(url == 0):
            pass
        else:
            dic['data']['url'] = url

        if(cache == 0):
            pass
        else:
            dic['data']['cache'] = cache

        if(id == 0):
            pass
        else:
            dic['data']['id'] = id

        if(c == 0):
            pass
        else:
            dic['data']['c'] = c

        print(json.dumps(dic))
        return self.JsonToCq(json.dumps(dic))

    def 回复(self,id=0,text=0,qq=0,time=0,seq=0):
        '''

        '''
        dic = {}
        dic['data'] = {}
        dic['type'] = 'reply'

        if(id == 0):
            pass
        else:
            dic['data']['id'] = id

        if(text == 0):
            pass
        else:
            dic['data']['text'] = text

        if(qq == 0):
            pass
        else:
            dic['data']['qq'] = qq

        if(time == 0):
            pass
        else:
            dic['data']['time'] = time

        if(seq == 0):
            pass
        else:
            dic['data']['seq'] = seq

        print(json.dumps(dic))
        return self.JsonToCq(json.dumps(dic))

    def 红包收(self,title=0):
        '''

        '''
        dic = {}
        dic['data'] = {}
        dic['type'] = 'redbag'

        if(title == 0):
            pass
        else:
            dic['data']['title'] = title

        print(json.dumps(dic))
        return self.JsonToCq(json.dumps(dic))

    def 戳一戳发(self,qq=0):
        '''

        '''
        dic = {}
        dic['data'] = {}
        dic['type'] = 'message id 恒定为 '

        if(qq == 0):
            pass
        else:
            dic['data']['qq'] = qq

        print(json.dumps(dic))
        return self.JsonToCq(json.dumps(dic))

    def 礼物发(self,qq=0,id=0):
        '''

        '''
        dic = {}
        dic['data'] = {}
        dic['type'] = 'message id 恒定为 '

        if(qq == 0):
            pass
        else:
            dic['data']['qq'] = qq

        if(id == 0):
            pass
        else:
            dic['data']['id'] = id

        print(json.dumps(dic))
        return self.JsonToCq(json.dumps(dic))

    def 合并转发收(self,id=0):
        '''

        '''
        dic = {}
        dic['data'] = {}
        dic['type'] = 'forward'

        if(id == 0):
            pass
        else:
            dic['data']['id'] = id

        print(json.dumps(dic))
        return self.JsonToCq(json.dumps(dic))

    def 合并转发消息节点发(self,id=0,name=0,uin=0,content=0,seq=0):      
        '''
[
        {
                "type": "node",
                "data": {
                        "id": "123"
                }
        },
        {
                "type": "node",
                "data": {
                        "id": "456"
                }
        }
]
[
        {
                "type": "node",
                "data": {
                        "name": "消息发送者A",
                        "uin": "10086",
                        "content": [
                                {
                                        "type": "text",
                                        "data": {
                                                "text": "测试消息1"      
                                        }
                                }
                        ]
                }
        },
        {
                "type": "node",
                "data": {
                        "name": "消息发送者B",
                        "uin": "10087",
                        "content": "[CQ:image,file=xxxxx]测试消息2"      
                }
        }
]
[
    {
        "type": "node",
        "data": {
            "name": "自定义发送者",
            "uin": "10086",
            "content": "我是自定义消息",
            "seq": "5123",
            "time": "3376656000"
        }
    },
    {
        "type": "node",
        "data": {
            "id": "123"
        }
    }
]

        '''
        dic = {}
        dic['data'] = {}
        dic['type'] = 'node'

        if(id == 0):
            pass
        else:
            dic['data']['id'] = id

        if(name == 0):
            pass
        else:
            dic['data']['name'] = name

        if(uin == 0):
            pass
        else:
            dic['data']['uin'] = uin

        if(content == 0):
            pass
        else:
            dic['data']['content'] = content

        if(seq == 0):
            pass
        else:
            dic['data']['seq'] = seq

        print(json.dumps(dic))
        return self.JsonToCq(json.dumps(dic))

    def XML消息(self,data=0,resid=0):
        '''
<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><msg serviceID="2" templateID="1" action="web" brief="&#91;分享&#93; 十年" sourceMsgId="0" url="https://i.y.qq.com/v8/playsong.html?_wv=1&amp;songid=4830342&amp;souce=qqshare&amp;source=qqshare&amp;ADTAG=qqshare" flag="0" adverSign="0" 
multiMsgFlag="0" ><item layout="2"><audio cover="http://imgcache.qq.com/music/photo/album_500/26/500_albumpic_89526_0.jpg" src="http://ws.stream.qqmusic.qq.com/C400003mAan70zUy5O.m4a?guid=1535153710&amp;vkey=D5315B8C0603653592AD4879A8A3742177F59D582A7A86546E24DD7F282C3ACF81526C76E293E57EA1E42CF19881C561275D919233333ADE&amp;uin=&amp;fromtag=3" /><title>十年</title><summary>陈奕迅</summary></item><source name="QQ音乐" icon="https://i.gtimg.cn/open/app_icon/01/07/98/56/1101079856_100_m.png" url="http://web.p.qq.com/qqmpmobile/aio/app.html?id=1101079856" action="app"  a_actionData="com.tencent.qqmusic" i_actionData="tencent1101079856://" appid="1101079856" /></msg>
<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><msg serviceID="2" templateID="1" action="web" brief="&#91;分享&#93; 十年" sourceMsgId="0" url="http://music.163.com/m/song/409650368" flag="0" adverSign="0" multiMsgFlag="0" ><item layout="2"><audio cover="http://p2.music.126.net/g-Qgb9ibk9Wp_0HWra0xQQ==/16636710440565853.jpg?param=90y90" src="https://music.163.com/song/media/outer/url?id=409650368.mp3" /><title>十年</title><summary>黄梦之</summary></item><source name="网易云音乐" icon="https://pic.rmb.bdstatic.com/911423bee2bef937975b29b265d737b3.png" url="http://web.p.qq.com/qqmpmobile/aio/app.html?id=1101079856" action="app" a_actionData="com.netease.cloudmusic" i_actionData="tencent100495085://" appid="100495085" /></msg>
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<msg serviceID="1">
<item><title>生死8秒！女司机高速急刹, 他一个操作救下一车性命</title></item>
<source name="官方认证消息" icon="https://qzs.qq.com/ac/qzone_v5/client/auth_icon.png" action="" appid="-1" />
</msg>
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<msg serviceID="1">
<item layout="4">
<title>test title</title>
<picture cover="http://url.cn/5CEwIUy"/>
</item>
</msg>

        '''
        dic = {}
        dic['data'] = {}
        dic['type'] = 'xml'

        if(data == 0):
            pass
        else:
            dic['data']['data'] = data

        if(resid == 0):
            pass
        else:
            dic['data']['resid'] = resid

        print(json.dumps(dic))
        return self.JsonToCq(json.dumps(dic))

    def JSON消息(self,data=0,resid=0):
        '''
[CQ:json,data={"app":"com.tencent.miniapp"&#44;"desc":""&#44;"view":"notification"&#44;"ver":"0.0.0.1"&#44;"prompt":"&#91;应用&#93;"&#44;"appID":""&#44;"sourceName":""&#44;"actionData":""&#44;"actionData_A":""&#44;"sourceUrl":""&#44;"meta":{"notification":{"appInfo":{"appName":"全国疫情数据 
统计"&#44;"appType":4&#44;"appid":1109659848&#44;"iconUrl":"http:\/\/gchat.qpic.cn\/gchatpic_new\/719328335\/-2010394141-6383A777BEB79B70B31CE250142D740F\/0"}&#44;"data":&#91;{"title":"确诊"&#44;"value":"80932"}&#44;{"title":"今日确诊"&#44;"value":"28"}&#44;{"title":"疑似"&#44;"value":"72"}&#44;{"title":"今日疑似"&#44;"value":"5"}&#44;{"title":"治愈"&#44;"value":"60197"}&#44;{"title":"今日治愈"&#44;"value":"1513"}&#44;{"title":"死亡"&#44;"value":"3140"}&#44;{"title":"今**亡"&#44;"value":"17"}&#93;&#44;"title":"中国加油, 武汉加油"&#44;"button":&#91;{"name":"病毒 : SARS-CoV-2, 其
导致疾病命名 COVID-19"&#44;"action":""}&#44;{"name":"传染源 : 新冠肺炎的 
患者。无症状感染者也可能成为传染源。"&#44;"action":""}&#93;&#44;"emphasis_keyword":""}}&#44;"text":""&#44;"sourceAd":""}]

        '''
        dic = {}
        dic['data'] = {}
        dic['type'] = 'json'

        if(data == 0):
            pass
        else:
            dic['data']['data'] = data

        if(resid == 0):
            pass
        else:
            dic['data']['resid'] = resid

        print(json.dumps(dic))
        return self.JsonToCq(json.dumps(dic))

    def cardimage发(self,file=0,minwidth=0,minheight=0,maxwidth=0,maxheight=0,source=0,icon=0):
        '''
[CQ:cardimage,file=https://i.pixiv.cat/img-master/img/2020/03/25/00/00/08/80334602_p0_master1200.jpg]

        '''
        dic = {}
        dic['data'] = {}
        dic['type'] = 'cardimage'

        if(file == 0):
            pass
        else:
            dic['data']['file'] = file

        if(minwidth == 0):
            pass
        else:
            dic['data']['minwidth'] = minwidth

        if(minheight == 0):
            pass
        else:
            dic['data']['minheight'] = minheight

        if(maxwidth == 0):
            pass
        else:
            dic['data']['maxwidth'] = maxwidth

        if(maxheight == 0):
            pass
        else:
            dic['data']['maxheight'] = maxheight

        if(source == 0):
            pass
        else:
            dic['data']['source'] = source

        if(icon == 0):
            pass
        else:
            dic['data']['icon'] = icon

        print(json.dumps(dic))
        return self.JsonToCq(json.dumps(dic))

    def 文本转语音发(self,text=0):
        '''

        '''
        dic = {}
        dic['data'] = {}
        dic['type'] = 'tts'

        if(text == 0):
            pass
        else:
            dic['data']['text'] = text

        print(json.dumps(dic))
        return self.JsonToCq(json.dumps(dic))
cqs = cqc()
print(cqs.图片('aa.jpg',0,0,'http://aaa.aa'))