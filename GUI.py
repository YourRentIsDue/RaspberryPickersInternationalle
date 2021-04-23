import tkinter as tk
import datetime
from Room import Room
from Sensors import *
from Devices import *


class Application(tk.Frame):
    def __init__(self, rooms, master=None):
        super().__init__(master)
        self.rooms = rooms
        self.time = datetime.datetime.now()
        #self.time = self.time.replace(hour=14)
        #function that checks the sensors
        self.after(2000,self.checkRooms) 
        #set size 
        self.master.minsize(400, 600)

        #holds the widgets for the rooms
        self.roomList = []
        self.roomInfo = []
        self.checkBoxVars = []

        #Used for room list in dev tools
        self.roomNames = []
        for room in rooms:
            self.roomNames.append(room.name)
        self.selectedRoom = tk.StringVar()
        self.selectedRoom.set(self.roomNames[0])
        self.newRoomName = tk.StringVar()
        
        self.pack()
        self.createWidgets()
        #starts the homescreen
        self.setHomeScreenRooms()

        #unfinished
        #self.saveData()
        #self.readData()

    def createWidgets(self):

        # Home screen----------#

        # create home frame
        self.homeScreen = tk.Frame(self, width=400, height=600, bg="red")
        self.homeScreen.pack()

        # add home screen title
        self.title = tk.Label(self.homeScreen, text="Eco Friendly Sensors", font=("Courier", 16))
        self.title.pack(side="top", pady=5)

        # create frame to hold rooms
        self.roomFrame = tk.Frame(self.homeScreen, bg="blue", height=20, width=50, bd=2)
        self.roomFrame.pack(padx=20, pady=20)


        
        #button for opening the dev tools
        self.openDevButton = tk.Button(self.homeScreen, text="Dev Tools", command=self.devScreen)
        self.openDevButton.pack()

        # ----------------------#

        # Room screen-----------#

        # create screen frame
        self.roomScreen = tk.Frame(self, width=400, height=600, bg="blue")
        self.roomScreen.pack(fill=None, expand=False)
        self.roomScreen.pack_forget()

        # add screen title
        self.roomTitle = tk.Label(self.roomScreen, text="Test Room", font=("Courier", 16))
        self.roomTitle.pack()

        # add back button
        self.back = tk.Button(self.roomScreen, text="Back")
        self.back["command"] = lambda homeScreen  = self.homeScreen : self.backButton(homeScreen)
        self.back.pack()

        # frame to hold the lights
        self.lightFrame = tk.Frame(self.roomScreen, bg="red", bd=2)
        self.lightFrame.pack()
        self.lightTitle = tk.Label(self.lightFrame, text="Lights")
        self.lightTitle.pack()
        # frame to hold the curtains
        self.curtainFrame = tk.Frame(self.roomScreen, bg="yellow", bd=2)
        self.curtainFrame.pack()
        self.curtainTitle = tk.Label(self.curtainFrame, text="Curtains")
        self.curtainTitle.pack()
        # frame to hold the sensors
        self.sensorFrame = tk.Frame(self.roomScreen, bg="green", bd=2)
        self.sensorFrame.pack()
        self.sensorTitle = tk.Label(self.sensorFrame, text="Sensors")
        self.sensorTitle.pack()

        # -------------------#

        # Settings for devices/sensors-----------#

        self.settingsWidgets = []
        self.settingsScreen = tk.Frame(self, width=400, height=600, bg="red")
        self.settingsScreen.pack_forget()
        # settings back button
        self.settingsBack = tk.Button(self.settingsScreen, text="Back")
        self.settingsBack["command"] = lambda roomScreen = self.roomScreen : self.backButton(roomScreen)
        self.settingsBack.pack()

        # Light settings frame-------------------#

        self.lightSettingsFrame = tk.Frame(self.settingsScreen, bg="blue")
        self.lightSettingsFrame.pack()
        self.lightSettingsFrame.pack_forget()

        # turn on and off
        self.activatedLabel = tk.Label(self.lightSettingsFrame, text="Activated")
        self.activatedLabel.pack()
        self.onCheck = tk.Checkbutton(self.lightSettingsFrame)
        self.onCheck.pack()

        # change the brightness
        self.brightnessLabel = tk.Label(self.lightSettingsFrame, text="Brightness")
        self.brightnessLabel.pack()
        self.brightness = tk.Scale(self.lightSettingsFrame, orient=tk.HORIZONTAL)
        self.brightness.pack()

        # change the colour
        self.lampColour = tk.Label(self.lightSettingsFrame, text="Light Colour")
        self.lampColour.pack()
        self.red = tk.Scale(self.lightSettingsFrame, label="Red", orient=tk.HORIZONTAL, to=255)
        self.red.pack()
        self.green = tk.Scale(self.lightSettingsFrame, label="Green", orient=tk.HORIZONTAL, to=255)
        self.green.pack()
        self.blue = tk.Scale(self.lightSettingsFrame, label="Blue", orient=tk.HORIZONTAL, to=255)
        self.blue.pack()


        # ---------------------------#

        # Sensor settings frame------------------------#

        self.sensorSettingFrame = tk.Frame(self.settingsScreen, bg="blue")
        # checkbox activated
        self.sensorLabel =tk.Label(self.sensorSettingFrame, text="Test")
        self.sensorLabel.pack(side="top",  pady=5)
        self.sensorCheckButton = tk.Checkbutton(self.sensorSettingFrame, text="Activated")
        self.sensorCheckButton.pack(side="top")
        # set sensor threshold to activate lights
        self.sensorThresLabel =tk.Label(self.sensorSettingFrame, text="Threshold to Activate")
        self.sensorThresLabel.pack(side="top",  pady=5)
        self.sensorThreshhold = tk.Scale(self.sensorSettingFrame, orient=tk.HORIZONTAL)
        self.sensorThreshhold.pack(side="top")

        # ---------------------------------------------#

        #Room Settings frame--------------------#

        self.roomSettingFrame = tk.Frame(self)
        self.day = tk.Scale(self.roomSettingFrame, label="day", orient=tk.HORIZONTAL, to=12)
        self.night = tk.Scale(self.roomSettingFrame, label="night", orient=tk.HORIZONTAL,to=24)
        self.night["from"] = 12

        #---------------------------------------#

        # Dev Screen----------------#

        self.devScreenFrame = tk.Frame(self)
        #backbutton
        self.devBack = tk.Button(self.devScreenFrame, text="Back")
        self.devBack["command"] = self.setHomeScreenRooms
        self.devBack.pack()
        #title label
        self.devLabel = tk.Label(self.devScreenFrame, text="Dev Screen")
        self.devLabel.pack()
        #button to add a room 
        self.addRoomButton = tk.Button(self.devScreenFrame, text="Add Room", command=self.addNewRoom)
        self.addRoomButton.pack()
        #entry for room name 
        self.roomNameLabel = tk.Label(self.devScreenFrame, text="New Room Name")
        self.roomNameLabel.pack()
        self.roomNameEntry = tk.Entry(self.devScreenFrame, textvariable=self.newRoomName)
        self.roomNameEntry.pack()
        
        #drop down to select a room
        self.selectRoomDropDown = tk.OptionMenu(self.devScreenFrame,self.selectedRoom,self.roomNames)
        self.selectRoomDropDown.pack()
        #button to add a new lamp, curtain, and the 3 sensors
        self.addLampButton = tk.Button(self.devScreenFrame, text="Add Lamp", command=self.addLamp)
        self.addLampButton.pack()
        self.addCurtainButton = tk.Button(self.devScreenFrame, text="Add Curtain", command=self.addCurtain)
        self.addCurtainButton.pack()
        self.addMotionSensorButton = tk.Button(self.devScreenFrame, text="Add Motion Sensor", command=self.addMotionSensor)
        self.addMotionSensorButton.pack()
        self.addLightSensorButton = tk.Button(self.devScreenFrame, text="Add Light Sensor", command=self.addLightSensor)
        self.addLightSensorButton.pack()
        self.addSoundSensorButton = tk.Button(self.devScreenFrame, text="Add Sound Sensor", command=self.addSoundSensor)
        self.addSoundSensorButton.pack()

        self.setTimeLabel= tk.Label(self.devScreenFrame, text="Set Time")
        self.setTimeLabel.pack()
        self.hourEdit = tk.Scale(self.devScreenFrame, label="Hour", orient=tk.HORIZONTAL, to=23)
        self.hourEdit["command"] = lambda value =1, timeType ="hour" : self.setTime(value, timeType)
        self.hourEdit.pack()
        self.minuteEdit = tk.Scale(self.devScreenFrame, label="Minute", orient=tk.HORIZONTAL, to=59)
        self.minuteEdit["command"] = lambda value =1, timeType ="minute" : self.setTime(value, timeType)
        self.minuteEdit.pack()
        self.printButton = tk.Button(self.devScreenFrame, text="Print Room Data", command=self.printAllRooms)
        self.printButton.pack()

        # --------------------------#
    #displays all rooms
    def printAllRooms(self):
        for room in self.rooms:
            print(room)
    
    #
    def setTime(self, value, timeType):
        value = int(value)
        if timeType == "minute":
            self.time = self.time.replace(minute=value)
        else:
            self.time = self.time.replace(hour=value)
        print(self.time)
    def addNewRoom(self):
        #got help from https://www.youtube.com/watch?v=XNL8veoNTC0
        name = self.newRoomName.get()
        self.rooms.append(Room(name))
        self.roomNames.append(name)
        self.newRoomName.set("")
        self.selectRoomDropDown.children["menu"].delete(0,"end")
        for room in self.roomNames:
            self.selectRoomDropDown.children["menu"].add_command(label=room,command = lambda name=room: self.selectedRoom.set(name))

    def addLightSensor(self):
        room = self.findRoom()
        if room != None:
            newSensor = LightSensor.LightSensor(str(len(room.lightSensors)+1))
            room.lightSensors.append(newSensor)
    def addSoundSensor(self):
        room = self.findRoom()
        if room != None:
            newSensor = SoundSensor.SoundSensor(str(len(room.soundSensors)+1))
            room.soundSensors.append(newSensor)
    def addMotionSensor(self):
        room = self.findRoom()
        if room != None:
            newSensor = MotionSensor.MotionSensor(str(len(room.motionSensors)+1))
            room.motionSensors.append(newSensor)
    def addLamp(self):
        room = self.findRoom()
        if room != None:
            newSensor = Lamp.Lamp(str(len(room.lamps)+1))
            room.lamps.append(newSensor)
    def addCurtain(self):
        room = self.findRoom()
        if room != None:
            newSensor = Curtain.Curtain(str(len(room.curtains)+1))
            room.curtains.append(newSensor)
    def setHomeScreenRooms(self):
        self.removeWidgets(self.roomList)
        self.backButton(self.homeScreen)
        # add room list
        for room in self.rooms:
            self.addRoom(room)
    def addRoom(self, room):
        self.roomButton = tk.Button(self.roomFrame, text=room.name)
        self.roomButton["command"] = lambda arg1=room: self.openRoom(arg1)
        self.roomButton.pack(side="top", padx=2, pady=10)
        self.roomList.append(self.roomButton)

    def backButton(self, screen):
        self.hideAllScreens()
        # show homescreen
        screen.pack()

    def settingsBackButton(self):
        self.hideAllScreens()
        self.roomScreen.pack()

    def devScreen(self):
        self.hideAllScreens()
        self.devScreenFrame.pack()
        self.hourEdit.set(self.time.hour)
        self.minuteEdit.set(self.time.minute)
        
    def openRoom(self, room):
        self.hideAllScreens()
        self.roomScreen.pack(fill=None, expand=False)
        self.roomTitle["text"] = room.name
        self.removeWidgets(self.roomInfo)
        self.checkBoxVars = None
        self.checkBoxVars = []
        # Display the lamps
        for lamp in room.lamps:
            lightHold = tk.Frame(self.lightFrame)
            lightHold.pack()
            lampLabel = tk.Label(lightHold, text=lamp.id)
            lampLabel.pack(side="left")
            lampColour = tk.Label(lightHold, text="Colour: " + str(lamp.colour))
            lampColour.pack(side="left")
            lampBrightness = tk.Label(lightHold, text="Brightness: " + str(lamp.brightness))
            lampBrightness.pack(side="left")
            self.checkBoxVars.append(tk.IntVar())
            lampOn = tk.Checkbutton(lightHold, text="On", variable=self.checkBoxVars[len(self.checkBoxVars)-1] )
            if lamp.activated:
                lampOn.select()
            #lampOn["command"] = lambda arg1=lampOn.get: self.lightSettings(arg1)
            lampSettings = tk.Button(lightHold, text="Edit")  # ,image= settingsImage )
            lampOn.pack(side="left")
            lampSettings["command"] = lambda arg1=lamp: self.lightSettings(arg1)
            lampSettings.pack(side="left")

            self.roomInfo.append(lampOn)
            self.roomInfo.append(lightHold)
        # Display the curtains
        for curtain in room.curtains:
            curtainHold = tk.Frame(self.curtainFrame)
            curtainHold.pack()
            curtainLabel = tk.Label(curtainHold, text=curtain.id)
            curtainLabel.pack(side="left")
            self.checkBoxVars.append(tk.IntVar(curtainHold))
            curtainOpen = tk.Checkbutton(curtainHold, text="Closed", variable=self.checkBoxVars[len(self.checkBoxVars)-1])
            if curtain.closed:
                curtainOpen.select()
            curtainOpen["command"] = lambda value=self.checkBoxVars[len(self.checkBoxVars)-1].get(): curtain.setClosed(value)
            self.checkBoxVars[len(self.checkBoxVars)-1].get()
            #print(self.checkBoxVars)
            curtainOpen.pack()
            self.roomInfo.append(curtainOpen)
            del curtainOpen
            self.roomInfo.append(curtainHold)

        # Display the sensors
        for sensor in room.getAllSensors():
            sensorHold = tk.Frame(self.sensorFrame)
            sensorHold.pack()
            sensorLabel = tk.Label(sensorHold, text=sensor.NAME + " " + sensor.id)
            sensorLabel.pack(side="left")
            sensorData = tk.Label(sensorHold, text="Value: " + str(sensor.getReading()))
            sensorData.pack(side="left")
            sensorSettings = tk.Button(sensorHold, text="Edit")
            sensorSettings["command"] = lambda curSensor=sensor: self.sensorSettings(curSensor)
            sensorSettings.pack()
            self.roomInfo.append(sensorHold)
        # add the same for sensors

    def sensorSettings(self, sensor):
        # change activation threshold
        self.hideAllScreens()
        # show settings screen & light settings
        self.settingsScreen.pack()
        self.sensorSettingFrame.pack()
        
        if sensor.activated:#check buttons my mortal enemy
            self.sensorCheckButton.select()
        self.sensorThreshhold["to"] = sensor.MAX
        self.sensorThreshhold.set(sensor.thresh)
        self.sensorThreshhold["command"] = sensor.setThreshhold




    def lightSettings(self, light):
        # hide the other screen
        self.hideAllScreens()
        # show settings screen & light settings
        self.settingsScreen.pack()
        self.lightSettingsFrame.pack()
        #show light's current settings
        if light.activated:
                self.onCheck.select()
        #self.checkOn["command"]= lambda value=1:light.setActivated(value,colour)
        self.brightness.set(light.brightness)
        self.brightness["command"] = light.setBrightness
        
        self.red["command"] = lambda value=1,colour = 0:light.editColour(value,colour) #the value var gets replaced with the value from the scale
        self.red.set(light.colour[0])

        self.green["command"] = lambda value=1,colour = 1:light.editColour(value,colour) #the colour responds to the RGB position
        self.green.set(light.colour[1])

        self.blue["command"] = lambda value=1,colour = 2:light.editColour(value,colour)
        self.blue.set(light.colour[2])

    #hides every screen 
    def hideAllScreens(self):
        self.homeScreen.pack_forget()
        self.roomScreen.pack_forget()
        self.settingsScreen.pack_forget()
        self.lightSettingsFrame.pack_forget()
        self.sensorSettingFrame.pack_forget()
        self.devScreenFrame.pack_forget()
        # & curtain

    #deletes all widgets from an array
    def removeWidgets(self, widgetArray):
        for wid in widgetArray:
            wid.destroy()
        widgetArray.clear()
    #find a room with a name
    def findRoom(self):
        for room in self.rooms:
            selectRoom = self.selectedRoom.get()
            if room.name == selectRoom:
                return room
    #loop for checking each sensor in a room
    def checkRooms(self):
        for room in self.rooms:
            room.checkSensors(self.time)
            
    #Saving data of room to file
    def saveData(self):
        with open('savedData.txt', 'w') as save_data:
            for i in self.rooms:
                #Saving room name
                save_data.write("Room Name: ")
                save_data.write(i.name)
                save_data.write('\n')

                #Saving the lamp ID's
                save_data.write("Lamp ID's: ")

                for j in i.lamps:
                    save_data.write(str(j.getID()))
                    save_data.write(', ')

                #Saving the curtain ID's
                save_data.write('\n')
                save_data.write("Curtain ID's: ")

                for j in i.curtains:
                    save_data.write(str(j.getID()))
                    save_data.write(', ')

                #Saving the light sensor ID's
                save_data.write('\n')
                save_data.write("Light Sensor ID's: ")

                for j in i.lightSensors:
                    save_data.write(str(j.getID()))
                    save_data.write(', ')
            
                #Saving the sound sensor ID's
                save_data.write('\n')
                save_data.write("Sound Sensor ID's: ")

                for j in i.soundSensors:
                    save_data.write(str(j.getID()))
                    save_data.write(', ')

                #Saving the motion sensor ID's
                save_data.write('\n')
                save_data.write("Motion Sensor ID's: ")

                for j in i.motionSensors:
                    save_data.write(str(j.getID()))
                    save_data.write(', ')

    #Reading data from file 
    def readData(self):
        with open('savedData.txt', 'r') as read_Data:
            lines = read_Data.readlines()

            #Getting the room name from the first line and removing everything except the name
            tempRoomName = ""
            newRoomName = ""

            tempRoomName = lines[0]
            newRoomName = tempRoomName[11:]

            newRoom = Room(newRoomName)

            #Reading all the lamp ID's from the file and creating lamps
            tempLamps = lines[1]

            for i in tempLamps:
                if i.isdigit():
                    newLamp = Lamp.Lamp(i)
                    newRoom.lamps.append(newLamp)
            
            #Reading all the curtain ID's from the file and creating curtains
            tempCurtains = lines[2]

            for i in tempCurtains:
                if i.isdigit():
                    newCurtain = Curtain.Curtain(i)
                    newRoom.curtains.append(newCurtain)
            
            #Reading all the light sensor ID's and creating light sensors
            tempLightSens = lines[3]

            for i in tempLightSens:
                if i.isdigit():
                    newLightSens = LightSensor.LightSensor(i)
                    newRoom.lightSensors.append(newLightSens)

            #Reading all the sound sensor ID's and creating sound sensors
            tempSoundSens = lines[4]

            for i in tempSoundSens:
                if i.isdigit():
                    newSoundSens = SoundSensor.SoundSensor(i)
                    newRoom.soundSensors.append(newSoundSens)        
            
            #Reading all the motion sensor ID's and creating motion sensors
            tempMotionSens = lines[5]

            for i in tempMotionSens:
                if i.isdigit():
                    newMotionSens = MotionSensor.MotionSensor(i)
                    newRoom.motionSensors.append(newMotionSens)
            print(newRoom)
        

            