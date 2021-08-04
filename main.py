from flask import Flask
import subprocess
app = Flask(__name__)

@app.route('/')
def hello_world():
    out = subprocess.Popen(['cat', '/data/node-storer/file1.txt'],
               stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    host = stdout.decode("utf-8")
    msg = 'Typing Cat on '
    msgToReturn = msg + host
    return msgToReturn
