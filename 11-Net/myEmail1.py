import smtplib
from email.mime.text import MIMEText
from datetime import datetime as dt


msg = MIMEText("Hello, this msg from myEmail1 and time is {0}".format(dt.now()), "plain", "utf-8")

from_addr = "lloyd108@163.com"
from_pwd = "Zfb19900218"

to_addr = "lloyd108@163.com"

smtp_srv = "smtp.163.com"


try:
    # srv = smtplib.SMTP(smtp_srv.encode(), 25)
    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465)
    srv.login(from_addr, from_pwd)
    srv.sendmail(from_addr, [to_addr], msg.as_string())
    srv.quit()
except Exception as e:
    print(e)