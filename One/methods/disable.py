import pymysql
import requests
# from One.models import Pic
headers = {
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-CN;q=0.8,en;q=0.7',
    }


# def check():
#     pic = Pic.objects.filter(package__gt=60167)
#     for i in pic:
#         try:
#             r = requests.get(i.first_pic, headers=headers)
#             if eval(r.headers['Content-Length']) < 10240:
#                 i.available = False
#                 i.save()
#         except:
#             i.available = False
#             i.save()
#         print('包：%s  可用：%s' % (i.package, i.available))


def mysql():
    host = '47.104.171.3'
    port = 3306
    user = 'admin'
    password = 'eW2PSJbBBhkT'
    db = "Hive"
    try:
        connect = pymysql.connect(host=host, port=port, user=user, password=password, database=db, charset='utf8')
        cursor = connect.cursor()
        return connect, cursor
    except:
        return ''


def check():
    sql1 = "SELECT package, first_pic FROM Pic WHERE package > 64246"
    sql2 = "UPDATE Pic SET available=0 WHERE package = %s"
    con, cur = mysql()
    cur.execute(sql1)
    con.commit()
    all_pic = cur.fetchall()
    for i in all_pic:
        try:
            r = requests.get(i[1], headers=headers, timeout=30)
            if eval(r.headers['Content-Length']) < 10240:
                cur.execute(sql2 % i[0])
                con.commit()
        except:
            cur.execute(sql2 % i[0])
            con.commit()
        print('包：%s 完成' % i[0])


check()
