from pydoc import resolve
from spyne import Application, rpc, ServiceBase, Iterable, Integer, Unicode

from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import os
import platform
import subprocess
import netifaces as ni
import shutil
import socket
import dns
import dns.resolver


class HelloWorldService(ServiceBase):

    @rpc(Unicode, Integer, _returns=Iterable(Unicode))
    def say_hello(ctx, name, times):
        """Docstrings for service methods appear as documentation in the wsdl.
        <b>What fun!</b>
        @param name the name to say hello to
        @param times the number of times to say hello
        @return the completed array
        """

        for i in range(times):
            yield u'Tere, %s' % name

    @rpc(Unicode, _returns=Iterable(Unicode))
    def ping_host(ctx, host):
        for i in range(5):
            response = os.system("ping -c 1 %s" % host)
            if response == 1:
                yield u'Host %s is reachable' % host
            else:
                yield u'Host %s is unreachable' % host

    @rpc(Unicode, _returns=Iterable(Unicode))
    def res_name(ctx, host):
        result = dns.resolver.query(host, 'A')
        # Can also be done using socket
        # res2 = socket.gethostbyname(host)
        for ipVal in result:
            yield u'%s has address ' % host + '%s' % ipVal.to_text()

    @rpc(Unicode, _returns=Iterable(Unicode))
    def dns(ctx, host):
        ns = dns.resolver.query(host, 'NS')
        mx = dns.resolver.query(host, 'MX')
        auth = dns.resolver.query(host, 'SOA')
        for NS in ns:
            yield u'Nameserver: %s' % NS.to_text()
        for AUTH in auth:
            yield u'Auth name-server: %s' % AUTH.to_text()
        for MX in mx:
            yield u'Mailserver: %s' % MX.to_text()


application = Application([HelloWorldService], 'spyne.examples.hello.soap',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)


if __name__ == '__main__':
    import logging

    from wsgiref.simple_server import make_server

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    logging.info("listening to http://127.0.0.1:8090")
    logging.info("wsdl is at: http://localhost:8090/?wsdl")

    server = make_server('127.0.0.1', 8090, wsgi_application)
    server.serve_forever()
