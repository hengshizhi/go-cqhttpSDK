# go-cqhttpSDK
### ——依赖于go-cqhttp，需要先正确安装并运行，使用HTTP协议，使你更方便的请求go-cqhttpAPI
### 使用方法：
1. 到[go-cqhttpSDK](https://github.com/hengshizhi/go-cqhttpSDK)下载go_cqhttpsdk.py并引入
2. 实例化sdk方法 `sdk = go_cqhttpsdk.sdk`
3. 设置API的url地址 `sdk.url = 'http://127.0.0.1:5700'`
4. 开始使用
5. 例子：
import go_cqhttpsdk as sdk
sdk = sdk.sdk()
sdk.url = "http://127.0.0.1:5700"
sdk.发送私聊消息(3192145045,'','你好')
sdk.send_private_msg(3192145045,'','hello shizhi')
'''
 PS D:\Downloads\人类智慧> & C:/Users/Administrator/AppData/Local/Programs/Python/Python310/python.exe d:/Downloads/人类智慧/QQjiqir/示例.py
 GET: http://127.0.0.1:5700/send_private_msg
 GET: http://127.0.0.1:5700/send_private_msg
'''
感谢：requests，go-cqhttp，tencent
