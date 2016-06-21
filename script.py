import urllib2, urllib,cookielib, socket, socks
from stem import Signal
from stem.control import Controller

#configuration start
id_number=40
votes=98
#configuration end

#tor socks 5 parameters
SOCKS5_PROXY_HOST = 'localhost'
SOCKS5_PROXY_PORT = 9050
#tor socks 5 parameters end

#changes circuit upon each call and calls the generate post request function
def use_tor():
     controller.signal(Signal.NEWNYM)
     socks.set_default_proxy(socks.SOCKS5, SOCKS5_PROXY_HOST, SOCKS5_PROXY_PORT)
     socket.socket = socks.socksocket
     generate_vote()

#makes a post request
def generate_vote():
     cj = cookielib.CookieJar() #cookies will get stored in cj
     opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
     #add headers if the website checks it
     opener.addheaders=[
        ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'),
        ('Referer', 'url.com'),
     ]
     #open a session
     session = opener.open('url.com')
     if session.getcode() == 200:
          #get the value of the session cookie
          for cookie in cj:
               if cookie.name=='session':
                    params = { 'id': id_number, 'submit': 'Submit', 'key':  cookie.value }
          url_params = urllib.urlencode(params) # url encode the parameters
          post = opener.open('url.com', url_params) #make the post request
     opener.close() #close the opener

with Controller.from_port(port = 9051) as controller: #defines controller on port 9051
    controller.authenticate() #write password here if you set a password earlier
    for _ in range(votes):
        use_tor()
