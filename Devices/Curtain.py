class Curtain():

    # Creating the curtain
    def __init__(self, id, curtainLocation=None, closed=0):
        self.id = id
        self.curtainLocation = curtainLocation
        self.closed = closed

    # Method to return the ID
    def getID(self):
        return self.id

    # Method to return the location
    def getLocation(self):
        return self.curtainLocation

    # Method to chech if its closed
    def isClosed(self):
        return self.closed

    # Method to close the curtain
    def close(self):
        # Checking to see if the curtain is already open
        if self.closed == False:
            self.closed = True
        else:
            print("This curtain is already closed")

    # Method to open the curtain
    def open(self):
        # Checking to see if it is already closed
        if self.closed == True:
            self.closed = False
        else:
            print("This curtain is already open")

    def setClosed(self, value):
        self.closed = value
        #print(self.closed)
