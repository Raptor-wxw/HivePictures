import pymysql
import requests
from bs4 import BeautifulSoup


class Save:
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
    insert1 = "INSERT INTO Pic(package, text, first_pic) VALUES (%d, '%s', '%s');"
    insert2 = "INSERT INTO Pics(package, photo) VALUES (%d, '%s');"
    url = 'https://www.94imm.com/article/%s/'
    photo = 'https://www.94imm.com'
    first_pic = ''

    def __init__(self, num, connect, cursor):
        self.num = num
        self.package = eval(num)
        self.connect = connect
        self.cursor = cursor

    def soup(self):
        url = self.url % self.num
        try:
            r = requests.get(url, headers=self.headers, timeout=20)
            if r.status_code != 200:
                return ''
            else:
                return r.text
        except:
            return 'timeout'

    @staticmethod
    def title(html):
        try:
            soup = BeautifulSoup(html, "html.parser")
            title = soup.find_all('h1')[1].string
            return title
        except:
            return ''

    @staticmethod
    def img(html):
        try:
            soup = BeautifulSoup(html, "html.parser")
            img_tags = soup.article.find_all('img')
            return img_tags[1:]
        except:
            return ''

    def save_title(self, title):
        sql = self.insert1 % (self.package, title, self.first_pic)
        self.cursor.execute(sql)
        self.connect.commit()

    def save_pic(self, image):
        first = 0
        for i in image:
            src = i.get('data-src')
            url = self.photo + src
            sql = self.insert2 % (self.package, url)
            if not first:
                self.first_pic = url
            self.cursor.execute(sql)
            self.connect.commit()
            first = 1


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


if __name__ == '__main__':
    for j in range(62746, 65000):
        print(j)
        con, cur = mysql()
        while not (con and cur):
            con, cur = mysql()
        save = Save(str(j), con, cur)
        raw = save.soup()
        while raw == 'timeout':
            raw = save.soup()
        if raw:
            my_images = save.img(raw)
            while not my_images:
                my_images = save.img(raw)
            save.save_pic(my_images)
            my_title = save.title(raw)
            while not my_title:
                my_title = save.title(raw)
            save.save_title(my_title)
            print(j, 'over')
        else:
            print(j, 'over')
            continue
