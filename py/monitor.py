from flask import Flask, request
import requests
import menu

app = Flask(__name__)


class API:
    @staticmethod
    def send(message):
        data = request.get_json()
        message_type = data['message_type']
        if 'group' == message_type:  # Determine whether the message type is a group chat type or a private chat type
            group_id = data['group_id']
            params = {
                "message_type": message_type,
                "group_id": str(group_id),
                "message": message
            }
        else:  # Message type is private chat type
            user_id = data['user_id']
            params = {
                "message_type": message_type,
                "user_id": user_id,
                "message": message
            }
        url = "http://127.0.0.1:5900/send_msg"  # Interface for sending messages
        """API interface format, set according to official documents"""
        requests.get(url, params=params)


@app.route('/', methods=['POST'])  # Request Method
def post_data():
    data = request.get_json()  # request.get_json().get Used to obtain the value of the keyword, refer to the data format used in the code snippet above
    print(data)

    if data['post_type'] == 'message':  # Message judgment and processing
        message = data['message']
        print(message)
        menu.menu()
    else:
        print('暂不处理')

    return "OK"  # return value


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5909)  # The settings of the [config. yml] file corresponding to [go cqhttp] for [host] and [port] here
