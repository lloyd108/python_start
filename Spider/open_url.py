from urllib import request

import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

"""
urllib.request
"""

if __name__ == "__main__":

    url = "https://jobs.zhaopin.com/244888886250454.htm"
    response = request.urlopen(url)

    html = response.read()

    # print(html)
    print(type(html))

    # html1 = str(html)
    # print(html1)
    # print(type(html1))

    html2 = html.decode()
    print(html2)
    print(type(html2))