from urllib import request, parse
import json
# import chardet

"""
urllib.request
"""

if __name__ == "__main__":

    # url = "https://www.baidu.com/s?word="
    trans_url = "https://fanyi.baidu.com/sug"
    kw = input("what do you want to translate: ")

    data = {
        "kw": kw
    }
    ts = parse.urlencode(data).encode()

    response = request.urlopen(trans_url, data=ts)

    result = response.read()
    result = json.loads(result)

    if 0 == result["errno"]:
        for v in result["data"]:
            print(v["k"], " === ", v["v"])
    else:
        print("errors???")
        print(result)

