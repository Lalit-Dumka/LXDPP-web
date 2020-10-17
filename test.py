import mysql.connector as mysql
db = mysql.connect(host="LalitDumka.mysql.pythonanywhere-services.com",user="LalitDumka",password='ktrhpdkn')
cursor = db.cursor()
cursor.execute(f"create database if not exists `LalitDumka$lakshit` ")
cursor.commit()
db.close()