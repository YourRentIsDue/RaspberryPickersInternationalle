import tkinter as tk
import datetime
from Room import Room
from Sensors import *
from Devices import *
from openpyxl import load_workbook


class Application(tk.Frame):
    def __init__(self, rooms, master=None):
        super().__init__(master)
        self.rooms = rooms
        self.time = datetime.datetime.now()
        self.customTime = False  # if true then will use time set in dev tools, else use actual current time
        # self.time = self.time.replace(hour=14)

        # set size
        self.master.minsize(400, 600)

        # holds the widgets for the rooms
        self.roomList = []
        self.roomInfo = []
        self.checkBoxVars = []

        # Used for room list in dev tools
        self.roomNames = []
        for room in rooms:
            self.roomNames.append(room.name)
        self.selectedRoom = tk.StringVar()
        self.selectedRoom.set(self.roomNames[0])
        self.newRoomName = tk.StringVar()

        self.pack()
        self.createWidgets()
        # starts the homescreen
        self.setHomeScreenRooms()

        # function that starts a loop to check the sensors
        self.after(2000, self.checkRooms)

        # unfinished
        # self.readData()

    def createWidgets(self):

        # Home screen----------#

        # create home frame
        self.homeScreen = tk.Frame(self, width=400, height=600, bg="gray50")
        self.homeScreen.pack()

        # add home screen title
        self.title = tk.Label(self.homeScreen, text="Eco Friendly Sensors", font=("Helvetica", 16), bg="gray50")
        self.title.pack(side="top", pady=5)

        # create frame to hold rooms
        self.roomFrame = tk.Frame(self.homeScreen, bg="gray40", height=20, width=50, bd=2)
        self.roomFrame.pack(padx=20, pady=20)

        # room settings button
        self.roomSettingsButton = tk.Button(self.homeScreen, text="Room Settings", command=self.roomSettings)
        self.roomSettingsButton.pack()

        # button for opening the dev tools
        self.openDevButton = tk.Button(self.homeScreen, text="Dev Tools", command=self.devScreen)
        self.openDevButton.pack()

        # ----------------------#

        # Room screen-----------#

        # create screen frame
        self.roomScreen = tk.Frame(self, width=400, height=600, bg="gray50")
        self.roomScreen.pack(fill=None, expand=False)
        self.roomScreen.pack_forget()

        # add screen title
        self.roomTitle = tk.Label(self.roomScreen, text="Test Room", font=("Helvetica", 16), bg="gray50")
        self.roomTitle.pack()

        # add back button
        self.back = tk.Button(self.roomScreen, text="Back")
        self.back["command"] = lambda homeScreen=self.homeScreen: self.backButton(homeScreen)
        self.back.pack()

        # frame to hold the lights
        self.lightFrame = tk.Frame(self.roomScreen, bg="gray50", bd=2)
        self.lightFrame.pack()
        self.lightTitle = tk.Label(self.lightFrame, text="Lights")
        self.lightTitle.pack()
        # frame to hold the curtains
        self.curtainFrame = tk.Frame(self.roomScreen, bg="gray50", bd=2)
        self.curtainFrame.pack()
        self.curtainTitle = tk.Label(self.curtainFrame, text="Curtains")
        self.curtainTitle.pack()
        # frame to hold the sensors
        self.sensorFrame = tk.Frame(self.roomScreen, bg="gray50", bd=2)
        self.sensorFrame.pack()
        self.sensorTitle = tk.Label(self.sensorFrame, text="Sensors")
        self.sensorTitle.pack()

        # -------------------#

        # Settings for devices/sensors-----------#

        self.settingsWidgets = []
        self.settingsScreen = tk.Frame(self, width=400, height=600, bg="gray50")
        self.settingsScreen.pack_forget()
        # settings back button
        self.settingsBack = tk.Button(self.settingsScreen, text="Back")
        self.settingsBack["command"] = lambda roomScreen=self.roomScreen: self.backButton(roomScreen)
        self.settingsBack.pack()

        # Light settings frame-------------------#

        self.lightSettingsFrame = tk.Frame(self.settingsScreen, bg="gray50")
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

        self.sensorSettingFrame = tk.Frame(self.settingsScreen, bg="gray50")
        # checkbox activated
        self.sensorLabel = tk.Label(self.sensorSettingFrame, text="Test")
        self.sensorLabel.pack(side="top", pady=5)
        self.sensorCheckButton = tk.Checkbutton(self.sensorSettingFrame, text="Activated")
        self.sensorCheckButton.pack(side="top")
        # set sensor threshold to activate lights
        self.sensorThresLabel = tk.Label(self.sensorSettingFrame, text="Threshold to Activate")
        self.sensorThresLabel.pack(side="top", pady=5)
        self.sensorThreshhold = tk.Scale(self.sensorSettingFrame, orient=tk.HORIZONTAL)
        self.sensorThreshhold.pack(side="top")

        # ---------------------------------------------#

        # Room Settings frame--------------------#

        self.roomSettingFrame = tk.Frame(self)
        self.roomSetBack = tk.Button(self.roomSettingFrame, text="Back")
        self.roomSetBack["command"] = self.setHomeScreenRooms
        self.roomSetBack.pack()
        self.day = tk.Scale(self.roomSettingFrame, label="Day Start", orient=tk.HORIZONTAL, to=11)
        self.day["command"] = lambda value=1, timeOfDay="day": self.changeRoomTimes(value, timeOfDay)
        self.day.pack()

        self.night = tk.Scale(self.roomSettingFrame, label="Night Start", orient=tk.HORIZONTAL, to=23)
        self.night["command"] = lambda value=1, timeOfDay="night": self.changeRoomTimes(value, timeOfDay)
        self.night.pack()
        self.night["from"] = 12

        # ---------------------------------------#

        # Dev Screen----------------#

        self.devScreenFrame = tk.Frame(self, bg="gray50")
        # backbutton
        self.devBack = tk.Button(self.devScreenFrame, text="Back")
        self.devBack["command"] = self.setHomeScreenRooms
        self.devBack.pack()
        # title label
        self.devLabel = tk.Label(self.devScreenFrame, text="Dev Screen", bg="gray50")
        self.devLabel.pack()
        # button to add a room
        self.addRoomButton = tk.Button(self.devScreenFrame, text="Add Room", command=self.addNewRoom)
        self.addRoomButton.pack()
        # entry for room name
        self.roomNameLabel = tk.Label(self.devScreenFrame, text="New Room Name", bg="gray50")
        self.roomNameLabel.pack()
        self.roomNameEntry = tk.Entry(self.devScreenFrame, textvariable=self.newRoomName, borderwidth=5)
        self.roomNameEntry.pack()

        # drop down to select a room
        self.selectRoomDropDown = tk.OptionMenu(self.devScreenFrame, self.selectedRoom, self.roomNames)
        self.selectRoomDropDown.pack()
        # button to add a new lamp, curtain, and the 3 sensors
        self.addLampButton = tk.Button(self.devScreenFrame, text="Add Lamp", command=self.addLamp)
        self.addLampButton.pack()
        self.addCurtainButton = tk.Button(self.devScreenFrame, text="Add Curtain", command=self.addCurtain)
        self.addCurtainButton.pack()
        self.addMotionSensorButton = tk.Button(self.devScreenFrame, text="Add Motion Sensor",
                                               command=self.addMotionSensor)
        self.addMotionSensorButton.pack()
        self.addLightSensorButton = tk.Button(self.devScreenFrame, text="Add Light Sensor", command=self.addLightSensor)
        self.addLightSensorButton.pack()
        self.addSoundSensorButton = tk.Button(self.devScreenFrame, text="Add Sound Sensor", command=self.addSoundSensor)
        self.addSoundSensorButton.pack()

        self.setTimeLabel = tk.Label(self.devScreenFrame, text="Set Time", background="gray50")
        self.setTimeLabel.pack()
        self.hourEdit = tk.Scale(self.devScreenFrame, label="Hour", orient=tk.HORIZONTAL, to=23, background="gray60")
        self.hourEdit["command"] = lambda value=1, timeType="hour": self.setTime(value, timeType)
        self.hourEdit.pack()
        self.minuteEdit = tk.Scale(self.devScreenFrame, label="Minute", orient=tk.HORIZONTAL, to=59,
                                   background="gray60")
        self.minuteEdit["command"] = lambda value=1, timeType="minute": self.setTime(value, timeType)
        self.minuteEdit.pack()
        self.printButton = tk.Button(self.devScreenFrame, text="Print Room Data", command=self.printAllRooms)
        self.printButton.pack(pady=2)

        # --------------------------#

    # displays all rooms
    def printAllRooms(self):
        for room in self.rooms:
            print(room)

    #
    def setTime(self, value, timeType):
        self.customTime = True
        value = int(value)
        if timeType == "minute":
            self.time = self.time.replace(minute=value)
        else:
            self.time = self.time.replace(hour=value)
        # print(self.time)

    def addNewRoom(self):
        # got help from https://www.youtube.com/watch?v=XNL8veoNTC0
        name = self.newRoomName.get()
        self.rooms.append(Room(name))
        self.roomNames.append(name)
        self.newRoomName.set("")
        self.selectRoomDropDown.children["menu"].delete(0, "end")
        for room in self.roomNames:
            self.selectRoomDropDown.children["menu"].add_command(label=room,
                                                                 command=lambda name=room: self.selectedRoom.set(name))

    def changeRoomTimes(self, value, timeOfDay):
        if timeOfDay == "day":
            for room in self.rooms:
                room.setNightTimeEnd(value)
        elif timeOfDay == "night":
            for room in self.rooms:
                room.setNightTimeStart(value)

    def addLightSensor(self):
        room = self.findRoom()
        if room is not None:
            newSensor = LightSensor.LightSensor(str(len(room.lightSensors) + 1))
            room.lightSensors.append(newSensor)

    def addSoundSensor(self):
        room = self.findRoom()
        if room is not None:
            newSensor = SoundSensor.SoundSensor(str(len(room.soundSensors) + 1))
            room.soundSensors.append(newSensor)

    def addMotionSensor(self):
        room = self.findRoom()
        if room is not None:
            newSensor = MotionSensor.MotionSensor(str(len(room.motionSensors) + 1))
            room.motionSensors.append(newSensor)

    def addLamp(self):
        room = self.findRoom()
        if room is not None:
            newSensor = Lamp.Lamp(str(len(room.lamps) + 1))
            room.lamps.append(newSensor)

    def addCurtain(self):
        room = self.findRoom()
        if room is not None:
            newSensor = Curtain.Curtain(str(len(room.curtains) + 1))
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
        # save all rooms information
        self.saveData()
        self.hideAllScreens()
        # show homescreen
        screen.pack()

    def settingsBackButton(self):
        self.hideAllScreens()
        self.roomScreen.pack()

    def roomSettings(self):
        self.hideAllScreens()
        self.roomSettingFrame.pack()
        if len(self.rooms) > 0:
            self.night.set(self.rooms[0].nightTimeStart)
            self.day.set(self.rooms[0].nightTimeEnd)

    def devScreen(self):
        self.hideAllScreens()
        self.devScreenFrame.pack()
        self.hourEdit.set(self.time.hour)
        self.minuteEdit.set(self.time.minute)

    def openRoom(self, room):
        self.checkRooms()
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
            lampOn = tk.Checkbutton(lightHold, text="On", variable=self.checkBoxVars[len(self.checkBoxVars) - 1])
            if lamp.activated:
                lampOn.select()
            # lampOn["command"] = lambda arg1=lampOn.get: self.lightSettings(arg1)
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
            curtainOpen = tk.Checkbutton(curtainHold, text="Closed",
                                         variable=self.checkBoxVars[len(self.checkBoxVars) - 1])
            if curtain.closed:
                curtainOpen.select()
            curtainOpen["command"] = lambda \
                    value=self.checkBoxVars[len(self.checkBoxVars) - 1].get(): curtain.setClosed(value)
            self.checkBoxVars[len(self.checkBoxVars) - 1].get()
            # print(self.checkBoxVars)
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

        if sensor.activated:  # check buttons my mortal enemy
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
        # show light's current settings
        if light.activated:
            self.onCheck.select()
        # self.checkOn["command"]= lambda value=1:light.setActivated(value,colour)
        self.brightness.set(light.brightness)
        self.brightness["command"] = light.setBrightness

        self.red["command"] = lambda value=1, colour=0: light.editColour(value,
                                                                         colour)  # the value var gets replaced with
        # the value from the scale
        self.red.set(light.colour[0])

        self.green["command"] = lambda value=1, colour=1: light.editColour(value,
                                                                           colour)  # the colour responds to the RGB
        # position
        self.green.set(light.colour[1])

        self.blue["command"] = lambda value=1, colour=2: light.editColour(value, colour)
        self.blue.set(light.colour[2])

    # hides every screen
    def hideAllScreens(self):
        self.homeScreen.pack_forget()
        self.roomScreen.pack_forget()
        self.settingsScreen.pack_forget()
        self.lightSettingsFrame.pack_forget()
        self.sensorSettingFrame.pack_forget()
        self.devScreenFrame.pack_forget()
        self.roomSettingFrame.pack_forget()
        # & curtain

    # deletes all widgets from an array
    def removeWidgets(self, widgetArray):
        for wid in widgetArray:
            wid.destroy()
        widgetArray.clear()

    # find a room with a name
    def findRoom(self):
        for room in self.rooms:
            selectRoom = self.selectedRoom.get()
            if room.name == selectRoom:
                return room

    # loop for checking each sensor in a room
    def checkRooms(self):
        for room in self.rooms:
            if self.customTime:
                room.checkSensors(self.time)
            else:
                room.checkSensors(datetime.datetime.now())
        # keep checking sensors every 2 secs
        self.after(2000, self.checkRooms)

        # Saving data of room to file

    def saveData(self):
        wb = load_workbook('test.xlsx')
        sheet = wb.active
        counter = 1
        for room in self.rooms:
            column = chr(65 + counter + 1)
            counter += 1
            anotherCounter = 0
            for lamp in room.lamps:
                sheet[column + str(9 + anotherCounter * 13)] = lamp.getBrightness()
                sheet[column + str(10 + anotherCounter * 13)] = lamp.colour[0]
                sheet[column + str(11 + anotherCounter * 13)] = lamp.colour[1]
                sheet[column + str(12 + anotherCounter * 13)] = lamp.colour[2]
                anotherCounter += 1

        try:
            wb.save(filename="test.xlsx")  # Tries to save the file as "test.xlsx"
        except PermissionError:  # If it encounters a Permission Error, the file is almost certainly open
            print(
                "There was an error generating the data storage file, perhaps an old instance of the file is already "
                "open?")

    def loadData(self):
        # Incomplete
        return None

