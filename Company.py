from Employee import Employee
from HourlyEmployee import HourlyEmployee
from SalariedEmployee import SalariedEmployee
from Manager import Manager
from Executive import Executive
from Tree import TreeNode, BinarySearchTree

class Company(object):

	tree = 0 # 0 for standard array, 1 for binary search tree

	def __init__(self, name):
		self.name = name
		if self.tree == 0:
			self.employees = []
		else:
			self.tree = BinarySearchTree()

	def hire(self, name, hours, salary, kind):
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
		if self.tree == 0:
			self.employees.append(new_employee)
		else:
			self.tree.put(new_employee, 0)
	
	def get_employees(self):
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

	def fire_employee(self, name):
		counter = 0
		for element in self.employees:
			to_fire = element.name
			if name == to_fire:
				print("Firing: ", to_fire)
				del self.employees[counter]
				return
			counter += 1
		print("Employee not found")
				
	def raise_employee(self, name):
		for element in self.employees:
			if element.name == name:
				increase = int(input("Enter raise amount: "))
				element.set_salary(element.amount + increase)
				return
		print("Employee not found")
		
#def tree_fire(self, name):
		

