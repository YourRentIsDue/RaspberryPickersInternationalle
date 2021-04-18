import tkinter as tk
class Room():
    def __init__(self,name, lamps = [], sensors = []):
        self.name = name
        self.lamps = lamps
        self.sensors = sensors
    def addLamp(self, lamp):
        self.lamps.append(lamp)
    def addSensor(self, sensor):    
        self.sensors.append(sensor)

class Application(tk.Frame):
    def __init__(self,rooms, master=None):
        super().__init__(master)
        self.rooms = rooms
        self.master = master
        self.master.minsize(400,600)
        #self.master.maxsize(400,600)
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        self.homeScreen = tk.Frame(self,width=400, height=600, bg="red")
        self.homeScreen.pack()
        self.homeScreen.pack_forget()

        self.roomScreen = tk.Frame(self,width=400,height=600, bg="blue")
        self.roomScreen.pack()

        self.back = tk.Button(self.roomScreen, text="Back", command=self.backButton)
        self.back.pack()

        self.roomList = []
        self.checkButtons = []

        self.title = tk.Label(self.homeScreen,text="Title App", font=("Courier", 16))
        self.title.pack(side="top", pady=5)
        self.hi_there = tk.Button(self.homeScreen)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.testButton
        self.hi_there.pack(side="top")
    
        self.roomFrame = tk.Frame(self.homeScreen, bg="blue", height=20, width=50, bd=2)
        self.roomFrame.pack(padx=20,pady=20)

        for room in self.rooms:
            self.addRoom(room.name)

    def addRoom(self, roomName = "test"):
        self.roomButton = tk.Button(self.roomFrame, text=roomName, command=self.openRoom)
        self.roomButton.pack(side="top",padx=2,pady=10)
        self.roomList.append(self.roomButton)

    def openRoom(self, room):
        self.homeScreen.pack_forget()
        self.roomScreen.pack()
    def backButton(self):
        self.roomScreen.pack_forget()
        self.homeScreen.pack()
    def testButton(self):
        test = tk.Checkbutton(self.roomFrame, text="abc")
        test.pack(side="top")
        self.checkButtons.append(test)

root = tk.Tk()
rooms = []
rooms.append(Room("test",["a", "b", "c"]))
rooms.append(Room("Bathroms",["c", "d", "e"]))
app = Application(rooms, master=root)
app.mainloop()