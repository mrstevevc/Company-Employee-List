'''
Author: Stephen Lester
'''


from Employee import Employee #Imports 
from HourlyEmployee import HourlyEmployee
from SalariedEmployee import SalariedEmployee
from Manager import Manager
from Executive import Executive

class Company(object): #Newstyle class defintion


	def __init__(self, name): #Constructor
		self.name = name
		self.employees = []

	def hire(self, name, hours, salary, kind): #Hire method for adding employees
		if kind == 0:
			new_employee = HourlyEmployee(name, hours, salary)
		elif kind == 1:
			new_employee = SalariedEmployee(name, hours, salary)
		elif kind == 2:
			new_employee = Manager(name, hours, salary)
		elif kind == 3:
			new_employee = Executive(name, hours, salary)
		else:
			print("ERROR: INVALID INPUT")
			return
		self.employees.append(new_employee)
	
	def get_employees(self): #Returning employees
		for element in self.employees:
			kind = element.__class__.__name__
			if kind == 'HourlyEmployee':
				end = '/hr'
			elif kind == 'Manager':
				if element.paytype == 0:
					end = '/hr'
				else:
					end = '/yr'
			else:
				end = '/yr'
			print(element.name, "-", kind, "- salary: $", element.salary, end)

	def fire_employee(self, name): #Removing employees
		counter = 0
		for element in self.employees:
			to_fire = element.name
			if name == to_fire:
				print("Firing: ", to_fire)
				del self.employees[counter]
				return
			counter += 1
		print("Employee not found")
				
	def raise_employee(self, name): #Pay raise for employees
		for element in self.employees:
			if element.name == name:
				increase = int(input("Enter raise amount: "))
				element.set_salary(element.amount + increase)
				return
		print("Employee not found")

