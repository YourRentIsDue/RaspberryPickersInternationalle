import tkinter as tk


class Application(tk.Frame):
    def __init__(self, rooms, master=None):
        super().__init__(master)
        self.rooms = rooms

        self.master = master
        self.master.minsize(400, 600)
        self.roomList = []
        self.roomInfo = []
        self.checkBoxVars = []
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

        # Curtain Settings frame-----------#

        self.curtainSettingFrame = tk.Frame(self.settingsScreen, bg="blue")

        self.curtainSettingFrame = tk.Frame(self.settingsScreen, bg="blue")

        # open/closed check box
        self.curtainCheckButton = tk.Checkbutton(self.curtainSettingFrame, text="open")
        self.curtainCheckButton.pack()
        # ---------------------------------#

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

        # Dev Screen----------------#
        self.devScreenFrame = tk.Frame(self)
        #button to open it
        #title label
        self.devLabel = tk.Label(self.devScreenFrame, text="Dev Screen")
        self.devLabel.pack()
        #button to add a room 
        self.addRoomButton = tk.Button(self.devScreenFrame, text="Add Room")
        self.addRoomButton.pack()
        #entry for room name 
        self.roomNameLabel = tk.Label(self.devScreenFrame, text="New Room Name")
        self.roomNameLabel.pack()
        self.roomNameEntry = tk.Entry(self.devScreenFrame)
        self.roomNameEntry.pack()
        #drop down to select a room
        self.selectRoomDropDown = tk.OptionMenu(self.devScreenFrame,1,1)
        self.selectRoomDropDown.pack()
        #button to add a new lamp, curtain, and the 3 sensors
        self.addLampButton = tk.Button(self.devScreenFrame, text="Add Lamp")
        self.addLampButton.pack()
        self.addCurtainButton = tk.Button(self.devScreenFrame, text="Add Curtain")
        self.addCurtainButton.pack()
        self.addMotionSensorButton = tk.Button(self.devScreenFrame, text="Add Motion Sensor")
        self.addMotionSensorButton.pack()
        self.addLightSensorButton = tk.Button(self.devScreenFrame, text="Add Light Sensor")
        self.addLightSensorButton.pack()
        self.addSoundSensorButton = tk.Button(self.devScreenFrame, text="Add Sound Sensor")
        self.addSoundSensorButton.pack()

        # --------------------------#




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
    def devScreen(self):
        self.hideAllScreens()
        self.devScreenFrame.pack()
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
            self.checkBoxVars.append(tk.IntVar())
            curtainOpen = tk.Checkbutton(curtainHold, text="Closed", variable=curtain.closed)

            if curtain.closed:
                curtainOpen.select()
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
            sensorSettings["command"] = lambda arg1=sensor: self.sensorSettings(arg1)
            sensorSettings.pack()
            self.roomInfo.append(sensorHold)
        # add the same for sensors

    def sensorSettings(self, sensor):
        # change activation threshold
        self.hideAllScreens()
        # show settings screen & light settings
        self.settingsScreen.pack()
        self.sensorSettingFrame.pack()
        
        if sensor.activated:
            self.sensorCheckButton.select()
        self.sensorThreshhold["to"] = sensor.MAX
        self.sensorThreshhold.set(sensor.thresh)


    def curtainSettings(self, curtain):
        self.hideAllScreens()

    def lightSettings(self, light):
        # hide the other screen
        self.hideAllScreens()
        # show settings screen & light settings
        self.settingsScreen.pack()
        self.lightSettingsFrame.pack()
        #show light's current settings
        if light.activated:
                self.checkOn.select()
        #self.checkOn["command"]= lambda value=1:light.setActivated(value,colour)
        self.brightness.set(light.brightness)
        self.brightness["command"] = light.setBrightness
        self.red.set(light.colour[0])
        self.red["command"] = lambda value=1,colour = 0:light.editColour(value,colour) #the value var gets replaced with the value from the scale
        self.green.set(light.colour[1])
        self.green["command"] = lambda value=1,colour = 1:light.editColour(value,colour) #the colour responds to the RGB position
        self.blue.set(light.colour[2])
        self.blue["command"] = lambda value=1,colour = 2:light.editColour(value,colour)

    def hideAllScreens(self):
        self.homeScreen.pack_forget()
        self.roomScreen.pack_forget()
        self.settingsScreen.pack_forget()
        self.lightSettingsFrame.pack_forget()
        self.sensorSettingFrame.pack_forget()
        self.devScreenFrame.pack_forget()
        # & curtain

    def removeWidgets(self, widgetArray):
        for wid in widgetArray:
            wid.destroy()
        widgetArray.clear()


    def saveData(self):
        with open('savedData.txt', 'w') as save_data:
            for i in self.rooms:
                save_data.write("Room Name: ")
                save_data.write(i.name)
                save_data.write('\n')
                save_data.write("Lamp ID's: ")

                for j in i.lamps:
                    save_data.write(j.getID)
                    save_data.write(', ')

                save_data.write('\n')
                save_data.write("Curtain ID's: ")

                for j in i.curtains:
                    save_data.write(j.getID)
                    save_data.write(', ')
            
                save_data.write('\n')
                save_data.write("Light Sensor ID's: ")

                for j in i.lightSensors:
                    save_data.write(j.getID)
                    save_data.write(', ')
            
                save_data.write('\n')
                save_data.write("Sound Sensor ID's: ")

                for j in i.soundSensors:
                    save_data.write(j.getID)
                    save_data.write(', ')

                save_data.write('\n')
                save_data.write("Motion Sensor ID's: ")

                for j in i.motionSensors:
                    save_data.write(j.getID)
                    save_data.write(', ')

