from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):

	@abstractmethod
	def employee_name(self, name):
		pass

	@abstractmethod
	def set_salary(self, hours, salary): 
		pass
	
