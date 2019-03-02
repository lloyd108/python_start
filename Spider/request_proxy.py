from urllib import request, parse, error
import json
# import chardet

"""
urllib.request
urllib.Request
"""

if __name__ == "__main__":

    # url = "https://www.baidu.com/s?word="
    trans_url = "https://fanyi.baidu.com/sug"
    proxy = {
        'http': '153.126.179.216:8080'
    }
    proxy_handler = request.ProxyHandler(proxy)
    proxy_opener = request.build_opener(proxy_handler)
    request.install_opener(proxy_opener)

    kw = input("what do you want to translate: ")

    data = {
        "kw": kw
    }
    ts = parse.urlencode(data).encode()

    headers = {
        'Content-length':len(ts),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
    }
    print(len(data), len(ts), sep="///")

    try:
        req = request.Request(trans_url, data=ts, headers=headers)
        rsp = request.urlopen(req)
        result = rsp.read()
        result = json.loads(result)
        rsp_header = rsp.headers
        print(rsp_header)

        if 0 == result["errno"]:
            for v in result["data"]:
                print(v["k"], " === ", v["v"])
        else:
            print("errors???")
            print(result)

    except error.HTTPError as e:
        print('HTTPError: {0}'.format(e.reason))
        print('HTTPError: {0}'.format(e))
    except error.URLError as e:
        print('URLError: {0}'.format(e.reason))
        print('URLError: {0}'.format(e))
    except Exception as e:
        print(e)

