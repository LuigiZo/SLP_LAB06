from Lab6.OOP_Lab import User
from datetime import date, datetime

class UserController:
    def __init__(self):
        self.users=[]
    def create_user(self, name, last_name, address, gender, birth_date, start_date=date.today()):
        u=User(name, last_name, address, gender, birth_date)
        self.users.append(u)
    def print_users(self):
        for user in self.users:
            print(user)

m="male"
f="female"
gender= m or f
#Point3
add1=("80-142", "S.George st.", 20)
add2=("80-142", "S.George st.", 18)
add3=("80-141", "King's Hill st.", 15)
add4=("80-140", "Miracles square", 2)
add5=("80-143", "S.John st.", 142)
uc=UserController()
uc.create_user("Alex", "Cena", add1, m, date(2000, 2, 2))
uc.create_user("Agata", "Happy", add2, f, date(1996, 3, 20))
uc.create_user("John", "Rock", add3, m, date(2001, 11, 25))
uc.create_user("Lia", "Fidat", add4, f, date(1993, 5, 12))
uc.create_user("Marianna", "Macan", add5, f, date(1999, 8, 30))
uc.print_users()