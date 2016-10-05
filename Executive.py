import abc #Imports
from Employee import Employee

class Executive(Employee): #Newstyle class defintion

	bonus = 0   #Constants
	weeks = 52

	def __init__(self, name, hours, salary): #Constructor
		self.name = name
		self.hours = hours
		self.amount = salary
		value = int(input("Please insert bonus: "))
		self.set_bonus(value)	
		self.set_salary(salary)

	def employee_name(self, name): #Setters 
		self.name = name
	
	def set_bonus(self, bonus):
		self.bonus = bonus

	def set_salary(self, amount):
		self.salary = (self.weeks * amount * self.hours) + self.bonus

	def get_name(self): #Getters, not necessary but nice for OOD
		return self.name

	def get_bonus(self):
		return bonus

	def get_salary(self):
		return self.salary
