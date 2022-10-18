class Calculator:
    def add(self, a, b):
        return a+b
    def sub(self, a, b):
        return a-b
    def mult(self, a, b):
        return a*b
    def div(self, a, b):
        return a/b
c = Calculator()
print(c.add(2, 4))
#6

#Write a program to concatenate, reverse and slice a string?
class String:
    def concat(self, a, b):
        return a+b
    def reverse(self, s):
        return s[::-1]
    def slicestr(self, s, start, end):
        return s[start:end+1]
s = String()
print(s.slicestr('ramkumar', 1, 4))
#amku

#Why is Python a popular programming language?
#It uses a simplified syntax with an emphasis on natural language, for a much easier learning curve for beginners. And, because Python is free to use and is supported by an extremely large ecosystem of libraries and packages, it's often the first-choice language for new developers.

#What are the other Frameworks that can be used with python?
#Pyramid, TurboGears, Web2py, CherryPy, Flask, Sanic

#Full form of WSGI
#The Web Server Gateway Interface is a simple calling convention for web servers to forward requests to web applications or frameworks written in the Python programming language.

#Consider a list (list = []). You can perform the operations

class List:
    def __init__(self):
        self.l = []
    def insert(self, a, pos):
        if pos <= len(self.l):
            self.l.insert(pos, a)
        else:
            print('position out of range')
            return
        return self.l
    def remove(self, a):
        self.l.remove(a)
        return self.l
    def append(self, a):
        self.l.append(a)
        return self.l
    def sort(self):
        return self.l
    def pop(self):
        return self.l.pop()
    def reverse(self):
        return self.l[::-1]
li = List()
print(li.insert(11, 0))
print(li.insert(12, 1))
print(li.remove(11))
print(li.append(13))
print(li.append(15))
print(li.sort())
print(li.pop())
print(li.reverse())
#[11]
#[11, 12]
#[12]
#[12, 13]
#[12, 13, 15]
#[12, 13, 15]
#15
#[13, 12]
