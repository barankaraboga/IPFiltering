import urllib2, urllib,cookielib
from stem import Signal
from stem.control import Controller
import socket
import socks

#configuration start
id_number=40
votes=98
#configuration end

#initialization start
default_socket = socket.socket
SOCKS5_PROXY_HOST = 'localhost'
SOCKS5_PROXY_PORT = 9050
#initialization end

def use_tor():
     socket.socket = default_socket
     controller.signal(Signal.NEWNYM)
     socks.set_default_proxy(socks.SOCKS5, SOCKS5_PROXY_HOST, SOCKS5_PROXY_PORT)
     socket.socket = socks.socksocket
     generate_vote()

         def generate_vote():
              cj = cookielib.CookieJar()
              opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
              session = opener.open('url.com')
              if session.getcode() == 200:
                  for cookie in cj:
                      if cookie.name=='session':
                          params = { 'id': id_number, 'submit': 'Submit', 'key':  cookie.value }
                      url_params = urllib.urlencode(params) # url encode the parameters
                      post=opener.open('url.com', url_params)
                      opener.close()

with Controller.from_port(port = 9051) as controller:
    controller.authenticate() #write password here if you set a password earlier
    for _ in range(votes):
        use_tor()
