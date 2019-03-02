from urllib import request, parse
import json
# import chardet

"""
urllib.request
urllib.Request
"""

if __name__ == "__main__":

    # url = "https://www.baidu.com/s?word="
    trans_url = "https://fanyi.baidu.com/sug"
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

    req = request.Request(trans_url, data=ts, headers=headers)

    rsp = request.urlopen(req)

    result = rsp.read()
    print(type(rsp))
    rsp_head = rsp.headers
    result = json.loads(result)

    # print(result)
    print(type(rsp_head))
    print(rsp_head)

    if 0 == result["errno"]:
        for v in result["data"]:
            print(v["k"], " === ", v["v"])
    else:
        print("errors???")
        print(result)

