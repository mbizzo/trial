from customer import Customer
from question import Question
from questionnaire import Questionnaire


class Application:

    def __init__(self):
        self.questionnaire = self.create_questionaire()
        self.customers = []

    def create_questionaire(self):
    	# TODO: define the methods for checking that the different inputs are valid, that
    	# the necessary conditions are valid as defined at the beginning of the exercise
        def is_name(name):
            if name[0].isupper() and name[1:].islower():
                return True
            else:
                return False

        def is_number(number):
            if number.isdigit():
                return True
            else:
                return False

        def is_nationality(nationality):
            nationalities = ["swiss", "american", "french", "italian", "spanish", "english", "dutch"]
            nationality = str(nationality[0].lower() + nationality[1:])
            if nationality in nationalities:
                return True
            if not nationality in nationalities:
                return False

        def is_profession (profession):
            professions = ["student", "doctor", "nurse"]
            profession = str(profession[0].lower() + profession[1:])
            if profession in professions:
                return True
            else:
                return False

        questionnaire = Questionnaire([])
        questionnaire.add(Question("first_name", "What is the customer's first name?", is_name))
        questionnaire.add(Question("last_name", "What is the customer's last name?", is_name))
        questionnaire.add(Question("age", "What is the customer's age?", is_number))
        questionnaire.add(Question("nationality", "What is the customer's nationality?", is_nationality))
        questionnaire.add(Question("profession", "What is the customer's profession?", is_profession))
        return questionnaire

    def start(self):
    	# TODO: print a Hello message to the user and the initial help instructions
		
		# TODO: ask the user what he would like to do, the user should input one 
		# of the 3 commands described in the exercise. If it is a valid command, 
		# handle it, otherwise print an error message and the help instructions

        print "This is application will help you register Costumers in a database.\nPlease enter all names starting with an upper case."
        print "\nPlease choose an action from the following three possibilities"
        print "\nadd: Adds a new customer to the database."
        print "list: Lists all the previously registered user data."
        print "exit: Quits the application."
        choice =raw_input("\nadd, list or exit?: ")
        choices = ["add", "list", "exit"]
        if choice in choices:
            if choice == "add":
                self.register_new_customer()
            if choice == "list":
                self.list_customers()
            if choice == "exit":
                quit()
        if not choice in choices:
            print "\nError: invalid input"
            self.print_help()


    def print_help(self):
        print("You can type one of the following actions:\n\nadd - Add a new customer\nlist - list the existing customers\nexit - exit the database\n")
	
    def register_new_customer(self):
        tmp = self.questionnaire.start()
        # if you don't understand what happens here, check this link:
        # https://docs.python.org/2/tutorial/controlflow.html#unpacking-argument-lists
        self.customers.append(Customer(**tmp))
        print("You successfully registered a new customer.\n")
        self.start()

    def list_customers(self):
    	# TODO: list all the customers registered so far, by printing their first and last
    	# names, the age, profession and nationality
        for c in self.customers:
            print
            print c
        self.start()


if __name__ == '__main__':
    Application().start()

Application().start()