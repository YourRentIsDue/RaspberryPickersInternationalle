class Lamp():

    def __init__(self, id, lampLocation, colour, activated, brightness):
        self.id = id
        self.lampLocation = lampLocation
        self.colour = colour
        self.activated = activated
        self.brightness = brightness
    
    def getID():
        return self.id

    def getLocation():
        return self.lampLocation
    
    def getColour():
        return self.colour
    
    def isActivated():
        return self.activated
    
    def getBrightness(self):
        return self.brightness
    
    def turnOn(self):
        if self.activated == False:
            self.activated = True
        else:
            print("This lamp is already turned on")
    
    def turnOff(self):
        if self.activated == True:
            self.activated = False
        else:
            print("This lamp is already turned off")

    def changeColour(self, newColour):
        self.colour = newColour
    
    def increaseBrightness(self):
        self.brightness += 50
    
    def decreaseBrightness(self):
        self.brightness -= 50
