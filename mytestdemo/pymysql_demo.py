import pymysql


class pyMySQL():
    __config = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': '111111',
        'db': 'jd_book_db',
        'charset': 'utf8'
    }

    # def __init__(self):
    #     self.host = "localhost"
    #     self.port = 3306
    #     self.user = ""
    #     self.password = 111111
    #     self.db = "jd_book_db"

    # def set_sql(self):
    #     sql = "create table 'jd_book' (" \
    #           "'id' int(11) not NULL AUTO_INCREMENT," \
    #           "'imgurl' varchar(255) NOT null ," \
    #           "'bookname' varchar(255) not  null ," \
    #           "'bookprice' varchar(255) not null ," \
    #           "'shuping' varchar(255) not null ," \
    #           "'chubanshe' varchar(255) not null " \
    #           ")ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1;"
    #     return sql

    # 创建表
    @classmethod
    def connect_mysql(cls):

        connection = pymysql.connect(**pyMySQL.__config)
        cur = connection.cursor()
        sql = "create table jd_book (" \
              "id int(11) auto_increment primary key ," \
              "bookname varchar(255) not  null ," \
              "bookprice varchar(255) not null ," \
              "shuping varchar(255) not null ," \
              "chubanshe varchar(255) not null " \
              ")DEFAULT CHARSET=utf8;"
        cur.execute(sql)

    @classmethod
    def insert_sql(cls, bookname, bookprice, shuping, chubanshe):
        connection = pymysql.connect(**pyMySQL.__config)
        cur = connection.cursor()
        sql = "insert into jd_book(bookname, bookprice, shuping, chubanshe)values(%s,%s,%s,%s)" % (
            bookname, bookprice, shuping, chubanshe)

        cur.execute(sql)


# if __name__ == '__main__':
#     a = pyMySQL()
#     a.connect_mysql()
