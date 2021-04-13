from One.methods import mail


def about(email, name, message):
    title = "用户反馈"
    content = '用户"%s"反馈：\n用户邮箱：%s\n%s' % (name, email, message)
    manager = '296854007@qq.com'
    mail.mail(manager, title, content)
