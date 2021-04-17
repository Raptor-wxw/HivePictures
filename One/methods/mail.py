import smtplib
from email.mime.text import MIMEText


def mail(email, title, content):    # 收件人邮箱， 邮件标题， 邮件内容
    mail_host = "smtp.qq.com"  # SMTP服务器
    mail_user = "296854007@qq.com"  # 用户名
    mail_pass = "dwenvmjyxaqbbgjb"  # 密码(这里的密码不是登录邮箱密码，而是授权码)

    sender = '296854007@qq.com'  # 发件人邮箱
    receivers = [email]  # 接收人邮箱

    title = title  # 邮件主题
    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        return 1
    except smtplib.SMTPException:
        return 0

# mail(2689969038, '123', '123')