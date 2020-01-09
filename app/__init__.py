#jika saat di migrate error, install mysql client ($ sudo apt-get install mysql-client ),
# lalu tulis kode di bawah ini:
import pymysql
pymysql.version_info = (1, 3, 13, "final", 0)
pymysql.install_as_MySQLdb()