import abc
from Employee import Employee

class Manager(Employee):

	paytype = 0	 # 0 for hourly, 1 for salaried, starts off set to hourly
	weeks = 52
	hours = 0

	def __init__(self, name, hours, salary):
		self.name = name
		self.hours = hours
		self.amount = salary
		user_input = int(input("0 for hourly, 1 for salaried: "))
		self.set_paytype(user_input)
		self.set_salary(salary)

	def employee_name(self, name):
		self.name = name

	def hours(self, hours):
		self.hours = hours
	
	def set_salary(self, amount):
		if self.paytype == 1:
			self.salary = self.hours * self.weeks * amount
		else:
			self.salary = amount

	def set_paytype(self, paytype):
		self.paytype = paytype
	
	def get_name(self):
		return self.name

	def get_hours(self):
		return self.hours

	def get_salary(self):
		return self.salary
