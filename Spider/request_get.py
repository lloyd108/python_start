from urllib import request
from urllib import parse
import chardet

"""
urllib.request
"""

if __name__ == "__main__":

    # url = "https://www.baidu.com/s?word="
    url = "http://www.baidu.com/s?"
    kw = input("what do you want to search: ")
    word = {
        "word": kw
    }
    qs = parse.urlencode(word)
    url = url + qs
    print(url)
    response = request.urlopen(url)

    html = response.read()

    cs = chardet.detect(html) 
    code = cs.get("encoding", "utf-8")

    html = html.decode(code)
    print(html)
    # print(type(html))