class User:
    # Constructor
    def __init__(self,name,balance): # Atributte
        self.name = name 
        self.balance = balance

    """
        self.name = name 
        self.balance = balance

        'name' and 'balance' This isnt only state, but atributtes holding data in the object and had lifecyle, until the data is changed and given behaviour in the method
    
    """

    # Method
    def get_info(self):
        return f"Welcome: {self.name}"
    
user1 = User("Jerry",2000)
print(user1.get_info())