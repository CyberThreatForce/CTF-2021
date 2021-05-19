from flask import Flask, request, render_template, make_response
import random

global key_holder
key_holder = []

def xor(cleartext,ciphertext):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#?!&%$-_1234567890"
    liste = []
    for i in cleartext:
        liste.append(alphabet.index(i))
    liste_bin=[]
    for i in liste:
        liste_bin.append(bin(i).split("b")[1])
    cipherbin = bin(int(ciphertext)).split("b")[1]*15
    liste_res = []
    for part in liste_bin:
        res = ""
        for index in range(len(part)):
            res += str(int(part[index])^int(cipherbin[index]))
        liste_res.append(res)
    liste_dec = []
    for i in liste_res:
        liste_dec.append(int(i,2))
    enc_text = ""
    for i in liste_dec:
        enc_text += alphabet[i%44]
    return enc_text

class Key:
    def __init__(self):
        self.key = ""
        self.password = ""

    def generate(self):
        first_part = random.choice(range(100000,999999))
        second_part = random.choice(range(100000,999999))
        self.key = str(first_part)+"@"+str(second_part)
        return self.key

    def generate_password(self,key):
        digit = str(random.choice(range(100,99999)))
        digit2 = str(random.choice(range(100,99999)))
        char = random.choice(["@","#","?","!","&","%","$"])
        char2 = random.choice(["@","#","?","!","&","%","$"])
        chaine = random.choice(["W34P0n","Dd0S","ApT-403","PhiSh1nG","R@ns0Mw4r3"])
        password = "_"+char2+digit2+chaine+digit+char+"_"

        print(password)

        key1,key2 = key.split("@")[0],key.split("@")[1]
        password = xor(password,key1)
        password = xor(password,key2)
        password = password[::-1]

        return password

    def check_password(self,password,key):
        key1,key2 = key.split("@")[0],key.split("@")[1]
        password = xor(password,key1)
        password = xor(password,key2)
        password = password[::-1]

        return password

def verify_wallet_key(key):
    filter1 = lambda x:(25<=len(x)<=34)
    filter2 = lambda x:(str(x)[0]=="1")
    filters = [filter1,filter2]
    for i in filters:
        if not i(key):
            return False
    return True

global password
password = Key()

app = Flask(__name__)


@app.route('/',methods=['GET',"POST"])
def index():
    global key_holder
    if request.method == 'GET':
        key = password.generate()
        site_password = password.generate_password(key)
        print(site_password)
        key_holder.append(site_password)
        res = make_response(render_template("index.html"))
        res.set_cookie("key",key,max_age=60*60*24*365*2)
        res.set_cookie("password",site_password,max_age=60*60*24*365*2)
        return res
    elif request.method == 'POST':
        key = request.form["wallet_key"]
        entry_password = request.form["password"]
        if not verify_wallet_key(key):
            return render_template('index.html',error="Invalid Bitcoin Adress")
        cookie = request.cookies.get('key')
        site_password = request.cookies.get('password')
        print(site_password)

        if password.check_password(entry_password,cookie)==site_password:
            if entry_password in key_holder:
                return render_template('index.html',success="{FLAG}")
            else:
                return render_template('index.html',error="Password not in the db")
        else:
            return render_template('index.html',error="Invalid Password")


@app.route('/algo',methods=['GET'])
def algo():
    return render_template('algo.html')


app.run(port=80,threaded=True,host="0.0.0.0")
