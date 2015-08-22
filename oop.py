#!/usr/bin/env python
# -*- coding: utf-8 -*-

'Co,.Ltd:Lcmj, programe:practice'

__author__ = 'naivecao'


# procedure-oriented
std1 = {'name':'xiaocao', 'score':61}
std2 = {'name':'xiaoming', 'score':72}
def print_score(std):
	print '%s:%s' % (std['name'], std['score'])

#print_score(std1)
#print_score(std2)

# oop
class Student(object):
	def __init__(self, name, score):
		self.__name = name
		self.__score = score
	
	def print_score(self):
		print '%s:%s' % (self.__name, self.__score)
	
	def get_grade(self):
		if self.__score >= 90:
			return 'A'
		elif self.__score >= 60:
			return 'B'
		else:
			return 'C'
	
	def set_score(self, score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('bad score')

#a = Student('xiaocao', 61)
#b = Student('xiaoming', 72)
#a.print_score()
#a.set_score(10)
#a.print_score()

# inherit and polymorphism
class Animal(object):
	def run(self):
		print 'Animal is running'

class Dog(Animal):
	def run(self):
		print 'Dog is running'
	
	def eat(self):
		print 'Eating meat'
	pass
	
class Cat(Animal):
	pass
	
dog = Dog()
#dog.run()
#cat = Cat()
#cat.run()
#print isinstance(dog, Dog)
#print isinstance(dog, Animal)
#print isinstance(dog, Object)
def run_twice(animal):
	animal.run()
	animal.run()

#run_twice(Animal())
#import types
#print type(dog)
#print types.StringType
#print dir(dog)
class A(object):
	__slots__ = ('a', 'b')

a = A()
a.a = 'a'
class student(object):

	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('Score is not correct')
		if value < 0 or value > 100:
			raise ValueError('Score must between 0~100')
		self._score = value

#s = student()
#s.score = 60
#print s.score
#s.score = 'a'
# custom class
class ABC(object):
	def __init__(self, name):
		self.name = name
	def __str__(self):
		return 'ABC object (name: %s)' % self.name
	__repr__ = __str__
	
# Metaclasses
class Hello(object):
	def hello(self, name = 'world'):
		print('Hello, %s.' % name)

h = Hello()
print type(Hello)
print type(h)

def fn(self, name = 'world'):
	print('Hello, %s.' % name)

World = type('World', (object,), dict(World = fn))
w = World()
#print type(World)
#print type(w)
class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):
		attrs['add'] = lambda self, value:self.append(value)
		return type.__new__(cls, name, bases, attrs)

class MyList(list):
	__metaclass__ = ListMetalass