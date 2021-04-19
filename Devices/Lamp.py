class Lamp():

    def __init__(self, lampLocation, colour, activated, brightness):
        self.lampLocation = lampLocation
        self.colour = colour
        self.activated = activated
        self.brightness = brightness
    
    def getLocation(self):
        return self.lampLocation
    
    def getColour(self):
        return self.colour
    
    def isActivated(self):
        return self.activated
    
    def getBrightness(self):
        return self.brightness
    
    def turnOn(self):
        if self.activated = False:
            self.activated = True
        else:
            print("This lamp is already turned on")
    
    def turnOff(self):
        if self.activated = True:
            self.activated = False
        else:
            print("This lamp is already turned off")

    def changeColour(newColour):
        self.colour = newColour
    
    def increaseBrightness(self):
        self.brightness += 50
    
    def decreaseBrightness(self):
        self.brightness -= 50
