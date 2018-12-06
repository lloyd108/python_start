import smtplib
from email.mime.text import MIMEText
from datetime import datetime as dt
from email.header import Header


msg = MIMEText("Hello, this msg from myEmail2 and time is {0}".format(dt.now()), "plain", "utf-8")
msg_from = Header("Header...nothing specital<yanzhuo108@yanzhuo.com>", "utf-8")
msg_to = Header("Send to myself just for check<yanzhuo108@yz.yz>", "utf-8")
msg_subject = Header("Simple subject", "utf-8")

msg['From'] = msg_from
msg['To'] = msg_to
msg['Subject'] = msg_subject

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