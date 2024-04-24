# class Person:
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id
# p1 = Person("Asik",4976)

# print(p1.name)
# print(p1.id)


class People:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    
    def writting(self):
        print(f"Hey! i am {self.name},now i am writting")
        print(f"last 4 digits of my id is {self.id},now i am writting this code")

Asik = People("Asik",4976)
Asik.writting()
        