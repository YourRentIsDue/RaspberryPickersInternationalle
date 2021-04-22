import tkinter as tk

import Sensors.LightSensor
from Room import Room

from openpyxl import Workbook

from random import randint
from Sensors import LightSensor, MotionSensor, SoundSensor
from Devices import Curtain, Lamp


class Application(tk.Frame):
    def __init__(self, rooms, master=None):
        super().__init__(master)
        self.rooms = rooms

        self.master = master
        self.master.minsize(400, 600)
        self.roomList = []
        self.roomInfo = []
        self.pack()
        self.createWidgets()

    def createWidgets(self):

        # Home screen----------#

        # create home frame
        self.homeScreen = tk.Frame(self, width=400, height=600, bg="red")
        self.homeScreen.pack()

        # add home screen title
        self.title = tk.Label(self.homeScreen, text="Title App", font=("Courier", 16))
        self.title.pack(side="top", pady=5)

        # create frame to hold rooms
        self.roomFrame = tk.Frame(self.homeScreen, bg="blue", height=20, width=50, bd=2)
        self.roomFrame.pack(padx=20, pady=20)

        # add room list
        for room in self.rooms:
            self.addRoom(room)

        # ----------------------#

        # Room screen-----------#

        # create screen frame
        self.roomScreen = tk.Frame(self, width=400, height=600, bg="blue")
        self.roomScreen.pack(fill=None, expand=False)
        self.roomScreen.pack_forget()

        # add screen title
        self.roomTitle = tk.Label(self.roomScreen, text="Test", font=("Courier", 16))
        self.roomTitle.pack()

        # add back button
        self.back = tk.Button(self.roomScreen, text="Back", command=self.backButton)
        self.back.pack()

        # frame to hold the lights
        self.lightFrame = tk.Frame(self.roomScreen, bg="red", bd=2)
        self.lightFrame.pack()
        self.lightTitle = tk.Label(self.lightFrame, text="Lights")
        self.lightTitle.pack()

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
        self.settingsBack = tk.Button(self.settingsScreen, text="Back", command=self.settingsBackButton)
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

        #Curtain Settings frame-----------#

        self.curtainSettingFrame = tk.Frame(self.settingsScreen,bg="blue")

        #open/closed check box
        self.curtainCheckButton = tk.Checkbutton(self.sensorSettingFrame,text="open")
        self.curtainCheckButton.pack()
        #---------------------------------#

        #Sensor settings frame------------------------#

        self.sensorSettingFrame = tk.Frame(self.settingsScreen,bg="blue")
        #checkbox activated
        self.sensorCheckButton = tk.Checkbutton(self.sensorSettingFrame)
        self.sensorCheckButton.pack()
        #inputbox for sensor threshhold
        self.sensorThreshhold = tk.Entry(self.sensorSettingFrame,label="Threshhold")
        self.sensorThreshhold.pack()


        #---------------------------------------------#
        

        # ---------------------------------------#

    def addRoom(self, room):
        self.roomButton = tk.Button(self.roomFrame, text=room.name)
        self.roomButton["command"] = lambda arg1=room: self.openRoom(arg1)
        self.roomButton.pack(side="top", padx=2, pady=10)
        self.roomList.append(self.roomButton)

    def backButton(self):
        self.hideAllScreens()
        # show homescreen
        self.homeScreen.pack()

    def settingsBackButton(self):
        self.hideAllScreens()
        self.roomScreen.pack()

    def openRoom(self, room):
        self.homeScreen.pack_forget()
        self.roomScreen.pack(fill=None, expand=False)
        self.roomTitle["text"] = room.name
        self.removeWidgets(self.roomInfo)
        self.removeWidgets
        for lamp in room.lamps:
            lightHold = tk.Frame(self.lightFrame)
            lightHold.pack()
            lampLabel = tk.Label(lightHold, text=lamp.id)
            lampLabel.pack(side="left")
            lampColour = tk.Label(lightHold, text="Colour: "+str(lamp.colour))
            lampColour.pack(side="left")
            lampBrightness = tk.Label(lightHold, text="Brightness: "+str(lamp.brightness))
            lampBrightness.pack(side="left")
            lampOn = tk.Checkbutton(lightHold, text="On", variable=lamp.activated)
            if lamp.activated: 
                lampOn.select()
            lampOn.pack(side="left")
            self.roomInfo.append(lampOn)
            del lampOn

            self.roomInfo.append(lightHold)
        for curtain in room.curtains:
            meep =1
        for sensor in room.sensors:
            sensorHold = tk.Frame(self.sensorFrame)
            sensorHold.pack()
            sensorLabel = tk.Label(sensorHold, text= sensor.NAME+" "+sensor.id)
            sensorLabel.pack(side="left")
            sensorData = tk.Label(sensorHold, text="Value: "+str(sensor.getReading()))
            sensorData.pack(side="left")
            #settingsImage = tk.PhotoImage(file=r"Resources/gear.png")
            sensorSettings = tk.Button(sensorHold,text="edit")#,image= settingsImage )
            sensorSettings["command"] = lambda arg1=sensor : self.lightSettings(arg1)
            sensorSettings.pack()
            self.roomInfo.append(sensorHold)
        #add the same for sensors
    
    def sensorSettings(self, sensor):
        #change activation threshold
        self.hideAllScreens()
        #show settings screen & light settings
        self.settingsScreen.pack()
        self.sensorSettingFrame().pack()
        print(1)
    def curtainSettings(self, curtain):
        self.hideAllScreens()

    def lightSettings(self, light):
        # hide the other screen
        self.hideAllScreens()
        # show settings screen & light settings
        self.settingsScreen.pack()
        self.lightSettingsFrame.pack()

    def hideAllScreens(self):
        self.homeScreen.pack_forget()
        self.roomScreen.pack_forget()
        self.settingsScreen.pack_forget()
        self.lightSettingsFrame.pack_forget()
        self.sensorSettingFrame.pack_forget()
        #& curtain

    def removeWidgets(self, widgetArray):
        for wid in widgetArray:
            wid.destroy()
        widgetArray.clear()


