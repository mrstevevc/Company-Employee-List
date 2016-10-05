from Company import Company #Imports
import pickle
try: #Try and catch for correct and incorrect input
	user_input = int(input("Enter 0 to start a new company, 1 to load a company: "))
	if user_input == 0:
		while True:
			name = input("Welcome! Please name your company: ")
			if name.endswith('.p'): #Necessary for object serialization
				break
			else:
				print("ERROR: COMPANY NAME MUST HAVE FILE EXTENSION '.p'")
		company_one = Company(name)
		user_input = name
	else:
		while True:
			user_input = input("Please type in company to load: ")
			if user_input.endswith('.p'):
				break
			else:
				print("ERROR: COMPANY NAME MUST HAVE FILE EXTENSION '.p'")
		while True:
			try: #Object serialization, saving the data after program close
				company_one = pickle.load( open(user_input, "rb"))
				break
			except IOError:
				print("ERROR: FILE DOES NOT EXIST")
				user_input = input("Please type in company to load: ")

	while True:
		option = input("Press h to hire an employee, v to view employees, r to give an employee a raise, f to fire an employee, press s to save: ")
	
		if option == 'h': #Options to alter employees
			name = input("Employee name: ")
			hours = int(input("Hours worked per week: "))
			salary = int(input("Salary per hour: "))
			kind = int(input("0 = Hourly, 1 = Salaried, 2 = Manager, 3 = Ex: "))
			company_one.hire(name, hours, salary, kind)
		elif option == 'v':
			company_one.get_employees()
		elif option == 'r':
			to_raise = input("Employee to receive a raise: ")
			company_one.raise_employee(to_raise)
		elif option == 'f':
			to_fire = input("Employee to fire: ")
			company_one.fire_employee(to_fire)
		elif option == 's':
			pickle.dump(company_one, open(user_input, "wb"))
		else:
			print("ERROR: INVALID INPUT")

except EOFError: #Exceptions
	pass

except ValueError:
	print("ERROR: MUST BE AN INTEGER INPUT")
	pass

except KeyboardInterrupt:
	pass
