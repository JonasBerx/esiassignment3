from datetime import datetime
from flask import Flask
from suds.client import Client

app = Flask("__name__")
client = Client('http://25f3-193-40-13-174.ngrok.io/?wsdl', cache=None)


@app.route('/')
def ping():
    arguments = 'www.google.com'
    res = client.service.ping_host(arguments)
    # Transform string array into dictionary
    dict = {}
    i = 0
    for r in res:
        dict[i] = r
        i += 1
    return dict


@app.route('/showip')
def showip():
    arguments = 'www.google.com'
    res = client.service.res_name(arguments)
    # Transform string array into dictionary
    dict = {}
    i = 0
    for r in res:
        dict[i] = r
        i += 1
    return dict


@app.route('/dns')
def dns():
    arguments = 'google.com'
    res = client.service.dns(arguments)
    # Transform string array into dictionary
    dict = {}
    i = 0
    for r in res:
        dict[i] = r
        i += 1
    return dict


if __name__ == "__main__":
    app.run(debug=True)
