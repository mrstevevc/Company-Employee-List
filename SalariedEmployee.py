import abc  #Imports
from Employee import Employee

class SalariedEmployee(Employee): #Newstyle class definition

	weeks = 52 #Constant

	def __init__(self, name, hours, salary): #Constructor
		self.name = name
		self.hours = hours
		self.amount = salary
		self.set_salary(salary)

	def employee_name(self, name):
		self.name = name
	
	def hours(self, hours):
		self.hours = hours

	def set_salary(self, amount):						
		self.salary = self.weeks * self.hours * amount		# $/yr

	def get_name(self):
		return self.name

	def get_hours(self):
		return self.hours

	def get_salary(self):
		return self.salary

	
