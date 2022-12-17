import requests
class sdk:
    url = "http://127.0.0.1:5700"
    def get(self,终结点,myParams):
        url = self.url+终结点  #拼接终结点
        res = requests.get(url=url, params=myParams)  #发送给API请求
        print('GET:',url)
        return(res.text)  #返回请求的内容

    ## 发送私聊消息
    def send_private_msg(self,user_id=True,group_id=True,message=True,auto_escape=True):
        myParams = {}
        myParams['user_id'] = user_id
        myParams['group_id'] = group_id
        myParams['message'] = message
        myParams['auto_escape'] = auto_escape
        ret = self.get('/send_private_msg',myParams)
        return ret
    
    def 发送私聊消息(self,user_id="对方 QQ 号",group_id="主动发起临时会话时的来源群号(可选, 机器人本身必须是管理员/群主)",message="要发送的内容",auto_escape="消息内容是否作为纯文本发送 ( 即不解析 CQ 码 ) , 只在 message 字段是字符串时有效"):
        self.send_private_msg(user_id,group_id,message,auto_escape)
    
    ## 发送群消息
    def send_group_msg(self,group_id=True,message=True,auto_escape=True):
        myParams = {}
        myParams['group_id'] = group_id
        myParams['message'] = message
        myParams['auto_escape'] = auto_escape
        ret = self.get('/send_group_msg',myParams)
        return ret
    
    def 发送群消息(self,group_id="群号",message="要发送的内容",auto_escape="消息内容是否作为纯文本发送 ( 即不解析 CQ 码 ) , 只在 message 字段是字符串时有效"):
        self.send_group_msg(group_id,message,auto_escape)
    
    ## 发送合并转发 ( 群 )
    def send_group_forward_msg(self,group_id=True,messages=True):
        myParams = {}
        myParams['group_id'] = group_id
        myParams['messages'] = messages
        ret = self.get('/send_group_forward_msg',myParams)
        return ret
    
    def 发送合并转发群(self,group_id="群号",messages="自定义转发消息, 具体看 CQcodeopen in new window"):
        self.send_group_forward_msg(group_id,messages)
    
    ## 发送消息
    def send_msg(self,message_type=True,user_id=True,group_id=True,message=True,auto_escape=True):
        myParams = {}
        myParams['message_type'] = message_type
        myParams['user_id'] = user_id
        myParams['group_id'] = group_id
        myParams['message'] = message
        myParams['auto_escape'] = auto_escape
        ret = self.get('/send_msg',myParams)
        return ret
    
    def 发送消息(self,message_type="消息类型, 支持 private、group , 分别对应私聊、群组, 如不传入, 则根据传入的 *_id 参数判断",user_id="对方 QQ 号 ( 消息类型为 private 时需要 )",group_id="群号 ( 消息类型为 group 时需要 )",message="要发送的内容",auto_escape="消息内容是否作为纯文本发送 ( 即不解析 CQ 码 ) , 只在 message 字段是字符串时有效"):
        self.send_msg(message_type,user_id,group_id,message,auto_escape)
    
    ## 撤回消息
    def delete_msg(self,message_id=True):
        myParams = {}
        myParams['message_id'] = message_id
        ret = self.get('/delete_msg',myParams)
        return ret
    
    def 撤回消息(self,message_id="消息 ID"):
        self.delete_msg(message_id)
    
    ## 获取消息
    def get_msg(self,message_id=True):
        myParams = {}
        myParams['message_id'] = message_id
        ret = self.get('/get_msg',myParams)
        return ret
    
    def 获取消息(self,message_id="消息id"):
        self.get_msg(message_id)
    
    ## 获取合并转发内容
    def get_forward_msg(self,message_id=True):
        myParams = {}
        myParams['message_id'] = message_id
        ret = self.get('/get_forward_msg',myParams)
        return ret
    
    def 获取合并转发内容(self,message_id="消息id"):
        self.get_forward_msg(message_id)
    
    ## 获取图片信息
    def get_image(self,file=True):
        myParams = {}
        myParams['file'] = file
        ret = self.get('/get_image',myParams)
        return ret
    
    def 获取图片信息(self,file="图片缓存文件名"):
        self.get_image(file)
    
    ## 标记消息已读
    def mark_msg_as_read(self,message_id=True):
        myParams = {}
        myParams['message_id'] = message_id
        ret = self.get('/mark_msg_as_read',myParams)
        return ret
    
    def 标记消息已读(self,message_id="消息id"):
        self.mark_msg_as_read(message_id)
    
    ## 群组踢人
    def set_group_kick(self,group_id=True,user_id=True,reject_add_request=True):
        myParams = {}
        myParams['group_id'] = group_id
        myParams['user_id'] = user_id
        myParams['reject_add_request'] = reject_add_request
        ret = self.get('/set_group_kick',myParams)
        return ret
    
    def 群组踢人(self,group_id="群号",user_id="要踢的 QQ 号",reject_add_request="拒绝此人的加群请求"):
        self.set_group_kick(group_id,user_id,reject_add_request)
    
    ## 群组单人禁言
    def set_group_ban(self,group_id=True,user_id=True,duration=True):
        myParams = {}
        myParams['group_id'] = group_id
        myParams['user_id'] = user_id
        myParams['duration'] = duration
        ret = self.get('/set_group_ban',myParams)
        return ret
    
    def 群组单人禁言(self,group_id="群号",user_id="要禁言的 QQ 号",duration="禁言时长, 单位秒, 0 表示取消禁言"):
        self.set_group_ban(group_id,user_id,duration)
    
    ## 群组匿名用户禁言
    def set_group_anonymous_ban(self,group_id=True,anonymous=True,anonymous_flag=True,duration=True):
        myParams = {}
        myParams['group_id'] = group_id
        myParams['anonymous'] = anonymous
        myParams['anonymous_flag'] = anonymous_flag
        myParams['duration'] = duration
        ret = self.get('/set_group_anonymous_ban',myParams)
        return ret
    
    def 群组匿名用户禁言(self,group_id="群号",anonymous="可选, 要禁言的匿名用户对象（群消息上报的 anonymous 字段）",anonymous_flag="可选, 要禁言的匿名用户的 flag（需从群消息上报的数据中获得）",duration="禁言时长, 单位秒, 无法取消匿名用户禁言"):
        self.set_group_anonymous_ban(group_id,anonymous,anonymous_flag,duration)
    
    ## 群组全员禁言
    def set_group_whole_ban(self,group_id=True,enable=True):
        myParams = {}
        myParams['group_id'] = group_id
        myParams['enable'] = enable
        ret = self.get('/set_group_whole_ban',myParams)
        return ret
    
    def 群组全员禁言(self,group_id="群号",enable="是否禁言"):
        self.set_group_whole_ban(group_id,enable)
    
    ## 群组设置管理员
    def set_group_admin(self,group_id=True,user_id=True,enable=True):
        myParams = {}
        myParams['group_id'] = group_id
        myParams['user_id'] = user_id
        myParams['enable'] = enable
        ret = self.get('/set_group_admin',myParams)
        return ret
    
    def 群组设置管理员(self,group_id="群号",user_id="要设置管理员的 QQ 号",enable="true 为设置, false 为取消"):
        self.set_group_admin(group_id,user_id,enable)
    
    ## 群组匿名
    def set_group_anonymous(self,group_id=True,enable=True):
        myParams = {}
        myParams['group_id'] = group_id
        myParams['enable'] = enable
        ret = self.get('/set_group_anonymous',myParams)
        return ret
    
    def 群组匿名(self,group_id="群号",enable="是否允许匿名聊天"):
        self.set_group_anonymous(group_id,enable)
    
    ## 设置群名片 ( 群备注 )
    def set_group_card(self,group_id=True,user_id=True,card=True):
        myParams = {}
        myParams['group_id'] = group_id
        myParams['user_id'] = user_id
        myParams['card'] = card
        ret = self.get('/set_group_card',myParams)
        return ret
    
    def 设置群名片群备注(self,group_id="群号",user_id="要设置的 QQ 号",card="群名片内容, 不填空字符串表示删除群名片"):
        self.set_group_card(group_id,user_id,card)
    
    ## 设置群名
    def set_group_name(self,group_id=True,group_name=True):
        myParams = {}
        myParams['group_id'] = group_id
        myParams['group_name'] = group_name
        ret = self.get('/set_group_name',myParams)
        return ret
    
    def 设置群名(self,group_id="群号",group_name="新群名"):
        self.set_group_name(group_id,group_name)
    
    ## 退出群组
    def set_group_leave(self,group_id=True,is_dismiss=True):
        myParams = {}
        myParams['group_id'] = group_id
        myParams['is_dismiss'] = is_dismiss
        ret = self.get('/set_group_leave',myParams)
        return ret
    
    def 退出群组(self,group_id="群号",is_dismiss="是否解散, 如果登录号是群主, 则仅在此项为 true 时能够解散"):
        self.set_group_leave(group_id,is_dismiss)
    
    ## 设置群组专属头衔
    def set_group_special_title(self,group_id=True,user_id=True,special_title=True,duration=True):
        myParams = {}
        myParams['group_id'] = group_id
        myParams['user_id'] = user_id
        myParams['special_title'] = special_title
        myParams['duration'] = duration
        ret = self.get('/set_group_special_title',myParams)
        return ret
    
    def 设置群组专属头衔(self,group_id="群号",user_id="要设置的 QQ 号",special_title="专属头衔, 不填空字符串表示删除专属头衔",duration="专属头衔有效期, 单位秒, -1 表示永久, 不过此项似乎没有效果, 可能是只有某些特殊的时间长度有效, 有待测试"):
        self.set_group_special_title(group_id,user_id,special_title,duration)
    
    ## 群打卡
    def send_group_sign(self):
        myParams = {}
        ret = self.get('/send_group_sign',myParams)
        return ret
    
    def 群打卡(self):
        self.send_group_sign()
    
    ## 处理加好友请求
    def set_friend_add_request(self,flag=True,approve=True,remark=True):
        myParams = {}
        myParams['flag'] = flag
        myParams['approve'] = approve
        myParams['remark'] = remark
        ret = self.get('/set_friend_add_request',myParams)
        return ret
    
    def 处理加好友请求(self,flag="加好友请求的 flag（需从上报的数据中获得）",approve="是否同意请求",remark="添加后的好友备注（仅在同意时有效）"):
        self.set_friend_add_request(flag,approve,remark)
    
    ## 处理加群请求／邀请
    def set_group_add_request(self,flag=True,sub_type=True,approve=True,reason=True):
        myParams = {}
        myParams['flag'] = flag
        myParams['sub_type'] = sub_type
        myParams['approve'] = approve
        myParams['reason'] = reason
        ret = self.get('/set_group_add_request',myParams)
        return ret
    
    def 处理加群请求邀请(self,flag="加群请求的 flag（需从上报的数据中获得）",sub_type="add  invite, 请求类型（需要和上报消息中的 sub_type 字段相符）",approve="是否同意请求／邀请",reason="拒绝理由（仅在拒绝时有效）"):
        self.set_group_add_request(flag,sub_type,approve,reason)
    
    ## 获取登录号信息
    def get_login_info(self):
        myParams = {}
        ret = self.get('/get_login_info',myParams)
        return ret
    
    def 获取登录号信息(self):
        self.get_login_info()
    
    ## 设置登录号资料
    def set_qq_profile(self):
        myParams = {}
        ret = self.get('/set_qq_profile',myParams)
        return ret
    
    def 设置登录号资料(self):
        self.set_qq_profile()
    
    ## 获取陌生人信息
    def get_stranger_info(self,user_id=True,no_cache=True):
        myParams = {}
        myParams['user_id'] = user_id
        myParams['no_cache'] = no_cache
        ret = self.get('/get_stranger_info',myParams)
        return ret
    
    def 获取陌生人信息(self,user_id="QQ 号",no_cache="是否不使用缓存（使用缓存可能更新不及时, 但响应更快）"):
        self.get_stranger_info(user_id,no_cache)
    
    ## 获取好友列表
    def get_friend_list(self):
        myParams = {}
        ret = self.get('/get_friend_list',myParams)
        return ret
    
    def 获取好友列表(self):
        self.get_friend_list()
    
    ## 获取单向好友列表
    def get_unidirectional_friend_list(self):
        myParams = {}
        ret = self.get('/get_unidirectional_friend_list',myParams)
        return ret
    
    def 获取单向好友列表(self):
        self.get_unidirectional_friend_list()
    
    ## 删除好友
    def delete_friend(self,user_id=True):
        myParams = {}
        myParams['user_id'] = user_id
        ret = self.get('/delete_friend',myParams)
        return ret
    
    def 删除好友(self,user_id="好友 QQ 号"):
        self.delete_friend(user_id)
    
    ## 获取群信息
    def get_group_info(self,group_id=True,no_cache=True):
        myParams = {}
        myParams['group_id'] = group_id
        myParams['no_cache'] = no_cache
        ret = self.get('/get_group_info',myParams)
        return ret
    
    def 获取群信息(self,group_id="群号",no_cache="是否不使用缓存（使用缓存可能更新不及时, 但响应更快）"):
        self.get_group_info(group_id,no_cache)
    
    ## 获取群列表
    def get_group_list(self):
        myParams = {}
        ret = self.get('/get_group_list',myParams)
        return ret
    
    def 获取群列表(self):
        self.get_group_list()
    
    ## 获取群成员信息
    def get_group_member_info(self,group_id=True,user_id=True,no_cache=True):
        myParams = {}
        myParams['group_id'] = group_id
        myParams['user_id'] = user_id
        myParams['no_cache'] = no_cache
        ret = self.get('/get_group_member_info',myParams)
        return ret
    
    def 获取群成员信息(self,group_id="群号",user_id="QQ 号",no_cache="是否不使用缓存（使用缓存可能更新不及时, 但响应更快）"):
        self.get_group_member_info(group_id,user_id,no_cache)
    
    ## 获取群成员列表
    def get_group_member_list(self,group_id=True,no_cache=True):
        myParams = {}
        myParams['group_id'] = group_id
        myParams['no_cache'] = no_cache
        ret = self.get('/get_group_member_list',myParams)
        return ret
    
    def 获取群成员列表(self,group_id="群号",no_cache="是否不使用缓存（使用缓存可能更新不及时, 但响应更快）"):
        self.get_group_member_list(group_id,no_cache)
    
    ## 获取群荣誉信息
    def get_group_honor_info(self,group_id=True,type=True):
        myParams = {}
        myParams['group_id'] = group_id
        myParams['type'] = type
        ret = self.get('/get_group_honor_info',myParams)
        return ret
    
    def 获取群荣誉信息(self,group_id="群号",type="要获取的群荣誉类型, 可传入 talkative performer legend strong_newbie emotion 以分别获取单个类型的群荣誉数据, 传入 all 获取所有数据"):
        self.get_group_honor_info(group_id,type)
    
    ## 获取 Cookies
    def get_cookies(self,domain=True):
        myParams = {}
        myParams['domain'] = domain
        ret = self.get('/get_cookies',myParams)
        return ret
    
    def 获取Cookies(self,domain="需要获取 cookies 的域名"):
        self.get_cookies(domain)
    
    ## 获取 CSRF Token
    def get_csrf_token(self):
        myParams = {}
        ret = self.get('/get_csrf_token',myParams)
        return ret
    
    def 获取CSRFToken(self):
        self.get_csrf_token()
    
    ## 获取 QQ 相关接口凭证
    def get_credentials(self,domain=True):
        myParams = {}
        myParams['domain'] = domain
        ret = self.get('/get_credentials',myParams)
        return ret
    
    def 获取QQ相关接口凭证(self,domain="需要获取 cookies 的域名"):
        self.get_credentials(domain)
    
    ## 获取语音
    def get_record(self,file=True,out_format=True):
        myParams = {}
        myParams['file'] = file
        myParams['out_format'] = out_format
        ret = self.get('/get_record',myParams)
        return ret
    
    def 获取语音(self,file="收到的语音文件名（消息段的 file 参数）, 如 0B38145AA44505000B38145AA4450500.silk",out_format="要转换到的格式, 目前支持 mp3、amr、wma、m4a、spx、ogg、wav、flac"):
        self.get_record(file,out_format)
    
    ## 检查是否可以发送图片
    def can_send_image(self):
        myParams = {}
        ret = self.get('/can_send_image',myParams)
        return ret
    
    def 检查是否可以发送图片(self):
        self.can_send_image()
    
    ## 检查是否可以发送语音
    def can_send_record(self):
        myParams = {}
        ret = self.get('/can_send_record',myParams)
        return ret
    
    def 检查是否可以发送语音(self):
        self.can_send_record()
    
    ## 获取版本信息
    def get_version_info(self):
        myParams = {}
        ret = self.get('/get_version_info',myParams)
        return ret
    
    def 获取版本信息(self):
        self.get_version_info()
    
    ## 重启 go-cqhttp
    def set_restart(self,delay=True):
        myParams = {}
        myParams['delay'] = delay
        ret = self.get('/set_restart',myParams)
        return ret
    
    def 重启gocqhttp(self,delay="要延迟的毫秒数, 如果默认情况下无法重启, 可以尝试设置延迟为 2000 左右"):
        self.set_restart(delay)
    
    ## 清理缓存
    def clean_cache(self):
        myParams = {}
        ret = self.get('/clean_cache',myParams)
        return ret
    
    def 清理缓存(self):
        self.clean_cache()
    
    ## 设置群头像
    def set_group_portrait(self,group_id=True,file=True,cache=True):
        myParams = {}
        myParams['group_id'] = group_id
        myParams['file'] = file
        myParams['cache'] = cache
        ret = self.get('/set_group_portrait',myParams)
        return ret
    
    def 设置群头像(self,group_id="群号",file="图片文件名",cache="表示是否使用已缓存的文件"):
        self.set_group_portrait(group_id,file,cache)
    
    ## 获取中文分词 ( 隐藏 API )
    def get_word_slices(self,content=True):
        myParams = {}
        myParams['content'] = content
        ret = self.get('/get_word_slices',myParams)
        return ret
    
    def 获取中文分词隐藏API(self,content="内容"):
        self.get_word_slices(content)
    
    ## 图片 OCR
    def ocr_image或(self,image=True):
        myParams = {}
        myParams['image'] = image
        ret = self.get('/ocr_image或',myParams)
        return ret
    
    def 图片OCR(self,image="图片ID"):
        self.ocr_image或(image)
    
    ## 获取群系统消息
    def get_group_system_msg(self):
        myParams = {}
        ret = self.get('/get_group_system_msg',myParams)
        return ret
    
    def 获取群系统消息(self):
        self.get_group_system_msg()
    
    ## 上传私聊文件
    def upload_private_file(self,user_id=True,file=True,name=True):
        myParams = {}
        myParams['user_id'] = user_id
        myParams['file'] = file
        myParams['name'] = name
        ret = self.get('/upload_private_file',myParams)
        return ret
    
    def 上传私聊文件(self,user_id="对方 QQ 号",file="本地文件路径",name="文件名称"):
        self.upload_private_file(user_id,file,name)
    
    ## 上传群文件
    def upload_group_file(self,group_id=True,file=True,name=True,folder=True):
        myParams = {}
        myParams['group_id'] = group_id
        myParams['file'] = file
        myParams['name'] = name
        myParams['folder'] = folder
        ret = self.get('/upload_group_file',myParams)
        return ret
    
    def 上传群文件(self,group_id="群号",file="本地文件路径",name="储存名称",folder="父目录ID"):
        self.upload_group_file(group_id,file,name,folder)
    
    ## 获取群文件系统信息
    def get_group_file_system_info(self,group_id=True):
        myParams = {}
        myParams['group_id'] = group_id
        ret = self.get('/get_group_file_system_info',myParams)
        return ret
    
    def 获取群文件系统信息(self,group_id="群号"):
        self.get_group_file_system_info(group_id)
    
    ## 获取群根目录文件列表
    def get_group_root_files(self,group_id=True):
        myParams = {}
        myParams['group_id'] = group_id
        ret = self.get('/get_group_root_files',myParams)
        return ret
    
    def 获取群根目录文件列表(self,group_id="群号"):
        self.get_group_root_files(group_id)
    
    ## 获取群子目录文件列表
    def get_group_files_by_folder(self,group_id=True,folder_id=True):
        myParams = {}
        myParams['group_id'] = group_id
        myParams['folder_id'] = folder_id
        ret = self.get('/get_group_files_by_folder',myParams)
        return ret
    
    def 获取群子目录文件列表(self,group_id="群号",folder_id="文件夹ID 参考 Folder 对象"):
        self.get_group_files_by_folder(group_id,folder_id)
    
    ## 创建群文件文件夹
    def create_group_file_folder(self,group_id=True,name=True,parent_id=True):
        myParams = {}
        myParams['group_id'] = group_id
        myParams['name'] = name
        myParams['parent_id'] = parent_id
        ret = self.get('/create_group_file_folder',myParams)
        return ret
    
    def 创建群文件文件夹(self,group_id="群号",name="文件夹名称",parent_id="仅能为 /"):
        self.create_group_file_folder(group_id,name,parent_id)
    
    ## 删除群文件文件夹
    def delete_group_folder(self):
        myParams = {}
        ret = self.get('/delete_group_folder',myParams)
        return ret
    
    def 删除群文件文件夹(self):
        self.delete_group_folder()
    
    ## 删除群文件
    def delete_group_file(self,group_id=True,file_id=True,busid=True):
        myParams = {}
        myParams['group_id'] = group_id
        myParams['file_id'] = file_id
        myParams['busid'] = busid
        ret = self.get('/delete_group_file',myParams)
        return ret
    
    def 删除群文件(self,group_id="群号",file_id="文件ID 参考 File 对象",busid="文件类型 参考 File 对象"):
        self.delete_group_file(group_id,file_id,busid)
    
    ## 获取群文件资源链接
    def get_group_file_url(self,group_id=True,file_id=True,busid=True):
        myParams = {}
        myParams['group_id'] = group_id
        myParams['file_id'] = file_id
        myParams['busid'] = busid
        ret = self.get('/get_group_file_url',myParams)
        return ret
    
    def 获取群文件资源链接(self,group_id="群号",file_id="文件ID 参考 File 对象",busid="文件类型 参考 File 对象"):
        self.get_group_file_url(group_id,file_id,busid)
    
    ## 获取状态
    def get_status(self):
        myParams = {}
        ret = self.get('/get_status',myParams)
        return ret
    
    def 获取状态(self):
        self.get_status()
    
    ## 获取群 @全体成员 剩余次数
    def get_group_at_all_remain(self,group_id=True):
        myParams = {}
        myParams['group_id'] = group_id
        ret = self.get('/get_group_at_all_remain',myParams)
        return ret
    
    def 获取群全体成员剩余次数(self,group_id="群号"):
        self.get_group_at_all_remain(group_id)
    
    ## 对事件执行快速操作 ( 隐藏 API )
    def handle_quick_operation(self,context=True,operation=True):
        myParams = {}
        myParams['context'] = context
        myParams['operation'] = operation
        ret = self.get('/handle_quick_operation',myParams)
        return ret
    
    def 对事件执行快速操作隐藏API(self,context="事件数据对象, 可做精简, 如去掉 message 等无用字段",operation='''快速操作对象, 例如 {"ban": true, "reply": "请不要说脏话"}'''):
        self.handle_quick_operation(context,operation)
    
    ## 发送群公告
    def _send_group_notice(self,group_id=True,content=True,image=True):
        myParams = {}
        myParams['group_id'] = group_id
        myParams['content'] = content
        myParams['image'] = image
        ret = self.get('/_send_group_notice',myParams)
        return ret
    
    def 发送群公告(self,group_id="群号",content="公告内容",image="图片路径（可选）"):
        self._send_group_notice(group_id,content,image)
    
    ## 获取群公告
    def _get_group_notice(self,group_id=True):
        myParams = {}
        myParams['group_id'] = group_id
        ret = self.get('/_get_group_notice',myParams)
        return ret
    
    def 获取群公告(self,group_id="群号"):
        self._get_group_notice(group_id)
    
    ## 重载事件过滤器
    def reload_event_filter(self,file=True):
        myParams = {}
        myParams['file'] = file
        ret = self.get('/reload_event_filter',myParams)
        return ret
    
    def 重载事件过滤器(self,file="事件过滤器文件"):
        self.reload_event_filter(file)
    
    ## 下载文件到缓存目录
    def download_file(self,url=True,thread_count=True,headers=True):
        myParams = {}
        myParams['url'] = url
        myParams['thread_count'] = thread_count
        myParams['headers'] = headers
        ret = self.get('/download_file',myParams)
        return ret
    
    def 下载文件到缓存目录(self,url="链接地址",thread_count="下载线程数",headers="自定义请求头"):
        self.download_file(url,thread_count,headers)
    
    ## 获取当前账号在线客户端列表
    def get_online_clients(self,no_cache=True):
        myParams = {}
        myParams['no_cache'] = no_cache
        ret = self.get('/get_online_clients',myParams)
        return ret
    
    def 获取当前账号在线客户端列表(self,no_cache="是否无视缓存"):
        self.get_online_clients(no_cache)
    
    ## 获取群消息历史记录
    def get_group_msg_history(self,message_seq=True,group_id=True):
        myParams = {}
        myParams['message_seq'] = message_seq
        myParams['group_id'] = group_id
        ret = self.get('/get_group_msg_history',myParams)
        return ret
    
    def 获取群消息历史记录(self,message_seq="起始消息序号, 可通过 get_msg 获得",group_id="群号"):
        self.get_group_msg_history(message_seq,group_id)
    
    ## 设置精华消息
    def set_essence_msg(self,message_id=True):
        myParams = {}
        myParams['message_id'] = message_id
        ret = self.get('/set_essence_msg',myParams)
        return ret
    
    def 设置精华消息(self,message_id="消息ID"):
        self.set_essence_msg(message_id)
    
    ## 移出精华消息
    def delete_essence_msg(self,message_id=True):
        myParams = {}
        myParams['message_id'] = message_id
        ret = self.get('/delete_essence_msg',myParams)
        return ret
    
    def 移出精华消息(self,message_id="消息ID"):
        self.delete_essence_msg(message_id)
    
    ## 获取精华消息列表
    def get_essence_msg_list(self,group_id=True):
        myParams = {}
        myParams['group_id'] = group_id
        ret = self.get('/get_essence_msg_list',myParams)
        return ret
    
    def 获取精华消息列表(self,group_id="群号"):
        self.get_essence_msg_list(group_id)
    
    ## 检查链接安全性
    def check_url_safely(self,url=True):
        myParams = {}
        myParams['url'] = url
        ret = self.get('/check_url_safely',myParams)
        return ret
    
    def 检查链接安全性(self,url="需要检查的链接"):
        self.check_url_safely(url)
    
    ## 获取在线机型
    def _get_model_show(self,model=True):
        myParams = {}
        myParams['model'] = model
        ret = self.get('/_get_model_show',myParams)
        return ret
    
    def 获取在线机型(self,model="机型名称"):
        self._get_model_show(model)
    
    ## 设置在线机型
    def _set_model_show(self,model=True,model_show=True):
        myParams = {}
        myParams['model'] = model
        myParams['model_show'] = model_show
        ret = self.get('/_set_model_show',myParams)
        return ret
    
    def 设置在线机型(self,model="机型名称",model_show="-"):
        self._set_model_show(model,model_show)
    
    ## 删除单向好友
    def delete_unidirectional_friend(self,user_id=True):
        myParams = {}
        myParams['user_id'] = user_id
        ret = self.get('/delete_unidirectional_friend',myParams)
        return ret
    
    def 删除单向好友(self,user_id="单项好友QQ号"):
        self.delete_unidirectional_friend(user_id)
    
    ## 发送合并转发 ( 好友 )
    def send_private_forward_msg(self,user_id=True,messages=True):
        myParams = {}
        myParams['user_id'] = user_id
        myParams['messages'] = messages
        ret = self.get('/send_private_forward_msg',myParams)
        return ret
    
    def 发送合并转发好友(self,user_id="好友QQ号",messages="自定义转发消息, 具体看 CQcodeopen in new window"):
        self.send_private_forward_msg(user_id,messages)