rooms = []

wb = Workbook()
sheet = wb.active


def createSensors(noOfLight, noOfMotion, noOfSound):
    lightSensors = []
    motionSensors = []
    soundSensors = []

    for i in range(noOfLight):
        lightSensors.append(Sensors.LightSensor.LightSensor(str(i + 1)))
    for i in range(noOfMotion):
        motionSensors.append(Sensors.MotionSensor.MotionSensor(str(i + 1)))
    for i in range(noOfSound):
        soundSensors.append(Sensors.SoundSensor.SoundSensor(str(i + 1)))

    if noOfLight > noOfMotion and noOfLight > noOfSound:
        biggest = noOfLight
    else:
        if noOfMotion > noOfLight and noOfMotion > noOfSound:
            biggest = noOfMotion
        else:
            biggest = noOfSound

    sheet['A1'] = "Room name:"

    counter = 2

    for i in range(biggest):
        sheet['A' + str(counter)] = "Light sensor ID:"
        counter += 1
        sheet['A' + str(counter)] = "Light level in lux:"
        counter += 1
        sheet['A' + str(counter)] = "Sound sensor ID:"
        counter += 1
        sheet['A' + str(counter)] = "Volume in dB:"
        counter += 1
        sheet['A' + str(counter)] = "Motion sensor ID:"
        counter += 1
        sheet['A' + str(counter)] = "Motion:"
        counter += 1
        sheet['A' + str(counter)] = ""
        counter += 1

    return lightSensors, motionSensors, soundSensors


def createDevices(noOfLamps, noOfCurtains):
    lamps = []
    curtainss = []
    for i in range(noOfLamps):
        lamps.append(str(i))
    for i in range(noOfCurtains):
        curtainss.append(str(i))

    return lamps, curtainss


def createRoom(noOfLight, noOfMotion, noOfSound, noOfLamps, noOfCurtains, roomName):
    lightSensors, motionSensors, soundSensors = createSensors(noOfLight, noOfMotion, noOfSound)
    lamps, curtainss = createDevices(noOfLamps, noOfCurtains)

    for lS in lightSensors:
        lS.setValue(randint(500, 1000))
        lS.setLocation(roomName)

    for mS in motionSensors:
        mS.setValue(randint(0, 100))
        mS.setLocation(roomName)

    for sS in soundSensors:
        sS.setValue(randint(30, 100))  # 100 dBs is really fucking loud, Calum
        sS.setLocation(roomName)

    rooms.append(Room(lamps, curtainss, lightSensors, soundSensors, motionSensors, roomName))

    column = chr(65 + len(rooms) + 1)

    sheet[column + str(1)] = roomName

    counter = 0

    for lS in lightSensors:
        sheet[column + str(2 + counter * 7)] = lS.getID()
        sheet[column + str(3 + counter * 7)] = lS.getReading()
        counter += 1

    counter = 0

    for sS in soundSensors:
        sheet[column + str(4 + counter * 7)] = sS.getID()
        sheet[column + str(5 + counter * 7)] = sS.getReading()
        counter += 1

    counter = 0

    for mS in motionSensors:
        sheet[column + str(6 + counter * 7)] = mS.getID()
        sheet[column + str(7 + counter * 7)] = mS.getValue()
        counter += 1

    try:
        wb.save(filename="text.xlsx")
    except PermissionError:
        print("There was an error generating the data storage file, perhaps an old instance of the file is already "
              "open?")


createRoom(2, 1, 1, 1, 1, "test")

root = tk.Tk()
app = Application(rooms, master=root)
app.mainloop()
