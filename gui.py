import tkinter as tk

import Sensors.LightSensor
from Room import Room

from openpyxl import load_workbook

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
        self.create_widgets()

    def create_widgets(self):

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

    def addRoom(self, room):
        self.roomButton = tk.Button(self.roomFrame, text=room.name)
        self.roomButton["command"] = lambda arg1=room: self.openRoom(arg1)
        self.roomButton.pack(side="top", padx=2, pady=10)
        self.roomList.append(self.roomButton)

    def backButton(self):
        self.roomScreen.pack_forget()
        self.homeScreen.pack()

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
            lampColour = tk.Label(lightHold, text="Colour: " + str(lamp.colour))
            lampColour.pack(side="left")
            lampBrightness = tk.Label(lightHold, text="Brightness: " + str(lamp.brightness))
            lampBrightness.pack(side="left")
            lampOn = lampButton = tk.Checkbutton(lightHold, text="On")
            lampOn.pack(side="left")
            # lampButton = tk.Checkbutton(self.lightFrame, text=lamp)
            # lampButton.pack(side="top")
            # self.roomInfo.append(lightHold)
            self.roomInfo.append(lightHold)
        for curtain in room.curtains:
            meep = 1
        for sensor in room.sensors:
            sensorHold = tk.Frame(self.sensorFrame)
            sensorHold.pack()
            sensorLabel = tk.Label(sensorHold, text=sensor.NAME + " " + sensor.id)
            sensorLabel.pack(side="left")
            sensorData = tk.Label(sensorHold, text="Value: " + str(sensor.getReading()))
            sensorData.pack(side="left")

            self.roomInfo.append(sensorHold)
        # add the same for sensors

    def removeWidgets(self, widgetArray):
        for wid in widgetArray:
            wid.destroy()
        widgetArray.clear()


rooms = []


def createSensors(noOfLight, noOfMotion, noOfSound):
    lightSensors = []
    motionSensors = []
    soundSensors = []
    for i in range(noOfLight):
        lightSensors.append(Sensors.LightSensor.LightSensor(str(i)))
    for i in range(noOfMotion):
        motionSensors.append(Sensors.MotionSensor.MotionSensor(str(i)))
    for i in range(noOfSound):
        soundSensors.append(Sensors.SoundSensor.SoundSensor(str(i)))

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

    rooms.append(Room(lamps, curtainss, lightSensors, soundSensors, motionSensors, roomName))


root = tk.Tk()
app = Application(rooms, master=root)
app.mainloop()
