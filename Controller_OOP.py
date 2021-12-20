from Lab6.OOP_Lab import User
from datetime import date, datetime

class UserController:
    def __init__(self):
        self.users=[]
    def create_user(self, name, last_name, address, gender, birth_date, start_date = date.today()):
        u=User(name, last_name, address, gender, birth_date)
        self.users.append(u)
    def print_users(self):
        for user in self.users:
            print(user)

m="male"
f="female"
gender= m or f
#Point3
add1=("80-142", "S.Paolo st.", 12)
add2=("80-142", "Dworcowa st.", 21)
add3=("80-141", "S.Gennaro st.", 8)
add4=("80-140", "Ks. Ignacego", 78)
add5=("80-143", "Jozefa st.", 91)
uc=UserController()
uc.create_user("Alex", "Cena", add1, m, date(199, 10, 10))
uc.create_user("Agata", "Happy", add2, f, date(1998, 12, 16))
uc.create_user("John", "Rock", add3, m, date(2000, 9, 30))
uc.create_user("Lia", "Fidat", add4, f, date(1989, 6, 22))
uc.create_user("Marianna", "Macan", add5, f, date(2002, 1, 2))
uc.print_users()