from flask import Flask, request

app = Flask(__name__)


@app.route('/api/login', methods=['post', 'get'])
def flash_01():
    data=request.get_json()
    channel=data['channel']
    print(request.get_json())
    if request.get_json()['channel'] == 'POS':
        return '传输正确'
    else:
        return '传输失败'

@app.route('/api/buy',methods=['post','get'])
def flash_02():
    data=request.get_json()
    username = data['username']
    if username== 'POS':
        return '传输正确'
    else:
        return '传输失败'



if __name__ == '__main__':
    app.run(debug=True)
