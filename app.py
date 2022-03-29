from datetime import datetime
from xmlrpc.client import _HostType
from flask import Flask
from suds.client import Client

app = Flask("__name__")
client = Client('http://236a-193-40-12-11.ngrok.io/?wsdl', cache=None)


@app.route('/<host>')
def ping(host):
    arguments = host
    res = client.service.ping_host(arguments)
    # Transform string array into dictionary
    dict = {}
    i = 0
    for r in res:
        dict[i] = r
        i += 1
    return dict


@app.route('/showip/<host>')
def showip(host):
    arguments = host
    return client.service.res_name(arguments)
    # Transform string array into dictionary
    #dict = {}
    #i = 0
    # for r in res:
    #    dict[i] = r
    #    i += 1
    # return dict


@app.route('/dns/<host>')
def dns(host):
    arguments = host
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
