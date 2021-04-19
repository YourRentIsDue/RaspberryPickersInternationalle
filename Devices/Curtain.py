class Curtain():

    def __init__(self, id, curtainLocation, closed):
        self.id = id
        self.curtainLocation = curtainLocation
        self.closed = closed
    
    def getID(self):
        return self.id

    def getLocation(self):
        return self.curtainLocation
    
    def isClosed(self):
        return self.closed
    
    def close(self):
        if self.closed == False:
            self.closed = True
        else:
            print("This curtain is already closed")
    
    def open(self):
        if self.closed == True:
            self.closed = False
        else:
            print("This curtain is already open")
    