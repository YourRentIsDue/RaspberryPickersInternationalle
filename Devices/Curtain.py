class Curtain():

    def __init__(self, curtainLocation, closed):
        self.curtainLocation = curtainLocation
        self.closed = closed
    
    def getLocation(self):
        return self.curtainLocation
    
    def isClosed(self):
        return self.closed
    
    def close(self):
        if self.closed = False:
            self.closed = True
        else:
            print("This curtain is already closed")
    
    def open(self):
        if self.closed = True:
            self.closed = False
        else:
            print("This curtain is already open")
    