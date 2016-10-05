from abc import ABCMeta, abstractmethod #Import

class Employee(metaclass=ABCMeta): #Newstlye class definition

	@abstractmethod # Methods that need to be implemented for child classes
	def employee_name(self, name):
		pass

	@abstractmethod
	def set_salary(self, hours, salary): 
		pass
	
