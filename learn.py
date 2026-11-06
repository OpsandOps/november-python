# ## python/django -- 
# # most data structure are created as classes.
# # data types  -- str, int, float, dict, list, tuples 
# # methods
# # loops and conditional expressions (if, while, match-case, for)
# # functions
# # classes (oop) / object

# ## ============ DATA TYPES ==============
# ## STRINGS - enclosed in a "", ''
# ## ======================================

# letter = 'a'
# # methods of strings
# dir('a'), dir(letter)

# ## ====INTEGERS ================(real)
# number = 20
# dir(2), dir(number)

# ## -=====FLOATING POINT ========(decimal/fraction)
# decimal_number = 70.000

# ## list ===========(sequence, enclosed in [])
# # ordered, indexed, changeable
# mylist = ["strings", 7000, 70.0000, 80, 90, 60, 50, 40]
# mylist[0] = 3000
# print(mylist[:-3])

# ## dictionaries ==============================(sequence, enclosed {}, key:value)
# ## indexed, ordered, changed
# mydictionary = {
#     #  key : value
#     "name": "python",
#     "mylist": ["strings", 90.00]
# }
# # methods
# """
# ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', 
# '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
#  '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__',
#   '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', 
#   '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
# """
# value = mydictionary.get("name", None)
# print(value)
# # print([i for i in mydictionary.keys()])
# print(mydictionary.pop("mylist"))
# print(type(mydictionary.popitem()))
# mydictionary.update({"school": "bizmarrow"})
# print(mydictionary)
# print("="*80)
# print(mydictionary)
# mydictionary['city'] = "abuja"
# print([i for i in mydictionary.values()])

# # =======tuple (sequence, enclosed ())
# # indexed, cant be changed, ordered
# # methods
# """
# ['__add__', '__class__', 
# '__class_getitem__', '__contains__', '__delattr__', '__dir__', 
# '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
# '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', 
# '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__',
#  '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', 
#  '__subclasshook__', 'count', 'index']
# """
# print("+"*70)
# mytuple = (1, 3, 4)
# print(mytuple.count.__doc__)
# print(mytuple.count(3))
# alist = list(mytuple)
# print(alist[0])


# # ================================
# # ====LOOPS ==========(list, dictionaries, tuples)
# # ===========================

# print("="*50)

# colors = ["red", "blue", "green", "purple", "cyan"]
# print(len(colors))

# # if conditional-expression:
# #     TrueBlock
# # else:
# #     FalseBlock
# # ========== "", []. {}. () amount False
# isloggedIn = False
# age = 18
# isloggedout = False

# if isloggedIn:
#     if age < 18:
#         print("user is old enough and logged in")
#     else:
#         print("user is not old enough but loggged in")
# else:
#     isloggedout = True

# print(isloggedout)
    

# if "red".upper() in colors:
#     print("red".upper())
# else:
#     print(f"RED is not in colors")

# a = 200
# b = 20

# if a == 90:
#     print(f"{a} is equal to 90")

# # while ========================= open sequence ====
# first = 90
# order = 0
# while True:
#     print(" i am True")
#     order += 1
#     if order == first:
#         break
    

# num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# evenNum = []
# oddNum = []
# for i in num:
#     if i % 2 == 1:
#        print(f"{i} is even")
#     else:
#         print(f"{i} is odd")


# ===============functions=======================
# f(x) = x + 2 + x 
# def functionName(params):
#        functionBody
#       print()
#       return
#
# invocation------------
# functionName()
# positional paramaters: 
# default parameters: 
# positional must come before default
# ===============================================


# decorator ==============================
def outer(func):
    def inner():
        print("before decorating")
        func(10)
        print("after decorating")
    return inner()

# ======================== ...

# decorator ==============================
# def outer(param1, param2):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             print(f"{param1} and {param2}")
#             result = func(*args, **kwargs)
#             print(f"{param1} and {param2}")
#             return result
#         return wrapper
#     return decorator

# @outer("args1", "args2")
# def greet(name):
#     print(f"hello {name}")

# greet("john")


# ===================CLASSES(OOP)===========
# class names should always begim with capital letters
# =============================================

class Student:
    # class attr
    name = "Bizmarrow"
    course = "Python"

    def setName(self, *args):
        self.name = args

    def setCourse(self, *args):
        self.course = args

    def getName(self):
        return self.name

    # class properties
    def __init__(self, age, state):
        self.age = age
        self.state = state

    def changeState(self):
        user_state = input("Enter your state here: ").lower().strip()
        self.state = user_state
        return f" new state : {user_state}"

# student_One = Student("")

# print("-" * 60)
# print(student_One.__dict__)
# student_One.name = "Timothy"
# print(student_One.__dict__)
# newName = student_One.setName("Torbita")
# print(student_One.__dict__)
# print(student_One.getName())
# print(Student.name, Student.course)
# print(dir(Student))
# print(Student.__static_attributes__)
# newname = Student.setName("Torbita")
# print(newname)
# print('-' * 70)
# object = Student(20, "Abuja")
# # print(dir(Student))
# print(object.changeState())
# print(object.state)

# paradigm in python OOP
# Inheritance

print('==' * 90)
print("Inheritance =====")


class Parent:
    def __init__(self, parentname):
        self.parentname = f"my surname is {parentname}"

    def changeParentName(self, name):
        if not name:
            return {"error": "requires name, no name given"}
        self.parentname = name.strip().lower()

class Child(Parent):
    def __init__(self, childname, parentname):
        super().__init__(parentname)
        self.childname = childname

dad = Parent("Mandy")
print(dad.__static_attributes__)
son = Child("Daniel", "Mandy")
print(son.__static_attributes__)
print(son.childname, son.parentname)
son.changeParentName("elion")
print(f"\n [NEW PARENT NAME] {son.parentname}")
# print(son.changeParentName("elion"))

# POLYMORPHISM ======single function behaving in different ways, and belong to seperate classes

class Vehicle:
    def __init__(self, name, sound, model="benz"):
        self.name = f"{name}"
        self.sound = f"{sound}"
        self.model = model     

    def changeSound(self, sound):
        if not sound:
            return {"error": "requires sound, none given"}
        self.sound = f"{sound} is the new vehicle sound for vehicle"

class Car(Vehicle):
    def __init__(self, name, sound, color, model):
        super().__init__(name, sound, model)
        self.color = color

    def changeSound(self, sound):
        if not sound:
            return {"error": "requires sound, none given"}
        self.sound = f"{sound} is the new car sound for car"

vehicle = Vehicle("lorry","zoom")
print(vehicle.name, vehicle.sound, vehicle.model)

car = Car("suv", "sooom", "red", "2009")
print(f"NAME: {car.name}, SOUND: {car.sound}, MODEL: {car.model}, COLOR: {car.color}")

# print("="* 40)
# sound = ["VOOOM", "COOOM"]
# methods = [vehicle, car]
# for index, i in enumerate(methods):
#     if isinstance(i, Vehicle):
#         i.changeSound(sound[index])
#         print(i.sound)

# === ENCAPSULATED =========
class Fruits:
    def __init__(self, name, color):
        self.name = name
        self.__color = color

    def setColor(self, color):
        """function sets the color property of the instance"""
        self.color = color

    def getColor(self):
        """function that returns the encapsulated property"""
        return self.color

print("="*70)
fruit = Fruits("mango", "greenish-yellow")
print(fruit.name)
print(fruit.__dict__)

fruit.setColor("purple")
print(fruit.__dict__)

print(fruit.color)

