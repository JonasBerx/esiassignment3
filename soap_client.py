from suds.client import Client

client = Client('http://localhost:8090/?wsdl', cache=None)

# print(client.service.say_hello(u'Maarika', 5))
print("Running Service 1 ...")
print(client.service.ping_host('localhost:9000'))
print("Running Service 2 ...")
print(client.service.res_name('www.google.com'))
print("\nRunning Service 3 ...")
print(client.service.dns('google.com'))

# wsdl = Client('http://www.learnwebservices.com/services/hello?wsdl', cache=None)
# request = {'Name': 'Maarika'}
# print(wsdl.service.SayHello(request))
