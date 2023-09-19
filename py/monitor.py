from flask import Flask, request
import requests
import menu

app = Flask(__name__)


class API:
    @staticmethod
    def send(message):
        data = request.get_json()
        message_type = data['message_type']
        if 'group' == message_type:  # 判断消息类型是否为群聊类型或是否为私聊类型
            group_id = data['group_id']
            params = {
                "message_type": message_type,
                "group_id": str(group_id),
                "message": message
            }
        else:  # 消息类型为私聊类型
            user_id = data['user_id']
            params = {
                "message_type": message_type,
                "user_id": user_id,
                "message": message
            }
        url = "http://127.0.0.1:5900/send_msg"  # 发送消息的接口
        """API接口格式, 按照官方文档来进行设置"""
        requests.get(url, params=params)


@app.route('/', methods=['POST'])  # 请求方式
def post_data():
    data = request.get_json()  # request.get_json().get 用于获取关键字的值，参考上面代码段使用的数据格式
    print(data)

    if data['post_type'] == 'message':  # 消息判断和处理
        message = data['message']
        print(message)
        menu.menu()
    else:
        print('暂不处理')

    return "OK"  # 返回值


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5909)  # 此处的 host和 port对应 go-cqhttp的config.yml文件的设置
