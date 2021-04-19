class Curtain():

    #Creating the curtain
    def __init__(self, id, curtainLocation, closed):
        self.id = id
        self.curtainLocation = curtainLocation
        self.closed = closed
    
    #Method to 
    def getID():
        return self.id

    def getLocation():
        return self.curtainLocation
    
    def isClosed():
        return self.closed
    
    def close():
        if self.closed == False:
            self.closed = True
        else:
            print("This curtain is already closed")
    
    def open():
        if self.closed == True:
            self.closed = False
        else:
            print("This curtain is already open")
    