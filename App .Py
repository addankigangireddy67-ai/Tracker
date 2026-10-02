from flask import Flask

app = Flask(__name__)

@app.route("/")
def opened():
    print("[+] LINK OPENED!")
    return "<h2>Link Opened ✅</h2><p>This is only a local demo.</p>"

app.run(host="127.0.0.1", port=8080)
