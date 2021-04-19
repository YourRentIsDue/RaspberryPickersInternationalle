import tkinter as tk
from Room import Room

class Application(tk.Frame):
    def __init__(self,rooms, master=None):
        super().__init__(master)
        self.rooms = rooms

        self.master = master
        self.master.minsize(400,600)
        #self.master.maxsize(400,600)
        self.roomList = []
        self.lampButtons = []
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        #Home screen----------#

        #create home frame
        self.homeScreen = tk.Frame(self,width=400, height=600, bg="red")
        self.homeScreen.pack()

        #add home screen title
        self.title = tk.Label(self.homeScreen,text="Title App", font=("Courier", 16))
        self.title.pack(side="top", pady=5)

        #create frame to hold rooms
        self.roomFrame = tk.Frame(self.homeScreen, bg="blue", height=20, width=50, bd=2)
        self.roomFrame.pack(padx=20,pady=20)

        #add room list
        for room in self.rooms:
            self.addRoom(room)

        #----------------------#

        #Room screen-----------#

        #create screen frame
        self.roomScreen = tk.Frame(self,width=400,height=600, bg="blue")
        self.roomScreen.pack(fill=None, expand=False)
        self.roomScreen.pack_forget()

        #add screen title
        self.roomTitle = tk.Label(self.roomScreen,text="Test", font=("Courier", 16))
        self.roomTitle.pack()

        #add back button
        self.back = tk.Button(self.roomScreen, text="Back", command=self.backButton)
        self.back.pack()

        #frame to hold the lights
        self.lightFrame = tk.Frame(self.roomScreen, bg="red", bd=2)
        self.lightFrame.pack()
        self.lightTitle = tk.Label(self.lightFrame,text="Lights")
        self.lightTitle.pack()

        #frame to hold the sensors
        self.sensorFrame = tk.Frame(self.roomScreen, bg="green", bd=2)
        self.sensorFrame.pack()
        self.sensorTitle = tk.Label(self.sensorFrame,text="Sensors")
        self.sensorTitle.pack()

        #-------------------#


    def addRoom(self, room):
        self.roomButton = tk.Button(self.roomFrame, text=room.name)
        self.roomButton["command"] = lambda arg1=room : self.openRoom(arg1)
        self.roomButton.pack(side="top",padx=2,pady=10)
        self.roomList.append(self.roomButton)

    def backButton(self):
        self.roomScreen.pack_forget()
        self.homeScreen.pack()

    def openRoom(self, room):
        self.homeScreen.pack_forget()
        self.roomScreen.pack(fill=None, expand=False)
        self.roomTitle["text"] = room.name
        self.removeWidgets(self.lampButtons)
        for lamp in room.lamps:
            lampButton = tk.Checkbutton(self.lightFrame, text=lamp)
            lampButton.pack(side="top")
            self.lampButtons.append(lampButton)
        #add the same for sensors
        

    def removeWidgets(self, widgetArray):
        for wid in widgetArray:
            wid.destroy()
        widgetArray.clear()
 

root = tk.Tk()
rooms = []
rooms.append(Room("test",["a", "b", "c"]))
rooms.append(Room("Bathroms",["c", "d", "e"]))
app = Application(rooms, master=root)
app.mainloop()