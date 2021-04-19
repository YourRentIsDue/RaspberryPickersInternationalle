class Lamp():

    def __init__(self, lampName, lampLocation, colour, activated):
        self.lampName = lampName
        self.lampLocation = lampLocation
        self.colour = colour
        self.activated = activated

    def getName(self):
        return self.lampName
    
    def getLocation(self):
        return self.lampLocation
    
    def getColour(self):
        return self.colour
    
    def isActivated(self):
        return self.activated
    
    def turnOn(self):
        self.activated = True
    
    def turnOff(self):
        self.activated = False

    def changeColour(self,newColour):
        self.colour = newColour