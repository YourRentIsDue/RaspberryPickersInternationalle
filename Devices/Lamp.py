class Lamp():

    def __init__(self, lampName, lampLocation, colour, activated):
        self.lampName = lampName
        self.lampLocation = lampLocation
        self.colour = colour
        self.activated = activated

    def getName():
        return self.lampName
    
    def getLocation():
        return self.lampLocation
    
    def getColour():
        return self.colour
    
    def isActivated():
        return self.activated
    
    def turnOn():
        self.activated = True
    
    def turnOff():
        self.activated = False

    def changeColour(newColour):
        self.colour = newColour