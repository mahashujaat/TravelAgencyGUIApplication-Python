from Administrator import Administrator
class Administrators:
    def __init__(self):
        self.administrators = []
        self.insert_dummy_data()  # Call the method to add dummy data during initialization
        self.allflight = []
    
    def has_administrator(self, username, password):
        for a in self.administrators:
            if a.login == username and a.password == password:
                return True
        #throw error
    
    def get_administrator(self, username, password):
        for a in self.administrators:
            if a.login == username and a.password == password:
                return a
                print(a)
                
        #throw error

    def insert_dummy_data(self):
        self.administrators.append(Administrator("Davey", "david46", "123"))
        self.administrators.append(Administrator("Angela", "angela123", "mypw"))
        self.administrators.append(Administrator("Rafiqul", "boss", "secure"))
        self.administrators.append(Administrator("Vishesh", "legend", "notsecure"))
        self.administrators.append(Administrator("Zyzz", "1", "1"))
