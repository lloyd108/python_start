from urllib import request, parse, error
from http import cookiejar
import time

trans_url = ""

# proxy
proxy = {
    'http': '153.126.179.216:8080'
}
proxy_handler = request.ProxyHandler(proxy)
proxy_opener = request.build_opener(proxy_handler)
request.install_opener(proxy_opener)

# cookie
cookie = cookiejar.CookieJar()
cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()
cookie_opener = request.build_opener(cookie_handler, http_handler, https_handler)


def login():
    my_url = 'http://www.renren.com/PLogin.do'
    my_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
    }
    my_data = {
        'email': '18609514473',
        'password': 'Zfb19900218'
    }

    my_data = parse.urlencode(my_data).encode()

    try:
        print('>Starting...')
        req = request.Request(url=my_url, headers=my_headers, data=my_data)
        rsp = cookie_opener.open(req)
        result = rsp.read()
        rsp_header = rsp.headers
        con_type = rsp_header['Content-Type']
        code_set = con_type[con_type.find('charset=') + len('charset='): len(con_type)] if con_type.find('charset=') else 'utf-8'
        print(con_type)
        print(code_set)
        for item in cookie:
            print(type(item), item, sep='====')

        with open('request_AutoCookie.html',  'w', encoding=code_set) as f:
            f.write(result.decode(code_set))

    except error.HTTPError as e:
        print('HTTPError: {0}'.format(e.reason))
        print('HTTPError: {0}'.format(e))
    except error.URLError as e:
        print('URLError: {0}'.format(e.reason))
        print('URLError: {0}'.format(e))
    except Exception as e:
        print(e)


def get_home_page():
    url = 'http://safe.renren.com/security/account'
    rsp = cookie_opener.open(url)
    result = rsp.read()
    rsp_header = rsp.headers
    con_type = rsp_header['Content-Type']
    code_set = con_type[con_type.find('charset=') + len('charset='): len(con_type)] if con_type.find('charset=') else 'utf-8'

    with open('request_AutoCookieHome.html',  'w', encoding=code_set) as f:
        f.write(result.decode(code_set))    


if __name__ == '__main__':
    login()
    get_home_page()

