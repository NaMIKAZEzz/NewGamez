from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Servidor de Keys funcionando!"})

@app.route('/getkey/<userid>')
def get_key(userid):
    # Exemplo: sistema fake de keys
    keys = {
        "manoel": "ABC123-KEY",
        "teste": "XYZ789-KEY"
    }
    return jsonify({"key": keys.get(userid, "Nenhuma key encontrada")})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
