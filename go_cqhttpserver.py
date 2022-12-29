import os
import json
import time
try:
    from flask import Flask, redirect, url_for, request, render_template
    print('flask导入成功')
except:
    os.system('pip3 install flask')
    from flask import Flask, redirect, url_for, request, render_template
    print('flask导入成功')
try:
    from multiprocessing import Process     # 导入模块
    print('multiprocessing导入成功')
except:
    os.system('pip3 install multiprocessing')
    from multiprocessing import Process     # 导入模块
    print('multiprocessing导入成功')

class apiserver:
    main_f = 'a.main()'
    communication_f = 'a.communication()'
    c_port = 8980  #端口
    c_listen = 100  #最大连接数
    data = '' #收到的消息
    c_state = 0  #socket开启状态
    def __init__(self):
        print('版本:1.0.2')
    def main(self):
        #print(json.dumps (self.data))
        pass
    def communication(self):
        if (self.c_state == 0):
            self.c_state += 1
            import socket
            self.sk = socket.socket()
            self.sk.bind(('127.0.0.1', 8980))
            self.sk.listen(self.c_listen)
            self.conn, self.addr = self.sk.accept()
            # try:
            self.conn.send(str(self.data).encode("utf-8"))
            # except:
            #     time.sleep(1)
            #     conn.send('aaaaa'.encode("utf-8"))
        else:
            self.conn.send(str(self.data).encode("utf-8"))
            # except:
            #     print('发送失败:没有客户端连接')
            #     conn.send('aaaaa'.encode("utf-8"))
        # 关闭客户端链接
        #conn.close()
        # 关闭服务器套接字
        #sk.close()    
    def go(self):
        self.app = Flask(__name__)
        self.app.add_url_rule('/', '', self.post_data,methods=["POST"])
        self.app.run(debug = True,port=5000)
    def post_data(self):
        self.data = request.get_json()
        exec(self.communication_f)
        exec(self.main_f)
        return 'OK'
a = apiserver()
a.go()
