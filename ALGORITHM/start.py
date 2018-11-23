import os


def run_app(file):
    try:
        os.startfile(file)
    except Exception as e:
        print("Error occurs...")


if __name__ == "__main__":
    chrome = r"C:\Users\lloyd\AppData\Local\Google\Chrome\Application\chrome.exe"
    pycharm = r"D:\Program Files\JetBrains\PyCharm Community Edition 2018.2.3\bin\pycharm64.exe"
    run_app(chrome)
    run_app(pycharm)
