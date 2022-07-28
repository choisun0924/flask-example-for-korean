# pip install flask
# Flask : 서버
# render_template : 쉽게 html을 return 할 수 있게 돕는 메서드 (Server Side Rendering 방식)
# jsonify : 쉽게 str을 json으로 return 할 수 있게 돕는 메서드
from flask import Flask, render_template, jsonify

# 테스트용 json파일을 열어주고 타입을 확인하면 str인 것을 알 수 있습니다.
testJson = open('for_test.json', "r+")
thisOne = testJson.read()
testJson.close()
print(thisOne)
print(type(thisOne))

# 플라스크 Class를 app으로 생성
app = Flask(__name__)

# 함수를 만들고 return 합니다.
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test')
def test():
    return f'test'

@app.route('/json_test')
def json_test():
    # str이 json으로 변경되어 return 됩니다.
    return jsonify(thisOne)

# html을 Server Side Rendering 방식 return 해줍니다
@app.route("/home")
def home():
    return render_template("test.html")


if __name__ == '__main__':
    app.run()

    # app.run 메서드는 아래와 같습니다.
    '''
    def run(
        self,
        host: t.Optional[str] = None,
        port: t.Optional[int] = None,
        debug: t.Optional[bool] = None,
        load_dotenv: bool = True,
        **options: t.Any,
    )
    '''
    # 예시
    # app.run(host='localhost', port=5001, debug=True)