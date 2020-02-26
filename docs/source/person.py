class Person:
    '''
    A person (a typical contact saved in our system)
    '''
    def __init__(self, name, age):
        '''
        Inits with a default name of unknown and age zero.

        :param name: (str) name of the person
        :param age: (int) age of the person
        '''
        self.name="unknown" 
        self.age=0 

    def display_person(self):
        '''
        Displays information for a person

        :return: tuple: Returns name, age of person
        '''
        print(self.name, self.age)
        return self.name, self.age
    
    def display_name(self):
        '''
        Displays name of a person

        :return: (str) name of the person
        '''
        print(self.name)
        return self.name
    
    def display_age(self):
        '''
        Displays age of a person

        :return: (int) age of the person
        '''
        print(self.age)
        return self.age
    