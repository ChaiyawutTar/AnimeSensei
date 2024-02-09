class User:
    def __init__(self, id, password):
        self.id = id
        self.password = password

    def getID(self):
        return self.id
    
    def setID(self, id):
        self.id = id

    def getPassword(self):
        return self.password
    
    def setPassword(self, password):
        self.password = password