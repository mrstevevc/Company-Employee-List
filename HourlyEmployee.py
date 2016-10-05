import abc #Imports
from Employee import Employee

class HourlyEmployee(Employee): #Newstyle class definition

	def __init__(self, name, hours, salary): #Constructor
		self.name = name
		self.hours = hours
		self.amount  = salary
		self.salary = salary

	def employee_name(self, name):
		self.name = name

	def hours(self, hours):
		self.hours = hours

	def set_salary(self, amount):
		self.salary = amount

	def get_name(self):
		return self.name
	
	def get_hours(self):
		return self.hours

	def get_salary(self):			# $/hr
		return self.salary
