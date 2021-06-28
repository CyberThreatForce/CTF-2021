from flask import Flask, request, render_template
import platform
import os
global secret

#1.1.1.1');global secret;secret=code;int('1

secret = "_"
app = Flask(__name__)
app.debug = False

def ddos(ip):
    global retour
    print("start")
    for i in ip.split("."):
        if isinstance(int(i),int):
            pass
        else:
            retour = "Hack Detected"
            return 0
    print("aaa")
    if len(ip.split(".")) > 4:
        retour = "Hack Detected"
        return 0
    if platform.system == 'Linux':
        os.system(f"ping {ip} -c 3")
        retour = "Starting Attack"
    else:
        os.system(f"ping {ip} -c 3")
        retour = "Attacking the victim"
@app.route('/',methods=['GET',"POST"])
def index():
    renvoi = ""
    global secret
    code = "CYBERTF{D0nT_D3fuSe_Th3_B0tN3t}"
    global retour
    retour = "" 
    if request.method == 'GET':
        return render_template('index.html')
    else:
        liste_attaque = ["os","sys","platform","socket","import",'exit()',"exec","eval","compile"]
        to_attack = request.form["ip"]
        print(to_attack,liste_attaque)
        for attaque in liste_attaque:
            print(attaque in to_attack)
            if attaque in to_attack:
                return render_template("index.html",var = "Hack Detected",ip="Attack Stopped due to Security Violations")
        try:
            print(f"ddos('{to_attack}')")
            exec(f"ddos('{to_attack}')")
        except Exception as e:
            return render_template("index.html",var = str(e))
        print("execution")
        if retour == "Hack Detected":
            return render_template("index.html",var = retour,ip="Attack Stopped due to Security Violations")
        renvoi = str(retour)+str(secret)
        secret = "_"
        return render_template("index.html",var = renvoi,ip=str(to_attack)+", port 80")

app.run(port=80,threaded=True,host="0.0.0.0")
