from urllib import request
import chardet

"""
urllib.request
"""

if __name__ == "__main__":

    # url = "https://jobs.zhaopin.com/244888886250454.htm"
    url = "http://www.baidu.com"
    response = request.urlopen(url)

    html = response.read()

    cs = chardet.detect(html)
    print(type(cs), cs, sep="///")
    code = cs.get("encoding", "utf-8")

    html = html.decode(code)
    print(html)
    print(type(html))