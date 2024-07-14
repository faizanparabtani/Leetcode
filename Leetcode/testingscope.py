# def simfunc(s):
#     for k, v in enumerate(s):
#         s[k] *= 2
#     return s
#     # return [i*2 for i in s]

# def myfunc():
#   x = 300
#   def myinnerfunc():
#     print(x)
# #   myinnerfunc()

# myfunc()

# arr = [1, 2, 3]
# print(simfunc(arr))
# print(arr)

# x = 300

# def myfunc():
#   global x
#   x = 200

# myfunc()

# print(x)

# listcomp = [i*2 for i in range(5, 1, -1)]
# print(listcomp)

# values = [[x,y] for x in range(5) for y in range(3)]

# values = []
# for x in range(5):
#     for y in range(3):
#         values.append((x,y))

# print(values)

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname):
#     super().__init__(fname, lname)
#     self.graduationyear = 2019

# def __str__(self):
#     return "This is students string method"

# x = Student("Mike", "Olsen")
# print(Student.__dict__)
# print(x.graduationyear)
# print(x.printname())


# def testfunc():
#     print('hello')

# ans = testfunc()
# print(ans)

# new_lis = [[y*3 for y in range(x)] for x in range(10)]

# print(new_lis)

# Python program to demonstrate working
# of map.

# Return double of n
def addition(n):
	return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)

print(list(result))
print(result)
