from urllib import request
import chardet

"""
urllib.request
"""

if __name__ == "__main__":

    # url = "http://wwww.1111.com"
    url = "https://www.baidu.com"
    response = request.urlopen(url)
    print(type(response))
    print(response.geturl(), response.info(), response.getcode(), sep='   ====   \n');

    html = response.read()

    cs = chardet.detect(html)#
    # print(type(cs), cs, sep="///")
    code = cs.get("encoding", "utf-8")

    # html = html.decode(code)
    # print(html)
    # print(type(html))

    