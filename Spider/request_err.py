from urllib import request, parse, error
import json
# import chardet

"""
urllib.request
urllib.Request
"""

if __name__ == "__main__":

    # url = "https://www.baidu.com/s?word="
    trans_url = "https://www.huawei.com/abb"
    # kw = input("what do you want to translate: ")
    kw = 'search'

    data = {
        "kw": kw
    }
    ts = parse.urlencode(data).encode()

    headers = {
        'Content-length':len(ts)
    }
    print(len(data), len(ts), sep="///")

    try:
        req = request.Request(trans_url, data=ts, headers=headers)
        rsp = request.urlopen(req)
        result = rsp.read()
        result = json.loads(result)

        print(result)

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
