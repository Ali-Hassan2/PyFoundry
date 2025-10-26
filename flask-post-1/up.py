from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users')
def getUser():
    users = [{'name':'Ali'},{'name':'Hassan'},{'name':'Faaiz'}]
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True, port=5000)