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
def distribute_students_to_topics(students, topics): #Сэдвүүдэд сурагчдыг хуваарилах
    """ Distribute students ensuring teams have variable sizes with at least 3 members """
    random.shuffle(students) #Даалгаврын санамсаргүй байдлыг хангахын тулд оюутнуудын жагсаалтыг санамсаргүй байдлаар хольж байна.
    assignments = {topic: [] for topic in topics} #Энэ нь оюутнуудын сэдвүүдийн даалгаврыг хадгалахын тулд "assignments" нэртэй хоосон сан эхлүүлж байна.
    assigned_students = set()
 
    base_size = len(students) // len(topics)
    extra = len(students) % len(topics)#Энэ нь нийт оюутны тоог нийт сэдвийн тоонд хуваасан үндсэн дээр сэдэв бүрийн үндсэн хэмжээг тооцдог.
 
    student_iter = iter(students)
    try:
        for topic in topics:
            target_size = base_size + (1 if extra > 0 else 0)
            extra -= 1
 
            while len(assignments[topic]) < target_size:
                student = next(student_iter)
                if student[1] not in assigned_students:
                    assignments[topic].append(student)
                    assigned_students.add(student[1]) #нэ нь сэдвүүдийг давтаж, баг бүр дор хаяж 3 гишүүнтэй хувьсах хэмжээтэй болтол сэдэв тус бүрээр оюутнуудыг хуваарилдаг.
    except StopIteration:
        print("Not enough students to assign at least three to each topic.") #хэрэв Сэдэв бүрд дор хаяж гурваас доошгүй оюутан оноох хангалттай сурагч байхгүй бол ингэж хэвлэнэ.
 
    return assignments
def print_assignments(assignments):
    """ Print the assignments of students to topics """
    for topic, students in assignments.items():
        print(f"{topic} ({len(students)} students):")
        for student in students:
            print(f"    {student[0]}, '{student[1]}'")
            #Энэ нь `assignments` сангийн  сэдэв бүрийг давтаж, тухайн сэдвийн нэрийг түүнд хуваарилагдсан оюутнуудын хамт хэвлэдэг.
            #Тухайн сэдэвт хуваарилагдсан оюутан бүрийн нэр, ID хэвлэдэг.
 
def main():
    students, topics = connect_fetch_data() #Өгөгдлийн сангаас оюутнууд болон сэдвүүдийг татаж байна
    if students and topics:
        assignments = distribute_students_to_topics(students, topics) #Хэрэв өгөгдөл амжилттай татагдсан бол оюутнуудыг сэдвүүдэд түгээх `students_to_topics()` функцийг дууддаж байна.
        print_assignments(assignments)
 
if __name__ == "__main__":
    main()
