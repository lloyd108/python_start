import webbrowser
import os


def open_web(browser='browser', browser_path='path', url='url'):
    if browser == 'browser' or browser_path == 'path' or url == 'url':
        exit(111)
    else:
        browser = browser
        url = url
        browser_path = browser_path

    webbrowser.register(browser, None, webbrowser.BackgroundBrowser(browser_path))
    webbrowser.get(browser).open(url, new=1, autoraise=True)


def open_app(app_path):
    os.startfile(app_path)


if __name__ == '__main__':
    open_web('chrome', r'C:\Users\lloyd\AppData\Local\Google\Chrome\Application\chrome.exe', r'https://study.163.com/member/login.htm')
    open_app(r'D:\Program Files\JetBrains\PyCharm Community Edition 2018.3.5\bin\pycharm64.exe')
    open_app(r'D:\Program Files\Sublime Text 3\sublime_text.exe')