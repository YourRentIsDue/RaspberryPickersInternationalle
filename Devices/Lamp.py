class Lamp():

    #Creating the lamp
    def __init__(self, id, lampLocation, colour, activated, brightness):
        self.id = id
        self.lampLocation = lampLocation
        self.colour = colour
        self.activated = activated
        self.brightness = brightness
    
    #Method to return the ID
    def getID():
        return self.id

    #Method to return the location
    def getLocation():
        return self.lampLocation
    
    #Method to return the colour
    def getColour():
        return self.colour
    
    #Method to return whether or not it is activated
    def isActivated():
        return self.activated
    
    #Method to return the brightness
    def getBrightness():
        return self.brightness
    
    #Method to activate the lamp
    def turnOn():
        #Checking to see if the lamp is off
        if self.activated == False:
            self.activated = True
        else:
            print("This lamp is already turned on")
    
    #Method to deactivate the lamp 
    def turnOff():
        #Checking to see if the lamp is on
        if self.activated == True:
            self.activated = False
        else:
            print("This lamp is already turned off")

    #Method to change the lamp colour
    def changeColour(newColour):
        self.colour = newColour
    
    #Method to increase the brightness
    def increaseBrightness():
        self.brightness += 50
    
    #Method to decrease the brightness
    def decreaseBrightness():
        self.brightness -= 50
