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
@outer
def deco(a):
    print(f"i am from the decorating function: {a}")

# deco(10)


# ===================CLASSES(OOP)===========
class Animal:
    # class property
    species = "mammal"
    age = 20

    # instance property
    def __init__(self, color="red", sound="hoot"):
        self.color = f"  {color}"
        self.sound = f" the sound of the animal is {sound}"

    #method
    def getSpecies(self):
        print(f"i am a {self.species} and my color is {self.color}")
 
print("="*50)
horses = Animal()
print(Animal.__static_attributes__)
print(horses.color)
print(horses.getSpecies())