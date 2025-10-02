from flask import Flask, jsonify
import random

ListRand = ['aB','Cd','ef','Gh','ij','kl','mN','Op','Qr','St','u','V','w','x','X','yZ','z','Z','1','2','3','4','5','6','7','8','9','0']
ListJoint = []
ListJoint.clear()

def genKey():
    random.shuffle(ListRand)
    for a in ListRand:
        ListJoint.append(a)
    
    return ''.join(ListJoint)
    

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Servidor de Keys funcionando!"})

@app.route('/getkey/<userid>')
def get_key(userid):
    # Exemplo: sistema fake de keys
    keys = {
        "manoel": genKey(),
        "teste": "XYZ789-KEY"
    }
    return jsonify({"key": keys.get(userid, "Nenhuma key encontrada")})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
