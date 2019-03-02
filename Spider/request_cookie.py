from urllib import request, parse, error
import json
import chardet

"""
urllib.request
urllib.Request
"""

if __name__ == "__main__":

    # url = "https://www.baidu.com/s?word="
    trans_url = "https://i.taobao.com/my_taobao.htm?spm=a21bo.2017.754894437.3.5af911d9MnnPio&ad_id=&am_id=&cm_id=&pm_id=1501036000a02c5c3739"
    proxy = {
        'http': '153.126.179.216:8080'
    }
    proxy_handler = request.ProxyHandler(proxy)
    proxy_opener = request.build_opener(proxy_handler)
    request.install_opener(proxy_opener)

    # kw = input("what do you want to translate: ")

    # data = {
    #     "kw": kw
    # }
    # ts = parse.urlencode(data).encode()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
        'Cookie':'miid=31086641583683231; cna=So2dE3PfvDMCAXzgXyvqOks6; isg=BD4-RREh7pEtfj1bZUWBdvYfjFRA1wKXslQg_uhHqgF8i95lUA9SCWRpB5fiqPoR; thw=cn; enc=IQZT5MGjxmWasmpjoxHoUUJzz95SYb8Je5xHiBur3XhQ08AdZUnTI8IQiQZMeDcBT8QDLPKZ9y58v7ulLUntYw%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; um=535523100CBE37C3C463F523562B904EA3192FBB9133E076A25619259659A9222D07ACD06D005B3BCD43AD3E795C914C70F893D5E6B570181E93799BE65404F8; tracknick=siva108; _cc_=UIHiLt3xSw%3D%3D; tg=0; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; t=fe199db97a25ed517f058999f4c907f9; l=bBgf7Xc7vwNIShfoBOCahurza77OSIOYYuPzaNbMi_5CK6T663QOlPBbMF96Vs5R_TYB4RVd54p9-etkZ; cookie2=108ec22a6611b1ecbcd52861426809ff; v=0; _tb_token_=f566e333e7dee; uc1=cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&cookie21=URm48syIYB3rzvI4DJOx&cookie15=VFC%2FuZ9ayeYq2g%3D%3D&existShop=false&pas=0&cookie14=UoTZ5be2nWCZdA%3D%3D&tag=10&lng=zh_CN; skt=0907c742fc6b462f; csg=644ba511; uc3=vt3=F8dByEv0IXxhGf9dSLQ%3D&id2=UNX6w7w6sS0%3D&nk2=EFeG6RaKnw%3D%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D; existShop=MTU1MTQyODA0NA%3D%3D; lgc=siva108; dnk=siva108; mt=ci=35_1&np=; _mw_us_time_=1551427960460; unb=35112592; sg=828; _l_g_=Ug%3D%3D; cookie1=AiVeMQBoXXSDqQ1YPYQd7obzVS6WOBH2bO9cjk8pgAs%3D; _nk_=siva108; cookie17=UNX6w7w6sS0%3D'
    }

    try:
        print('>Starting...')
        req = request.Request(trans_url, headers=headers)
        rsp = request.urlopen(req)
        result = rsp.read()
        # result = json.loads(result)
        rsp_header = rsp.headers
        # print(rsp_header)
        con_type = rsp_header['Content-Type']
        code_set = con_type[con_type.find('charset=') + len('charset='): len(con_type)] if con_type.find('charset=') else 'utf-8'
        print(con_type)
        print(code_set)
        # print(result.decode(code_set))

        with open('request_cookie.html',  'w', encoding='utf-8') as f:
            f.write(result.decode(code_set))

    except error.HTTPError as e:
        print('HTTPError: {0}'.format(e.reason))
        print('HTTPError: {0}'.format(e))
    except error.URLError as e:
        print('URLError: {0}'.format(e.reason))
        print('URLError: {0}'.format(e))
    except Exception as e:
        print(e)

