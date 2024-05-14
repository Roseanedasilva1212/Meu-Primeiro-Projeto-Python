from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Olá, mundo! Este é o meu site no Flask!'

if __name__ == '__main__':
    app.run(debug=True)
