# MySQL холболтыг үүсгэх хэсэг
import mysql.connector  # MySQL холбогч санг импортлох
from mysql.connector import Error  # MySQL холбогч сангаас Error класс импортлох
import random  # Санамсаргүй өгөгдөл үүсгэхийн тулд random модулийг импортлох
 
 
def connect_fetch_data():
    """  MySQL database холболт хийж өгөгдлийг татах  """
    conn = None  # Холболтын connection хувьсагчид анхны утга оноох
    try:
 
        #Өгөгдсөн шаардалагын дагуу MySQL өгөгдлийн сантай холболт үүсгэх хэсэг
        #Host-host-ийн нэр
        #datadbase- өгөгдлийн сангийн нэр
        #user- холбогдох хэрэглэгчийн нэр
        #password- нэвтрэх нууц үг
 
        conn = mysql.connector.connect(host='localhost',
                                       database='enh',
                                       user='root',
                                       password='4gamerz984')
       
        if conn.is_connected():  # Холболт амжилттай болсныг шалгах хэсэг
            print('Connected to MySQL database')
            cursor = conn.cursor()  # SQL асуулгыг гүйцэтгэх курсор объект үүсгэх хэсэг
 
            #'Students' хүснэгтээс өгөгдлийг авах хэсэг
            cursor.execute("SELECT Name, Student_id FROM Students")
            students = cursor.fetchall()  # Үр дүнгээсс бүх өгөгдлийг татаж авах хэсэг
 
            # 'Team_work' хүснэгтээс агуулгын өгөгдлийг авах хэсэг
            cursor.execute("SELECT Aguulga FROM Team_work")
            topics = [item[0] for item in cursor.fetchall()]  # Үр дүнгээсс бүх өгөгдлийг татаж авах хэсэг
 
            # Татсан өгөгдлөө буцаах хэсэг
            return students, topics
    except Error as e:
        print(e)  # Алдаа гарвал алдааны мэдээлэл хэвлэнэ
    finally:
        if conn is not None and conn.is_connected():
            conn.close()  # Өгөгдлийн сантай хийсэн холболтоо хаах хэсэг
